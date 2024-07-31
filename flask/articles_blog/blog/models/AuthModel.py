from blog import db, login_manager, cfg # من ملف __init__
from sqlalchemy.sql import func
from flask_login import UserMixin
from itsdangerous.url_safe import URLSafeSerializer

# تاخذ الايدي المستخدم بجلسة المستخدم وترجع كائن المستخدم لذاك الاي دي
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




#جدول
# تخليعها ترث من يوزر ميكسن لمعرفة اذا كان مسجل ام لا سابقا (داله داخل المتحكم)
class User(db.Model, UserMixin):
    #صف من نوع انتجر
    id = db.Column(db.Integer, primary_key=True)
    #صف من نوع ديت تايم
    join_date = db.Column(db.DateTime(timezone = True), server_default=func.now())
    # تمكين دعم المنطقة الزمنية timezone = True
    # الوقت البديل هو الوقت حسب قاعدة البيانات وليس المستخدم
    # لان الوقت يختلف من مكان لاخر
    
    # صف من نوع سترنج 30 حرف
    username = db.Column(db.String(80), unique=False, nullable=False)
    # nullable=False يجب ان لا يكون نلل
    # unique=False عادي يكون غير مميز   
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    # default=False القيمة الافتراضية
    #عمود وهمي لا يضهر بقاعدة البيانات يجعلك تصل للمقالات
    articales = db.relationship("Article", backref="user", lazy=True)
    stripe_customers = db.relationship("StripeCustomer", backref="user", lazy=True)
    Like = db.relationship("Like", backref="user", passive_deletes=True)
    
    def get_reset_token(self):
        # salt تحديد سياق التوقيع
        # cfg.SECRET_KEY العنصر الي يشفر منه
        # يولد كلمة عن طريق المزج بين الكلمة الرئيسية والملح "سالت"
        sign = URLSafeSerializer(cfg.SECRET_KEY, salt="PasswordReset")
        # يكون رمز مخصص الاليدي المحدد
        return sign.dumps(self.id)
    
    # لا ينشا نسخة من الكان بكل مرة نستدعي بها الكلاس
    @staticmethod
    def verify_reset_token(token):
        sign = URLSafeSerializer(cfg.SECRET_KEY, salt="PasswordReset")
        try:
            # المفتاح الذي يرسله المستخدم token
            # عمر المفتاح بالثانية max_age (المفتاح مفعل لساعة واحدة فقط)
            user_id = sign.load(token, max_age=3600)["user_id"]
            # يضهر خطا عند انهائ المدة
        except:
            return None
        return User.query.get(user_id)
        
    
    # تحل محل السترنج
    def __repr__(self):
        return f"User('{self.username}'. '{self.email}')" 
    