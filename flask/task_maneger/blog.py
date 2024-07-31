#اكواد خاصة بانشاء المهمات
from flask import Flask, request, redirect, url_for, render_template, flash, session,g,Blueprint,abort
import functools,sqlite3
DATABASE = 'posts.db'


#هذا الكائن مشابه للكائن Flask
#-اسم كائن بلو برنت
#-مكان تعريف هذا الكائن
#- (اختياري اذا باغي تضيف مسار)المسار المضاف لكل مكان معرف كبلو برنت لهذا الكائن
bp = Blueprint('blog', __name__, url_prefix="/")
#التطبيقات متبوعة APP

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


#داله نسوي لها بعدين دكريتر
def login_required(func):
    #ينسخ البيانات الداله المزخرف بها الى الداله المزخرفة
    @functools.wraps(func)
    def wrapped_func(**kwrd):
        #اذا لا يوجد مستخدم رجع لصفحة تسجيل الدخول
        if g.user is None:
            return redirect(url_for('auth.login'))
        return  func(**kwrd)
    return wrapped_func
#جلب مقاله
def get_post(post_id, chack_author = True):
    post = get_db().execute("SELECT * FROM posts WHERE id = ?", (post_id,)).fetchone()
    if post is None:
        abort(404, f"المقاله ذان المعرف {post_id} غير موجود")

    #منع المستخدمين من تعديل مقالات الغير
    if chack_author and post["auther_id"] != g.user["id"]:
        abort(403)

    return post
@bp.route('/posts')
def index():
    connection = get_db()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

@bp.route('/posts/<int:post_id>')
def show(post_id):
    post = get_post(post_id, False)
    return render_template("show.html", post=post)




@bp.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create():
    #اذا ارسل لها بوست (بعد ملء الاستمارة)
    if request.method =='POST':
        #من الاستمارة
        title = request.form['title']
        body = request.form['body']
        #نضيف لقاعدة البيانات
        connection = get_db()
        # g.user["auther_id"]
        if session.get("user_id") == None:
            return redirect(url_for("blog.index"))
        connection.execute("INSERT INTO posts (title, body, auther_id) VALUES (?, ?, ?)", (title, body, g.user["id"]))
        connection.commit()
        connection.close()
        #بعد ملئ الاستمارة اعدنا للامتدادا المكتوب (للصفحة الرئيسية)
        # return redirect("/posts")#الطريقة الي تحت افضل
        #يمكن نغيير المسار او نعدل بالمشروع ويتغير الامتدتد لذا هناك طريقة اخرى يستكشن الامتداد عن طريق كتابة اسم الداله
        return redirect(url_for("auth.login"))
    # يطلب ملء الاستمارة عند الجيت     
    return render_template("create.html")


@bp.route('/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update(post_id):
    post = get_post(post_id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = "العنوان مطلوب"

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('UPDATE posts SET title = ?, body = ? WHERE id = ?', (title, body, post_id))
            db. commit()
            db.close()
            return redirect(url_for('blog.index'))

    return render_template('create.html', post=post )



@bp.route('/<int:post_id>/delete', methods=['POST'])
@login_required
def delete(post_id):
    post = get_post(post_id )
    db = get_db()
    db.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    db.commit()
    db.close()
    return  redirect(url_for('blog.index'))