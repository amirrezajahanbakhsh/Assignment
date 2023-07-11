numbers = []

for i in range(10):
    number = float(input("enter a number: "))
    numbers.append(number)

print(numbers)
numbers_1 = []
c = 0

while c < 10:
    numbers_1.append(numbers[c] + 2)
    c += 1

print(numbers_1)