numbers = []
number1 = float(input("enter your number: "))
numbers.append(number1)

number2 = float(input("enter your number: "))
numbers.append(number2)

number3 = float(input("enter your number: "))
numbers.append(number3)

number4 = float(input("enter your number: "))
numbers.append(number4)

number5 = float(input("enter your number: "))
numbers.append(number5)

print(sorted(numbers))
print(sorted(numbers, reverse=True))