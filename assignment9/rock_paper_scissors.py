import random
import pyfiglet

title = pyfiglet.figlet_format("rock  paper  scissors", font="banner3-d")
print(title)

a = int(input("1 = player_1 VS computer \n2 = player_1 VS player_2 \nChoose Your Gamemode"))
c = int(input("1 point or 3 point or 5 point? "))
computer_s = 0
player_1 = 0
player_2 = 0
rps = ["rock","paper","scissors"]

if a == 1:
    while True:
        if computer_s == c or player_1 == c:
            break

        computer = random.choice(rps)
        player1 = input("rock or paper or scissors \t")
        print(f"computer : {computer} and player1 : {player1} \n")
        

        if player1 == "rock":
            a = {"scissors" : "player1", "paper" : "computer", "rock" : "draw"}
            for j in a:
                if computer == j:
                    b = a.get(j)
                
        elif player1 == "paper":
            a = {"scissors" : "computer", "paper" : "draw", "rock" : "player1"}
            for j in a:
                if computer == j:
                    b = a.get(j)

        elif player1 == "scissors":
            a = {"scissors" : "draw", "paper" : "player1", "rock" : "computer"}
            for j in a:
                if computer == j:
                    b = a.get(j)

        if b == "player1":
            player_1 += 1
            print("Plyer Win")
        elif b == "computer":
            computer_s += 1
            print("Computer Win")
        else:
            print("Draw")

        print(f"player1 : {player_1} and computer : {computer_s}")

elif a == 2:
    while True:
        if player_1 == c or player_2 == c:
            break

        player1 = input("player1 : rock or paper or scissors \t")
        player2 = input("player2 : rock or paper or scissors \t")
        print(f"player2 : {player2} and player1 : {player1} \n")
        
        if player1 == "rock":
            a = {"scissors" : "player1", "paper" : "player2", "rock" : "draw"}
            for j in a:
                if player2 == j:
                    b = a.get(j)
                
        elif player1 == "paper":
            a = {"scissors" : "player2", "paper" : "draw", "rock" : "player1"}
            for j in a:
                if player2 == j:
                    b = a.get(j)

        elif player1 == "scissors":
            a = {"scissors" : "draw", "paper" : "player1", "rock" : "player2"}
            for j in a:
                if player2 == j:
                    b = a.get(j)

        if b == "player1":
            player_1 += 1
            print("Player1 Win!!")
        elif b == "player2":
            player_2 += 1
            print("Player2 Win")
        else:
            print("Draw")

        print(f"player1 : {player_1} and player2 : {computer_s}")