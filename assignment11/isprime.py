def isprime(number):
    numbers = []
    for i in range(1, number):
        if (i != 1) and ((number % i) == 0) and(i != number):
            numbers.append(i)
            number_1 = "not prime"
    if len(numbers) == 0:
        number_1 = "prime"

    return number_1
number = int(input("enter your number:\n"))

print("your number is",isprime(number))