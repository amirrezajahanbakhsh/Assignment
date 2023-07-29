import math

a = float(input("enter your first number(a)\n"))
b = float(input("enter your second number(b)\n"))
c = float(input("enter your second number(c)\n"))

def Eq(a,b,c):
    if a != 0:
        x = b ** 2 - 4 * a * c
        if x > 0:
            x1 = (-b + math.sqrt(x)) / 2 * a
            x2 = (-b - math.sqrt(x)) / 2 * a
            return(f' The equation has two real roots : \n x1 = {x1} \n x2 = {x2} ')
        elif x == 0:
            x_conj = -b / 2 * a
            return(f' The equation has one conj root : {x_conj}')
        elif x < 0:
            return(' The equation has not root(s) ')
    elif a == 0:
        return(" Coefficient error : 'a' can not be zero, the following equation is linear")

print(Eq(a,b,c))