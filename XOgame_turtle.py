import turtle, random, time, pyautogui
def main():
    #اماكن الاكس والاو
    chises = [1,2,3,4,5,6,7,8,9]
    turtle.pensize(10)
    # 300 300
    turtle.setup(width=350, height=350, startx=0, starty=0)#مقاس اللوحة
    # turtle.screensize(300,300)
    #احداثيات رسم الخطوط
    listT = [(-50,150,270), (50,150, 270), (150,50, 180), (150,-50, 180)]
    #شكل الخارجي
    for i in listT:
        turtle.penup()
        turtle.goto(i[0], i[1])
        # ضبط السلحفاة على زاوية معينة
        turtle.setheading(i[2])
        turtle.pendown()
        turtle.forward(300)

    x = []
    o = []
    #الاحداثيات الي يكون عندها فاز المستخدم
    wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
             [1, 4, 7], [2, 5, 8], [3, 6, 9],
             [1, 5, 9], [3, 5, 7]]
    
    




    for i in range(9):

        #العدد الزوجي والفردي يبدل بينك وبين الكمبيوتر
        if i%2 != 0:
            num = int(pyautogui.prompt("enter your location(1 - 9):"))#اضهار شعار منبثق لاخذ رقم
            while num < 1 or num > 9 or (num not in chises):
                num = int(pyautogui.prompt("enter your location(1 - 9):"))#ضهار شعار منبثق لاخذ رقم
            exceTT(num)
            x.append(num)
            chises.remove(num)
        else:
            num = random.choice(chises)
            cercleTT(num)
            o.append(num)
            chises.remove(num)#اذا تم اخيار المكان لا يختار مرة اخرى
        chackeX = []
        for test in wins:
            chackeX.append(all(i in x for i in test))

        if any(chackeX):
            pyautogui.alert("x win")
            exit()
            
        chackeY = []
        for test in wins:
            chackeY.append(all(i in o for i in test))

        if any(chackeY):
            pyautogui.alert("y win")
            exit()

    #تعادل 
    print("equ")
    exit()


    # while True:
    #     test = int(input("enter "))
    #     exceTT(test)

#الاو
def cercleTT(sqr):
    #اذا اخترنا 1 مثلا يحطنا باحداثيات الصحيحة للرسم
    if sqr == 1: sqr = (-100, 50 + 15)
    if sqr == 2: sqr = (0, 50 + 15)
    if sqr == 3: sqr = (100, 50 + 15)

    if sqr == 4: sqr = (-100, -50 + 15)
    if sqr == 5: sqr = (0, -50 + 15)
    if sqr == 6: sqr = (100, -50 + 15)

    if sqr == 7: sqr = (-100, -150 + 15)
    if sqr == 8: sqr = (0, -150 + 15)
    if sqr == 9: sqr = (100, -150 + 15)
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(sqr[0], sqr[1])
    turtle.pendown()

    # نصف القطر
    turtle.circle(35)

#الاكس
def exceTT(sqr):
    #اذا اخترنا 1 مثلا يحطنا باحداثيات الصحيحة للرسم

    if sqr == 1: sqr = (-150 + 15, 50 + 15)#1
    if sqr == 2: sqr = (-50 + 15, 50 + 15)#2
    if sqr == 3: sqr = (50 + 15, 50 + 15)#3

    if sqr == 4: sqr = (-150 + 15, -50 + 15)#4
    if sqr == 5: sqr = (-50 + 15, -50 + 15)#5
    if sqr == 6: sqr = (50 + 15, -50 + 15)#6

    if sqr == 7: sqr = (-150 + 15, -150 + 15)#7
    if sqr == 8: sqr = (-50 + 15, -150 + 15)#8
    if sqr == 9: sqr = (50 + 15, -150 + 15)#9
    turtle.setheading(45)

    turtle.penup()
    turtle.goto(sqr[0], sqr[1])
    turtle.pendown()

    turtle.forward(100)
    turtle.forward(-50)
    turtle.right(90)
    turtle.forward(50)
    turtle.forward(-100)



main()