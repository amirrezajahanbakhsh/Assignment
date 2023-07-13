import random

score_player1 = 0
score_player2 = 0
score_computer = 0

while True:
    start_game = int(input("1_player1 VS computer\n2_computer VS player1\nenter your number:  "))
    
    if start_game == 1:
        number = int(input("player1: enter youre number:(range = 0 to 100 "))
        the_highest_number = 100
        the_lowest_number = 0
        input_number = random.randint(the_lowest_number, the_highest_number)
        while True:
            if input_number == number:
                print(f"computer number is: {input_number}", "COMPUTER WIN :)")
                score_computer += 1
                print("score_player1", score_player1, "score_computer", score_computer)
                break
            elif input_number > number:
                print(f"computer number is:{input_number}", "go down")
                the_highest_number = input_number
                input_number = random.randint(the_lowest_number, the_highest_number)
            else:
                print(f"computer number is:{input_number}", "go up!")
                the_lowest_number = input_number
                input_number = random.randint(the_lowest_number, the_highest_number)
    
    elif start_game == 2: 
        number = random.randint(0, 100)
        while True:
            input_number = int(input("enter youre number:"))
            if input_number == number :
                print("YOU WIN :)")
                score_player1 += 1
                print("score_player1", score_player1, "score_computer", score_computer)
                break
            elif input_number > number:
                print("go down")
            else:
                print("go up")
    
    else:
        print("your number dosent found")
