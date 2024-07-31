from blog import db
from sqlalchemy.sql import func
#جدول
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime(timezone = True), server_default=func.now())
    #لا نخزن الصورة بقاعدة البيانات بل الاسم فقط عشان المساحة
    artical_img = db.Column(db.String(255), nullable=False, default="default.png")
    # انشا علاقة واحد لواحد بين هذا العمود و العمود اي دي بالصف يوزر
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    # الكلاس User
    # الجدول user
    
    Like = db.relationship("Like", backref="articale", passive_deletes=True)

    # تحل محل السترنج
    def __repr__(self):
        return f"Articale('{self.user_id}'. '{self.title}')" 