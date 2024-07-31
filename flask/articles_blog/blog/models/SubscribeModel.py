from blog import db

class StripeCustomer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscription_type = db.Column(db.String(20), nullable=True, unique=False)
    status = db.Column(db.String(20), nullable=True, unique=False)#الحاله
    customer_id = db.Column(db.String(255), nullable=True, unique=False) # معرف اي دي العميل
    subscription_id = db.Column(db.String(255), nullable=True, unique=False) # معرف اي دي الاشتراك
    amount = db.Column(db.Integer) # الكمية
    subscription_start = db.Column(db.DateTime) # تاريخ بدئ الاشتراك
    subscription_end = db.Column(db.DateTime) # تاريخ انتهاء الاشتراك
    subscription_canceled = db.Column(db.Boolean, nullable=True) # حاله الاشتراك الان
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def _repr_(self):
        return f"Customer('{self.user_id}'. '{self.status}')"