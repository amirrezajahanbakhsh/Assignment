import random
import pyfiglet

Animals = ["cat", "dog", "cow", "pig", "goat", "fox", "bat", "ant", "wolf", "elephant", "tiger", "bear", "snake", "hog","horse"]
Colors = ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple", "dark blue", "terquoise", "violet"]
fruits = ["banana", "apple", "strawberry", "pineapple", "cherry", "orange", "kiwi", "grape, blueberry", "mango", "peach", "papaya", "water melon"]
Sports = ["soccer", "tennis", "golf", "boxing", "skiing", "pool", "rugby", "karate", "archery", "judo", "basketball", "volleyball"]
Clothes = ["skirt", "cap", "hat", "vest", "scarf", "dress", "boots", "belt", "socks", "jacket", "t-shirt", "shirt", "sport shoes"]

def choose(choose_category, Animals, Colors, fruits, Sports, Clothes):
    if choose_category == 1:    
        return random.choice(Animals)

    elif choose_category == 2:
        return random.choice(Colors)

    elif choose_category == 3:
        return random.choice(fruits)

    elif choose_category == 4:
        return random.choice(Sports)

    elif choose_category == 5:
        return random.choice(Clothes)
    else:
        print("your number is not found please try againe")
        try_again = input("do you want to choose agian?(yes, no)")
        if try_again != "yes":
            return random.choice(Animals)

def create_word(show_word):
    return "".join(show_word)

def create_hearts(hearts):
    return "❤" * int(hearts)

def check(hearts, show_word, word, user_char= "", idx = 0):
    if hearts == 0:
        return "Game over", hearts
    if not("-" in show_word):
        return "YOU WIN!", hearts

    if user_char in word:
        for j in word:
            if user_char == j:
                show_word[word.index(j, idx)] = user_char
            idx += 1  
    else:
        hearts -= 1
        return "your character is not exist", hearts
        
while True:
    result = pyfiglet.figlet_format("Welcome to Hangman game!")  
    print(result) 

    while True:
        choose_category = int(input("1_Animals\n2_Colors\n3_fruits\n4_Sports\n5_Clothes\nenter number of the category: "))
        word = choose(choose_category, Animals, Colors, fruits, Sports, Clothes)
        if word != None:
            break

    hearts = (len(word) * 1.5) // 1
    show_word = []
    number_of_true_char = 0

    for i in range(len(word)):
        show_word.append("-")

    while True:
        print(create_word(show_word))
        print(create_hearts(hearts))
        
        s = check(hearts, show_word, word)
        if s != None:
            if s[0] == "Game over" or s[0] == "YOU WIN!":
                print(s[0])
                break
        
        user_char = input("enter your character : ").lower()
        idx = 0

        s = check(hearts, show_word, word, user_char, idx)
        if s != None:
            hearts = s[1]
            print(s[0])
            
    try_again = input("do you want to try agian?(yes, no)")
    if try_again != "yes":
        break