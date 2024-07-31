import mimetypes
mimetypes.add_type("application/javascript",".js")

from flask import Flask, render_template
from flask_bcrypt import Bcrypt
from blog.config import ProducionCfg, DevelopmantCfg
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_seeder import FlaskSeeder
from flask_login import LoginManager
from flask_mail import Mail
from flask_ckeditor import CKEditor
import stripe
# from flask_paginate import 
"""Enable for Development mode"""
# سواء استخدمنا الكائن الاصلي او انشانا نسخة عادي
cfg = DevelopmantCfg
# cfg = DevelopmantCfg()
"""Enable for Production mode"""
# cfg = ProductionCfg

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
seeder = FlaskSeeder()
login_manager = LoginManager()
mail = Mail()
ckeditor = CKEditor()

stripe.api_key = cfg.STRIPE_SECRET_KEY
# تخصيص تسجيل الدخول
# ارسال المستخدم الغير مصادق عليه لصفحة تسجيل الدخول
login_manager.login_view = "auth_controller.user_login"
# رساله تضهر لمستخدم مجهول عند محاولة دخول صفحة محمية
login_manager.login_message = cfg.LOGIN_MSG
# نوع رسائل فللش الافتراضية
login_manager.login_message_category = "warning" #  تحزيرية تاخت تنسيقات التحذيرية مثل اللون الاحمر الخ


def creat_app():
    app = Flask(__name__,template_folder=cfg.VIEWS_DIR, static_folder=cfg.STATIC_DIR)
    app.config.from_object(cfg)
    # سلوك التطبيق او سياقه
    with app.app_context():
        # نعوض بالفنكشن لتسهيبل قرائة الكود
        # """التطبيق ابب هو كائن ليس ضروري تعويضه تعيده عند تغييره"""
        regester_extention(app)
        regester_blueprints(app)
        # التعامل مع الاخطائ
        register_errorhandlers(app)
        
        app.before_first_request(populate_database)
    return app


def regester_extention(app):
    # يعلم التطبيق ان يوجد كائن بيكربت
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)
    # التعامل مع تسجيل الدخول
    login_manager.init_app(app)
    # الايميلات ارسال 
    mail.init_app(app)
    
    ckeditor.init_app(app)
def regester_blueprints(app):
    # استدعاء كائنات بلو برنت
    from blog.routes.ArticleRouter import ArticleRouter
    from blog.routes.AuthRouter import AuthRouter
    from blog.routes.MainRouter import MainRouter
    from blog.routes.SubscribeRouter import SubscribeRouter
    # اضافة كل كائنات بلوبرنت
    app.register_blueprint(ArticleRouter)
    app.register_blueprint(AuthRouter)
    app.register_blueprint(MainRouter)
    app.register_blueprint(SubscribeRouter)
        
    
from blog.models.AuthModel import User
from blog.models.ArticleModel import Article
from blog.models. SubscribeModel import StripeCustomer
from blog.models.LikeModel import Like
# داله ملئ قاعدة البيانات
def populate_database():
    # التاكد من وجود الجداول اذا موجودة زين اذا لا انشاها
    db.create_all()
    if not User.query.filter_by(username = cfg.OWNER_USERNAME).first():
        user = User(
            username = cfg.OWNER_USERNAME,
            email = cfg.OWNER_EMAIL,
            # bcrypt تجمع بين الهاشنج والانكربشن
            password = bcrypt.generate_password_hash(cfg.OWNER_PASSWORD).decode("UTF-8"),
            is_admin = True     
        )
        # الاضافة لقاعدة البيانات
        db.session.add(user)
        db.session.commit()# الحفض بقاعدة اليانات        


   
def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, "code", 404)
	# اسم الملف 404
        return render_template(f"main/{error_code}.jinja", error_code= error_code,
                title="غير متوفر")

# قائمة بها 404 للتعامل مع هذا الخطا فقط
# يمكننا اضافة المزيد من الاخطاء [404, 505, 222] وانشاء صفحات الاتشس تي ام ال الخاصة بهم
    for errcode in [404]:
	# اذا شي ارور404 تصرف مثل ما موجود بالداله
        # تستخدم render_error  كديكوريتور تضع به كائن من نوع ارور 
        app.errorhandler(errcode)(render_error)

