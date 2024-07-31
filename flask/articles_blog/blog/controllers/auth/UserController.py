from blog.models.AuthModel import User
from blog.models.SubscribeModel import StripeCustomer
from blog.forms.AuthForm import LoginForm, RegistrationForm, RequestResetForm, RequestPasswordForm
from blog import bcrypt, db, cfg
from flask_login import login_user, current_user, logout_user, login_required
from flask import redirect, url_for, flash, request, render_template
from blog.utils.AuthUtils import send_reset_email
from flask_paginate import Pagination
class UserController:
    def user_login():
        # اذا كان مسجل الدخول سابقا اعده لصفحة الرئيسية لازم تخلي الجدول يوزر يرث من يوزر ميكسن
        if current_user.is_authenticated:
            return redirect(url_for('main_controller.home'))
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user is not None and bcrypt.check_password_hash(user.password, form.password.data):
                
                login_user(user, remember=form.remember.data)
                flash("تم تسجيل الدخول بنجاح", "success")
                # return redirect(url_for(request.args.get("next")) or url_for("main_controller.home"))
                try:
                    return redirect(url_for(request.args.get("next")))
                except:
                    return redirect(url_for("main_controller.home"))
            else:
                flash("فشل بتسجيل الدخول! تاكد من كتابة البريد الالكتروني وكلمة السر بشكل صحيح", "danger")
                # return redirect(url_for("main_controller.user_login"))
                return redirect(url_for("auth_controller.user_login"))
            
        return render_template("auth/login.jinja", form=form, title="تسجيل الدخول")
    
    
    def user_register():
        if current_user.is_authenticated:
            return redirect(url_for('main_controller.home'))
        form = RegistrationForm()
        if form.validate_on_submit():
            passwordH = bcrypt.generate_password_hash(form.password.data).decode("UTF-8")
            user = User(username=form.username.data,email=form.email.data, password=passwordH)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            username = form.username.data
            flash(f"اهلا بك {username}بمدونة حاسوب قم بالاشتراك لقرائة المقالات", "success")
            return redirect(url_for("auth_controller.user_login"))
        return render_template("auth/register.jinja", form=form, title="انشائ حساب")
    
    # لا يمكن الوصول لها الا اذا كنت مسجل دخول
    @login_required
    def user_logout():
        logout_user()
        flash("تم تسجيل الخروج", "warning")
        return redirect(url_for("main_controller.home"))
    
    def reset_request():
        # اذا مسجل دخول
        if current_user.is_authenticated:
            return redirect(url_for("main_controller.home"))
        form = RequestResetForm()
        # استوفا شروظ
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            # ارسال بريد الكتروني
            send_reset_email(user)
            flash("تم ارسال رابط لاعادة تعيين كلمة السر")
            return redirect(url_for("auth_controller.user_login"))
        
        return render_template("auth/reset_request.jinja", title= "اعادة تعيين كلمة المرور", form=form)
        
        
    def reset_pass(token):
        if current_user.is_authenticated:
            return redirect(url_for("main_controller.home"))
        user = User.verify_reset_token(token)
        
        if user is None:
            # انتهت المدة الزمنية
            flash("انتهت صلاحية الرابط حاول مرة اخرى", "warning")
            return redirect(url_for("auth_controller.reset_request"))
        form = RequestPasswordForm()
        if form.validate_on_submit():
            passwordH = bcrypt.generate_password_hash(form.password.data).decode("UTF-8")
            user.password = passwordH
            db.sesstion.commit()
            flash("تم تغيير كلمة المرور بنجاح", "success")
            return redirect(url_for("auth_controller.user_login"))
        return render_template("auth/reset_pass.jinja", title="اعادة تعيين كلمة السر", form=form)
    @login_required
    def user_account():
        if current_user.is_admin:
            pagination = Pagination(total=len(current_user.articales))
            return render_template("auth/account.jinja", pagination=pagination)
        
        # التاكد من انه مشترك او لا
        customer = StripeCustomer.query.filter_by(user_id=current_user.id).first()
        if customer and customer.subscription_id is not None:
            title = f"Le {current_user.username}"
            
            return render_template("auth/account.jinja", title=title, customer=customer, prices=cfg.prices)
        else:
            return render_template("auth/account.jinja")