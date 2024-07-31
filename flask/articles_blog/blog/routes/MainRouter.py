from flask import Blueprint
from blog.controllers.MainController import MainController

MainRouter = Blueprint("main_controller", __name__)

# عند هذا الامتداد شغل الداله المحددة من داخل كلاس
MainRouter.route("/")(MainController.home)
