import random

game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

def show():
    for row in game_board:
        for cell in row:
            if cell=="X":
                print(cell ,end=" ")
            elif cell == "O":
                print(cell ,end=" ")
            else:
                print(cell, end="  ")
        print()

def chek_game(player1_ch, player2_ch):
    for j in range(3):
        if game_board[j][0] == player1_ch and game_board[j][1] == player1_ch and game_board[j][2] == player1_ch or game_board[0][j] == player1_ch and game_board[1][j] == player1_ch and game_board[2][j] == player1_ch or game_board[0][2] == player1_ch and game_board[1][1] == player1_ch and game_board[2][0] == player1_ch or game_board[0][0] == player1_ch and game_board[1][1] == player1_ch and game_board[2][2] == player1_ch:
            print("player 1 win!")
            exit()
        if game_board[j][0] == player2_ch and game_board[j][1] == player2_ch and game_board[j][2] == player2_ch or game_board[0][j] == player2_ch and game_board[1][j] == player2_ch and game_board[2][j] == player2_ch or game_board[0][2] == player2_ch and game_board[1][1] == player2_ch and game_board[2][0] == player2_ch or game_board[0][0] == player2_ch and game_board[1][1] == player2_ch and game_board[2][2] == player2_ch:
            print("player 2 win!")
            exit()

def game():
    player1_ch = "X"
    player2_ch = "O"

    k = 0
    while True:
        if k == 9:
            print("DRAW")
            exit()

        print("player 1")
        while True:
            row = int(input("select the desired row: "))
            column = int(input("select the desired column: "))

            if 1 <= row <= 3 and 1 <= column <= 3: 
                if game_board[row-1][column-1] == "-":
                    k = k + 1
                    game_board[row-1][column-1] = player1_ch
                    break
                else:
                    print("this box is full!")
                    print("try againe!")
            else:
                print("choose in range(0 to 2): ")
        

        if k == 9:
            exit()
        show()
        print("player 2")
        while True:
            row = int(input("select the desired row: "))
            column = int(input("select the desired column: "))

            if 1 <= row <= 3 and 1 <= column <= 3:
                if game_board[row-1][column-1] == "-":
                    k = k + 1
                    game_board[row-1][column-1] = player2_ch
                    break
                else:
                    print("this box is full")
                    print("try againe")
            else:
                print("choose in range(0 , 2)")

        show()
        chek_game(player1_ch, player2_ch)






show()

game()
