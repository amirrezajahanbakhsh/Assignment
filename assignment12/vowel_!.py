vowels = character = ['A', 'a', 'I', 'i', 'U', 'u', 'E', 'e', 'O', 'o ']
Sentence = input("Please enter a Sentence: ")

check = [i for i in Sentence]
for i in character:
    for j in check:
        if i == j:
            check[check.index(j)] = "!"

print("".join(check))