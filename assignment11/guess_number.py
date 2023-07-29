def check(number, number_u):
    if number > number_u:
        return "up"
        
    elif number < number_u:
        return "down"
    
    elif number == number_u:
        return "win"

def game():
    number = int(input("enter a number: "))
    while True:
        a = check(number,int(input("Guess a number: ")))
        print(a)
        if a == "win":
            break

game()