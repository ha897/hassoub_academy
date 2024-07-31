from dotenv import load_dotenv
from datetime import datetime
import os
from pathlib import Path
load_dotenv()
# ضبط اعدادات التهيئة العامة
# نخليها فولس لان بتسوي مشاكل امنية خارج بيئة التطوير
class Config():
    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")


# ضبط اعدادات عند التطوير
# DEBUGمفيدة للكشف عن الاخطاء
class DevelopmantCfg(Config):
    DEBUG = True
    # يجيب المسار المطلق لملف الاعدادت
    APP_DIR = Path(os.path.dirname(os.path.realpath(__file__)))
    VIEWS_DIR = APP_DIR / "template"
    CONTROLLER_DIR = APP_DIR / "controller"
    STATIC_DIR = APP_DIR / "static"
    IMAGES_DIR = STATIC_DIR / "images"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@localhost/{os.getenv("DATABASE_NAME")}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False #تجاهل تنبيهات اس كيو ال الكيمي عند حدوث تغييرات بقاعدة البيانات
    OWNER_USERNAME = os.getenv("OWNER_USERNAME")
    OWNER_EMAIL = os.getenv("OWNER_EMAIL")
    OWNER_PASSWORD = os.getenv("OWNER_PASSWORD")
    
    # seeder
    ACCOUNT_COUNT = 25
    ADMIN_PERCENTAGE = 10 #10%
    USER_PASSWORD = "123"
    
    # article
    ARTICLE_COUNT = 100
    
    # customer
    CUSTOMER_COUNT = 20
    START_DATE = datetime(2023,1,1)
    
    # like
    LIKE_COUNT = 200
    
    LOGIN_MSG = "يجب عليك الاشتراك لمشاهدة المحتوى"
    
    #mail
    MAIL_SERVER='sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    
    RESET_MAIL = "alshihy.567a@gmail.com"
    # عدد المقالات بالصفحة
    POSTES_PER_PAGE = 9
    STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
    STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
    
    STRIPE_WEBHOOK_KEY = os.getenv("STRIPE_WEBHOOK_KEY")
    
    # PRICES
    prices = {
        "yearly_subscription" : "price_1Ph1F0DmKD9C7pTkCJQupw78",
        "monthly_subscription" : "price_1Ph1FsDmKD9C7pTk78tJSk7u"
    }
    # عدد المقالات عند عرضها كسجل للادمن
    R_PER_PAGE = 20
    
    
    
    USERS_PER_PAGE = 15
# اعدادات الانتاج
class ProducionCfg(Config):
    pass



