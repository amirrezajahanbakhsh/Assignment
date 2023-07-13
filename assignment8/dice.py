import random
number = 0
list_numbers = []
counter = 0

while not (number == 6):
    list_numbers.append(number)
    number = random.randint(1, 6)
    counter += 1
    if number == 6:
        print(f"round {counter} YOU WIN :)")
    else:
        print(f"round {counter} is: ", number)
        
print("total numbers of previous rounds: ", sum(list_numbers))
print("sum of whole numbers", sum(list_numbers) + 6 )

    
