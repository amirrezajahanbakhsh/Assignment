numbers = input("enter your numbers: ")

dict_for_number = {}

for number in numbers:
    if number in dict_for_number:
        dict_for_number[number] += 1
    else:
        dict_for_number[number] = 1

print(dict_for_number)