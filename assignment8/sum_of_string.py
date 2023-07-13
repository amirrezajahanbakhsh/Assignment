string_input = input("enter a sentence: ")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
characters = []
s = 0
for i in numbers:
    for j in string_input:
        if str(i) == j:
            s += i
        else:
            characters.append(j)
print(s)