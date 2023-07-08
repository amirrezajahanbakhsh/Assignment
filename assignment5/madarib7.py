number = int(input("enter youre number:"))
number1 = number // 7
if number % 7 == 0:
    print(number1 , "is madarib 7")
else:
    print(number , "is not madarib 7")
    number2 = number + 1
    number2 = number * 7
    print("The closest multiple of 7 is close to" , number2)