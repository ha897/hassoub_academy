import sqlite3,random, os
from flask import Flask, render_template, request, redirect, url_for, send_file
from helpers import create_database, random_question, connect_database, get_key_value
from config import main_databases, test_database
app = Flask(__name__)

# الصفحة الرئيسية
@app.route("/")
def index():
    return render_template("home.jinja")

# صفحة الاختبار
@app.route("/test/<int:num>", methods=["GET", "POST"])
def test(num):
    # يمثل num الصعوبة
    # انشاء قاعدة بيانات الاختبار اذا لم تكن موجودة
    result = create_database()
    
    if request.method == "GET":
    # الاستجابة غيت لاختيار سؤال واخذ اجابة من المستخدم
        question,answer = random_question(main_databases[num-1])
        return render_template("test.jinja", question=question)
    else:
    # الاستجابة بوست للتحقق من اجابة المستخدم واضهار النتيجة
        try:
            # اجابة المستخدم
            user_query = request.form["query"]
            # السوال النموزجية
            question = request.form["question"]
        except:
            return redirect(url_for("index"))
        
        if "drop" in user_query.lower():
            # فلاش حدث خطا
            return redirect(url_for("index"))
        
        # نجيب الاجابة الاسكيو ال من قاعدة البيانات
        data_query = connect_database(main_databases[num-1],f"SELECT answer FROM main WHERE question = '{question}'")[0]
        
        # اس كيو ال المستخدم نطلع منه النتيجة
        user_answer = str(connect_database(test_database,user_query)[0])
        # اس كيو ال النموزجية نطلع منه النتيجة
        data_answer = str(connect_database(test_database,data_query)[0])
        
        if num == 1:
            name = get_key_value(question, num)
            if user_answer == data_answer:
                result_stat = True
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, name = name)
            else:
                result_stat = False
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, user_answer = user_answer, data_answer = data_answer, name = name)
        elif num == 2:
            age = get_key_value(question, num)
            if user_answer == data_answer:
                result_stat = True
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, age = age)
            else:
                result_stat = False
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, user_answer = user_answer, data_answer = data_answer, age = age)
        elif num == 3:
            age, name = get_key_value(question, num)
            age = int(age)
            buth=True
            if user_answer == data_answer:
                result_stat = True
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, age = age, buth=buth)
            else:
                result_stat = False
                return render_template("test.jinja", question=question, result=result, result_stat = result_stat, user_answer = user_answer, data_answer = data_answer, age = age, buth=buth)

# تنزيل قاعدة بيانات الاختبار
@app.route("/dounlowd-database", methods=["POST"])
def downloud_database():
    
    return send_file(
                open(test_database,'rb'),
                #النوع 
                mimetype='application/vnd.sqlite3', as_attachment=True, 
                #اسم الملف اذا تم تنزيله
                download_name ='DATABASE.db'
            )

app.run(debug=True)