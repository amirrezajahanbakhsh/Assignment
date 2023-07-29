import random

c = int(input("1, 3 or 5 point? "))
player1_s = 0
player2_s = 0
rps = ["rock","paper","scissors"]

def check(player1, player2):
    if player1 == "rock":
        a = {"scissors" : "player1", "paper" : "player2", "rock" : "draw"}
        for j in a:
            if player2 == j:
                return a.get(j)
            
    elif player1 == "paper":
        a = {"scissors" : "player2", "paper" : "draw", "rock" : "player1"}
        for j in a:
            if player2 == j:
                return a.get(j)

    elif player1 == "scissors":
        a = {"scissors" : "draw", "paper" : "player1", "rock" : "player2"}
        for j in a:
            if player2 == j:
                return a.get(j)

while True:
    if player1_s == c or player2_s == c:
        break

    player1 = input("player1 : rock, paper or scissors\n")
    player2 = input("player2 : rock, paper or scissors\n")
    print(f"{player2} !! {player1} \n")
    
    s = check(player1, player2)

    if s == "player1":
        player1_s += 1
        print(f"player1 {player1_s} player2 {player2_s}")
    elif s == "player2":
        player2_s += 1
        print(f"player1 {player1_s} player2 {player2_s}")
    
    if player1_s == c:
        print("Player1 Winer")
    elif player2_s == c:
        print("Player2 Winer")