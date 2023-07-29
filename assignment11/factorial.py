def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n - 1) * n

number = int(input("enter your numebr: "))
print(factorial(number))