from flask import render_template
from blog.models.ArticleModel import Article
from blog.models.AuthModel import User
from blog.utils.MainUtilis import Paginate
from blog import cfg
class MainController:
    def home():
        # order_by ترتيب حسب
        # Article.createrd_date.desc() تاريخ انشائ المقاله بالعكس(احدث المقالات)
        # artical_list = Article.query.order_by(Article.created_date.desc()).all() 
        artical_list = Article.created_date.desc()
        pagination, article_per_page = Paginate(cfg.POSTES_PER_PAGE ,Article ,artical_list)       
        return render_template("main/home.jinja", title="مدونة حاسوب", article_per_page=article_per_page ,pagination=pagination)