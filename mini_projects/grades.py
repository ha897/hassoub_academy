grades = int(input("enter the grades: "))
if grades not in range(0,101):
    print("the grade is wrong!")
    exit()
if grades >= 90:
    print("Your Grades is A")
elif grades >= 80:
    print("Your Grades is B")
elif grades >= 70:
    print("Your Grades is C")
elif grades >= 60:
    print("Your Grades is D")
elif grades >= 50:
    print("Your Grades is E")
else:
    print("Your Grades is F")