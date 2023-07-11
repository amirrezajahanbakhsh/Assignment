import math
x = 0
while True:
    print("""select the desired operation
    1 +
    2 - 
    3 *
    4 / 
    5 **
    6 sqr
    7 fac
    8 round
    9 tan 
    10 sin
    11 cos
    12 cot
    13 log
    14 abs
    15 exit""")

    x = int(input("choose your oparation: "))

    if x == 15:
        print("Good bye:)")
        exit(0)

    if 1 <= x <= 5:
        first_number = float(input("enter your first number: "))
        second_number = float(input("enter your second number: "))
        if x == 1:
            result = first_number + second_number   
        elif x == 2:
            result = first_number - second_number
        elif x == 3:
            result = first_number * second_number
        elif x == 4:
            if second_number != 0:
                result = first_number / second_number 
            else:
                print("error") 
        else:
            result = first_number ** second_number

    elif 6 <= x <= 14:
        num = float(input("enter your number: "))
        if x == 6:
            result = math.sqrt(num)
        elif x == 7:
            result = math.factorial(num)
        elif x == 8:
            result = round(num)
        elif x == 9:
            result = math.tan(num)
        elif x == 10:
            result = math.sin(num)
        elif x == 11:
            result = math.cos(num)
        elif x == 12:
            result = math.cos(num) / math.sin(num)
    
        elif x == 13:
            result = math.log(num)
        else:
            result = abs(num)
    else:
        print("i can not find")

    print(result)
    
   
   