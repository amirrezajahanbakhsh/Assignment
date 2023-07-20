import random
from tkinter import W
import pyfiglet

Animals = ["cat", "dog", "cow", "pig", "fly", "goat", "fox", "bat", "ant", "wolf", "elephant", "tiger", "bear", "snake", "hog","horse"]
Colors = ["red", "blue", "black", "white", "green", "orange", "gold", "gray", "coral", "purple", "dark blue", "terquoise", "violet"]
fruits = ["banana", "apple", "strawberry", "pineapple", "cherry", "orange", "kiwi", "grape, blueberry", "mango", "peach", "papaya", "water melon"]
Sports = ["soccer", "tennis", "golf", "boxing", "skiing", "pool", "rugby", "karate", "archery", "judo", "basketball", "volleyball"]
Clothes = ["skirt", "cap", "hat", "vest", "scarf", "dress", "boots", "belt", "socks", "jacket", "t-shirt", "shirt", "sport shoes"]
while True:
    result = pyfiglet.figlet_format("Welcome to Hangman game!")  
    print(result) 
    while True:
        choose_category = int(input("1_Animals\n2_Colors\n3_fruits\n4_Sports\n5_Clothes\nenter number of the category: "))
        if choose_category == 1:    
            word = random.choice(Animals)
            break

        elif choose_category == 2:
            word = random.choice(Colors)
            break

        elif choose_category == 3:
            word = random.choice(fruits)
            break

        elif choose_category == 4:
            word = random.choice(Sports)
            break

        elif choose_category == 5:
            word = random.choice(Clothes)
            break
        else:
            print("your number is not found please try againe")
            try_again = input("do you want to choose agian?(yes, no)")
            if try_again != "yes":
                word = random.choice(Animals)
                break
    hearts = (len(word) * 1.5) // 1
    show_word = []
    number_of_true_char = 0
    for i in range(len(word)):
        show_word.append("_")
    while True:
        print("".join(show_word))
        print("❤" * int(hearts))
        if hearts == 0:
            print("Game over")
            break
        
        if not("_" in show_word):
            print("Hip Hip Hoorey!")
            break
        user_char = input("enter your character : ").lower()
        idx = 0
        if user_char in word:
            for j in word:
                if user_char == j:
                    show_word[word.index(j, idx)] = user_char
                idx += 1  
        else:
            print("your character is not exist")
            hearts -= 1
    try_again = input("do you want to try agian?(yes, no)")
    if try_again != "yes":
        break