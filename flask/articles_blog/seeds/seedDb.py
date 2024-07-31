from faker import Faker
from flask_seeder import Seeder
from blog import bcrypt, db, cfg

from blog.models.AuthModel import User 
from blog.models.ArticleModel import Article
from blog.models.SubscribeModel import StripeCustomer
from blog.models.LikeModel import Like

import os, random
from datetime import timedelta
fake = Faker("ar_AA")

class SeedDb(Seeder):
        
    def add_user(self):
        # لاعطاء معلومات وهمية fake.unique.first_name()
        # cfg.ACCOUNT_COUNT عدد المستخدمين من الاعدادات
        names = [fake.unique.first_name() + " " + fake.unique. last_name() for i in range(cfg.ACCOUNT_COUNT)]
        emails = [fake.unique. email() for i in range(cfg.ACCOUNT_COUNT)]
        for name, email in zip(names, emails):
            user = User(
                username = name,
                email = email,
                # كلمة المرور متشابهة لك المستخدمين الوهميين وموجودة بالاعدادات cfg.USER_PASSWORD
                password = bcrypt.generate_password_hash(cfg.USER_PASSWORD).decode('utf-8'),
                # cfg.ADMIN_PERCENTAGE  نسبة الترو من الاعدادات
                is_admin = fake.boolean(chance_of_getting_true = cfg.ADMIN_PERCENTAGE),
                # يجيب تاريخ عشوائي من هذه السنة
                join_date = fake.date_this_year()
            )
            print(user)
            db.session.add(user)
            # db.session.commit() تقوم المكتبة سيدر بعمل الحفض تلقائيا

    def add_article(self):
        
        # لازم المعدل على المقالات يكون ادمن
        admins = User.query.filter_by(is_admin=True).all()

        # اسماء الصور
        images = []
        # تحويل الامتداد سترنج الى بايتس
        directory = os.fsencode(cfg.IMAGES_DIR)
        
        for file in os.listdir(directory):
        # تحويل الامتداد بايتس الى سترنج
            filename = os.fsdecode(file)
            # التاكد من الامتداد
            if filename.endswith("png") or filename.endswith("jpg"):
                images.append(filename)
        # or
        # images = [ os.fsdecode(file) for file in os.listdir(directory) if os.fsdecode(file).endswith("png") or os.fsdecode(file).endswith("jpg") ]
        
        # عدد المقالات cfg.ARTICLE_COUNT
        for i in range(cfg.ARTICLE_COUNT):
            admin = random.choice(admins)
            img = random.choice(images)
            
            article = Article(
                title = fake.sentence(nb_words=7),
                content = fake.paragraph(nb_sentences=200),
                artical_img = img,
                user_id = admin.id,
                created_date = fake.date_this_year()
            )
            
            print(article)
            db.session.add(article)
            db.session.commit()

    def add_customer(self):
        # المشتركين يجب ان لا يكونو ادمن
        subscribers = User.query.filter_by(is_admin=False).all()
        for i in range(cfg.CUSTOMER_COUNT):
            # المشترك مرة واحدة فقط لذا بعد الاختيار نحذف
            subscriber = random.choice(subscribers)
            subscribers.remove(subscriber)
            
            subscription_start = fake.date_between(start_date=cfg.START_DATE)#ياخذ ويعيد كائن ديت تايم
            db_customer = StripeCustomer(
                user_id = subscriber.id,
                subscription_type = "year",
                status = "active",
                customer_id = fake.lexify(text="id_??????????"),
                subscription_id = fake.lexify(text="sub_??????????"),
                amount = 100,

                subscription_end = subscription_start + timedelta(days=30),
                subscription_canceled = False
            )
            print(db_customer)
            db.session.add(db_customer)
            db.session.commit()
            
    def add_likes(self):
        articles = Article.query.all()
        # المشتركين
        subscribers = StripeCustomer.query.filter_by(status="active").all()
        # الادمنوز
        admins = User.query.filter_by(is_admin=True).all()
        # كلاهما لهم صلاحية وضع لايك ندمجهم كالتالي
        subscribers.extend(admins)
        
        for article in range(cfg.LIKE_COUNT):
            liked_user = random.choice(subscribers).id
            liked_article = random.choice(articles).id
            print(liked_article, liked_user)
            like = Like(
                liked_user = liked_user,
                article_id = liked_article
            )
            # print(like)
            db.session.add(like)
            db.session.commit()


    def run(self):
        # self.add_user()
        # self.add_article()
        self.add_customer()
        # self.add_likes()