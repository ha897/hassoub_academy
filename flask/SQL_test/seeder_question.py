import sqlite3,random
from config import main_databases, names, ages

    
def create_question_database_1():
    sql_ = sqlite3.connect(main_databases[0])
    cur = sql_.cursor()
    try:
        cur.execute("CREATE TABLE main(question Text, answer Text)")
    except:
        print("table 1 already exists.")
        return
    for name in names:
        cur.execute("INSERT INTO main(question , answer) VALUES(?, ?)", 
                    (f"how many {name} there?", f"SELECT COUNT(*) FROM user_table WHERE name = '{name}'"))

    sql_.commit()
    sql_.close()
    print("Create table 1 successfully.")
    
def create_question_database_2():
    sql_ = sqlite3.connect(main_databases[1])
    cur = sql_.cursor()
    try:
        cur.execute("CREATE TABLE main(question Text, answer Text)")
    except:
        print("table 2 already exists.")
        return
    for age in ages:
        cur.execute("INSERT INTO main(question , answer) VALUES(?, ?)", 
                    (f"How many people are {age} years old?", f"SELECT COUNT(*) FROM user_table WHERE age = {age}"))

    sql_.commit()
    sql_.close()
    print("Create table 2 successfully.")
    
def create_question_database_3():
    sql_ = sqlite3.connect(main_databases[2])
    cur = sql_.cursor()
    try:
        cur.execute("CREATE TABLE main(question Text, answer Text)")
    except:
        print("table 3 already exists.")
        return
    # انشائ نسخة مرتبة عشوائيا
    shuffled_names = random.sample(names, len(names))
    shuffled_ages = random.sample(ages, len(ages))

    for name, age in zip(shuffled_names, shuffled_ages):
        cur.execute("INSERT INTO main(question , answer) VALUES(?, ?)", 
                    (f"How many people are {age} years old and named {name}?", f"SELECT COUNT(*) FROM user_table WHERE age = {age} AND name = '{name}'"))
    
    sql_.commit()
    sql_.close()
    print("Create table 3 successfully.")
    
    
if __name__ == '__main__':
    create_question_database_1()
    create_question_database_2()
    create_question_database_3()
    print("all done.")