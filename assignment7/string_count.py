string = input("enter your sentence: ")
character = input("enter your character: ")
counter = 0

for i in range(len(string)):
    if string[i] == character:
        counter += 1

print(counter)