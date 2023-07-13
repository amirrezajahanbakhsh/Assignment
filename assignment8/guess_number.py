import random

score_player1 = 0
score_player2 = 0

while True:
    start_game = int(input("1_player1 VS player2\n2_player2 VS player1\nenter your number:  "))
    
    if start_game == 1:
        number = int(input("player1: enter youre number:(range = 0 to 100)"))
        while True:
            input_number = int(input("player2: enter youre number:(range(0 to 100)"))
            if input_number == number :
                print("YOU WIN :)")
                score_player2 += 1
                break
            elif input_number > number:
                print("go down")
            else:
                print("go up")
    
    elif start_game == 2: 
        number = int(input("player2: enter youre number:(range = 0 to 100)"))
        while True:
            input_number = int(input("player1: enter youre number:(range(0 to 100)"))
            if input_number == number:
                print("YOU WIN :)")
                score_player1 += 1
                break
            elif input_number > number:
                print("go down")
            else:
                print("go up")

    else:
        print("your number dosent found")

print("score_player1", score_player1, "score_player2", score_player2,)
