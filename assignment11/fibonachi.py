def fibonacchi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fibonacchi(n-1) + fibonacchi(n-2)
number = int(input("enter your number(for fibonacchi sequence)\n"))
print(fibonacchi(number))