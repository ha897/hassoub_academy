from flask import Blueprint
from blog.controllers.MainController import MainController
from blog.controllers.ArticleController import ArticleController

ArticleRouter = Blueprint("article_controller", __name__, url_prefix="/article")
#يشير للفنكشن 
#والفنكشن تشير لصفحة الاتش تي ام ال ترسل لها النموزج للملئ 
# عند ملئه يعود لنفس الداله صفحة الاتش تي ام ال لنفس الداله
# ليكون استوفى الشروط ليحفض بقاعدة البيانات
ArticleRouter.route("/article_add", methods=["GET", "POST"])(ArticleController.article_add)
ArticleRouter.route("/<int:id>", methods=["GET"])(ArticleController.article_show)
ArticleRouter.route("/<int:id>/like", methods=["POST"])(ArticleController.article_like)
ArticleRouter.route("/<int:id>/update", methods=["GET", "POST"])(ArticleController.article_update)
ArticleRouter.route("/<int:id>/delete", methods=["GET"])(ArticleController.article_delete)
ArticleRouter.route("/article_list", methods=["GET"])(ArticleController.article_list)