from flask import Blueprint
# from blog.controllers.MainController import MainController
from blog.controllers.auth.UserController import UserController
from blog.controllers.auth.AdminController import AdminController
AuthRouter = Blueprint("auth_controller", __name__)



AuthRouter.route("/register", methods=["GET", "POST"])(UserController.user_register)
AuthRouter.route("/login", methods=["GET", "POST"])(UserController.user_login)
AuthRouter.route("/logout", methods=["GET"]) (UserController.user_logout)
AuthRouter.route("/reset_password", methods=["GET", "POST"])(UserController.reset_request)
# token المفتاح الفريد
AuthRouter.route("/reset_password/<token>", methods=["GET", "POST"])(UserController.reset_pass)

AuthRouter.route("/account") (UserController.user_account)
AuthRouter.route("/sub-panel/users-controller") (AdminController.users_control)
AuthRouter.route("/sub-panel/role-grant/<int:user_id>") (AdminController.role_grant)
AuthRouter.route("/sub-panel/role-revoke/<int:user_id>") (AdminController.role_revoke)

AuthRouter.route("/sub-panel/satatistics") (AdminController.sub_panel)