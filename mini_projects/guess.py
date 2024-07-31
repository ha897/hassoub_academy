my_number = 6
user_guess = int(input("enter your guess: "))
if user_guess >= 0:
    if user_guess == my_number:
        print("YUU WIN!!!")
    elif (user_guess - 1 == my_number) or (user_guess + 1 == my_number):
        print("so close!!!")
    else:
        print("You lose!!!")
else:
    print("input a positve number")