import sqlite3, random
from config import test_db_rows, test_database, names as seed_name, ages as seed_ages   
def create_database():   
    sql_ = sqlite3.connect(test_database)
    cur = sql_.cursor()
    names = seed_name
    ages = seed_ages
    try:
        cur.execute("CREATE TABLE user_table(name STRING(7), age INTEGER)")
    except:
        result = cur.execute("SELECT * FROM user_table").fetchall() 
        sql_.close()
        return result
    
    for _ in range(test_db_rows):
        name = random.choice(names)
        age = random.choice(ages)
        cur.execute("INSERT INTO user_table(name, age) VALUES(?, ?)", (name, age))
    sql_.commit()
    result = cur.execute("SELECT * FROM user_table").fetchall() 
    sql_.close()
    return result
    
# اخذ سوال عشوائي
def random_question(db_dir):
    sql_ = sqlite3.connect(db_dir)
    cursor = sql_.cursor()
    result = cursor.execute("SELECT * FROM main ORDER BY RANDOM() LIMIT 1").fetchone()
    sql_.close()
    return result
    
    
# تطبيق استعلام اس كيو ال على قاعدة بياانات محددة
def connect_database(file_name, query):
    sql_ = sqlite3.connect(file_name)
    cur = sql_.cursor()
    result = cur.execute(query).fetchone()
    sql_.close()
    return result

# يستخرج متغيرات اللزمة من السوال
def get_key_value(question, num):
    if num == 1:
        # استخراج الاسم
        # how many Ahmed there?
        name = question.replace("how many ","").replace(" there?","").strip()
        return name
    if num == 2:
        # استخراج العمر
        # How many people are 14 years old?
        age = int(question.replace("How many people are ","").replace(" years old?","").strip())
        return age
    if num == 3:
        # استخراج الاسم والعمر
        # How many people are 31 years old and named Mohamed?
        age,name = question.replace("How many people are ","").replace(" years old and named ",",").replace("?","").strip().split(",")
        return age,name