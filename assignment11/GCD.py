def gcd(b, a):
    if b > a:
       GCD_1 = b
    else:
       GCD_1 = a

    while(True):
        if((b % GCD_1 == 0) and (a % GCD_1 == 0)):
            break
        GCD_1 -= 1\

    return GCD_1

number_1 = int(input("enter your first number 1: "))
number_2 = int(input("enter your second number 2:  "))
print("GCD : ",gcd(number_1, number_2))