from blog.forms.ArticleForm import ArticleForm
from blog.models.ArticleModel import Article
from blog.models.SubscribeModel import StripeCustomer
from blog.models.AuthModel import User
from blog.models.LikeModel import Like
from blog.utils.ArticleUtils import save_image
from blog import db, cfg
from flask import url_for, render_template, flash, redirect, request, jsonify
from flask_login import current_user, login_required
from blog.utils.MainUtilis import Paginate

class ArticleController:
    @login_required
    def article_add():
        if current_user.is_admin is False:
            flash("لا تملك صلاحية الوصول للصفحة المطلوبة", "warning")
            return redirect(url_for("main_controller.home"))
        
        form = ArticleForm()
        # اسا استوفت شروط الفورم
        if form.validate_on_submit():
            if form.artical_img.data:
                # اذا ادخل المستخدم صورة احفضها مع الصور
                image_name = save_image(form.artical_img.data)
                new_article = Article(user_id=current_user.id, title=form.title.data, content=form.content.data, artical_img=image_name)
            else:
                
                # استخراج البيانات من النموزج
                # form.title.data استخراج بيانات العنون من النموزج
                new_article = Article(user_id=current_user.id, title=form.title.data, content=form.content.data)
                
            db.session.add(new_article)
            db.session.commit()
            flash("تم اضافة المقاله بنجاح","success")
            return redirect(url_for("main_controller.home"))
        return render_template("articles/article_add.jinja", form=form, legend= "اضافة مقاله جديدة", title="اضافة مقالة")
    
    def article_show(id):
        # اذا شي زين ما شي خطا 404
        article = Article.query.get_or_404(id)
        # هل مسجل دخول
        if current_user.is_authenticated:
            # نتاكد مناه مشترك
            customer = StripeCustomer.query.filter_by(user_id=current_user.id).first()
            admin = User.query.filter_by(id=current_user.id).first()
            # يكون المستخدم له سجل اشتراك ومفعل
            if customer and customer.status == "active":
                return render_template("articles/article.jinja", title=article.title, article=article, customer=customer, Admin=admin.is_admin)
            return render_template("articles/article.jinja", title=article.title, article=article, customer=None, Admin=admin.is_admin)
        return render_template("articles/article.jinja", title=article.title, article=article, customer=None, Admin=None)
    
    @login_required
    def article_list():
        if current_user.is_admin:
            artical_list = Article.created_date.desc()
            pagination, artical_list = Paginate(cfg.R_PER_PAGE ,Article ,artical_list)       
            return render_template("articles/articles_list.jinja", title="لائحة المقالات", artical_list=artical_list ,pagination=pagination)
        else:
            flash("لا تملك صلاحية الوصول للصفحة المطلوبة", "warning")
            return redirect(url_for("main_controller.home"))
        
    @login_required
    def article_like(id):
        if request.method == "GET":
            flash("لا تملك صلاحية الوصول للصفحة المطلوبة", "warning")
            return redirect(url_for("main_controller.home"))

        try:
            customer = StripeCustomer.query.filter_by(user_id=current_user.id).first()
            article = Article.query.filter_by(id=id).first()
            if (customer and customer.status == "active") or current_user.is_admin:
                
                like = Like.query.filter_by(liked_user=current_user.id, article_id=article.id).first()
                # اذكان معلق بلايك احذفه واذا ما كان علق به 
                if like:
                    db.session.delete(like)
                    db.session.commit()
                else:
                    like = Like(liked_user=current_user.id, article_id=article.id) 
                    
                    db.session.add(like)
                    db.session.commit()

                # يعيد عدد الرلايكات ونتحقق من وجود ايدي المستخدم في اي دي المستخدمين الي وضعو لايك
                return jsonify({"likes":len(article.Like), "liked":current_user.id in map(lambda x:x.liked_user, article.Like)}), 200
                    
                    
            else:
                flash("يجب عليك الاشتراك اولا", "danger")
                return redirect(url_for("article_controller.article_show"), id=article.id)
        except:
            print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwPP")
            # طلب مقاله غير موجودة
            flash("المقاله غير موجودة", "danger")
            return redirect(url_for("main_controller.home"))

        
        
    @login_required
    def article_update(id):
        if current_user.is_admin is False:
            flash("لا تملك صلاحية الوصول للصفحة المطلوبة", "warning")
            return redirect(url_for("main_controller.home"))
        
        form = ArticleForm()
        
        # حدد المقاله من الايدي اذا ما شي 404
        article = Article.query.get_or_404(id)
        # اسا استوفت شروط الفورم
        if form.validate_on_submit():
            if form.artical_img.data:
                # اذا ادخل المستخدم صورة احفضها مع الصور
                image_name = save_image(form.artical_img.data)
                
                article.artical_img = image_name
            article.title = form.title.data
            article.content = form.content.data
            db.session.commit()
            # بعد تعديل المقاله يعرضها
            flash("تم تعديل المقاله بنجاح","success")
            return redirect(url_for("article_controller.article_show", id = article.id))
        
        form.title.data = article.title
        form.content.data = article.content
        form.artical_img.data = article.artical_img
        return render_template("articles/article_add.jinja", form=form, legend= "تعديل المقاله", title="تعديل مقاله")
    
    @login_required
    def article_delete(id):
        article = Article.query.get_or_404(id)
        if current_user.is_admin:
            db.session.delete(article)
            db.session.commit()
            flash("تم حذف المقاله", "success")
            # return redirect(url_for("main_controller.home"))
            return redirect(url_for("article_controller.article_list"))
        else:
            flash("لا تملك الصلاحية للوصول للصفحة المطلوبة", "warning")
            return redirect(url_for("main_controller.home"))