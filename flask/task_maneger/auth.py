from flask import Flask, request, redirect, url_for, render_template, flash, session,g,Blueprint
import functools,sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from blog import get_db


bp = Blueprint('auth', __name__)



#تسجيل الدخول
@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        #متغير للتعبير عن الخطا
        error = None

        if not username:
            error = "اسم المستخدم مطلوب"
        if not email:
            error = "الايميل مطلوب"

        if not password:
            error = "كلمة المرور مطلوبة"


        #اذا لا يوجد اي اخطاء
        if  error is None:
            db = get_db()
            try:
                #generate_password_hash للتشفير 
                db.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, generate_password_hash(password)) )
                db.commit()
                db.close()

            #معنا هذا الارور ان هذا العنصر مكرر
            except db.IntegrityError:
                error = f"{username}مسجل بالفعل"
            else:
            #عرض رساله الخطا
                return redirect(url_for("login"))
            flash(error)

    return render_template("auth/register.html")

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('blog.index'))
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        error = None
        db = get_db()
        
        user = db.execute("SELECT * FROM users WHERE email=?", (email,)).fetchone()
        
        
        
        if not email:
            error = "البريد الالكتوني غير موجود"

        elif not check_password_hash(user["password"], password):
            error = "كلمة المرور خاطئة"
        #لا يوجد اخطاء
        if error is None:
            #قاموس عبارة عن كوكيز
            session.clear()
            session["user_id"] = user["id"]
            return redirect(url_for("blog.index"))
        flash(error)



    return render_template('auth/login.html')


#داله تعمل قبل اي طلب
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if user_id == None:
        g.user = None

    else:
        g.user = get_db().execute("SELECT * FROM users WHERE id =?", (user_id, )).fetchone()



@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('blog.index'))


@bp.route("/profile")
def profile():
    print(g.user)
    return render_template('auth/profile.html')
