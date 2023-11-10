import os
new_line = '\n------------------------------\n'

def isGameFinished(board):
    # Win?
    for i in range(3):
        if (board[i][0]==board[i][1]) and (board[i][0]==board[i][2]) and (board[i][0] != " "):
            return(board[i][0])
        elif (board[0][i]==board[1][i]) and (board[0][i]==board[2][i]) and (board[0][i] != " "):
            return(board[0][i])

    if (board[0][0]==board[1][1]) and (board[0][0]==board[2][2]) and (board[1][1] != " "):
        return(board[1][1])
    elif (board[0][2]==board[1][1]) and (board[2][0]==board[1][1]) and (board[1][1] != " "):
        return(board[1][1])

    # Finish?
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return 0
    # Tie
    return 3



def isValidMove(board,x,y):
    # isValidMove(board,0,1)
    try:
        if board[x][y] == " ":
            return True
        return False
    except:
        return False



def newGameBoard():
    board = [[" "," "," "],
             [" "," "," "],
             [" "," "," "]]
    return board



def printBoard(board):
    print("     | y 0 | y 1 | y 2 |\n-----┼-----┼-----┼-----┼\n x 0 |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |\n-----┼-----┼-----┼-----┼\n x 1 |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |\n-----┼-----┼-----┼-----┼\n x 2 |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |\n-----┼-----┼-----┼-----┼".format(board = board))

"""
Demo
     | y 0 | y 1 | y 2 |
-----┼-----┼-----┼-----┼
 x 0 |  X  |  O  |  △  |
-----┼-----┼-----┼-----┼
 x 1 |  □  |     |  □  |
-----┼-----┼-----┼-----┼
 x 2 |  △  |  O  |  X  |
-----┼-----┼-----┼-----┼
"""



def TTT():
    win = 0
    pointer = 1
    symbol = "XO△□"
    board = newGameBoard()

    print(new_line)
    print("Please choose a symbol you like from following:\nX\t| O\t| △\t| □")
    player_1 = input("Player 1: ")
    while player_1 not in symbol:
        print("Invalid input! Try again!")
        player_1 = input("Player 1: ")
    player_2 = input("Player 2: ")
    while (player_2 not in symbol) or (player_2 == player_1):
        print("Invalid input! Try again!")
        player_2 = input("Player 2: ")
    
    # One move
    while win == 0:
        status = False
        print(new_line)
        printBoard(board)
        while not status:
            if pointer == 1:
                message = str("Player 1 ({}):".format(player_1))
            elif pointer == 2:
                message = str("Player 2 ({}):".format(player_2))
            choice = input(message)

            try:
                x = int(choice[1:2])
                y = int(choice[3:4])
                status = isValidMove(board,x,y)
                if not status:
                    print("Invalid move! Please try again!")
            except:
                print("Invalid input! Please try again!")
        
        # Save progress
        if pointer == 1:
            board[x][y] = player_1
        elif pointer == 2:
            board[x][y] = player_2
        
        # Switch turn
        pointer -= 1
        if pointer == 0:
            pointer = 2

        # Win tie or unfinish
        win = isGameFinished(board)
    
    # Display winner or tie
    print(new_line)
    printBoard(board)
    if win == 3:
        print("Tie!")
    elif win == player_1:
        print("Player 1 WIN!")
    elif win == player_2:
        print("Player 2 WIN!")


        
def menu():
    print(new_line)
    print("This is a Python program for Tic Tac Toe")
    print("Enter 1 to start")
    print("Enter 999 to exit")
    choice = input()
    if choice == "1":
        TTT()
    elif choice == "999":
        exit()
    else:
        print("Invalid input! Please try again!")

    menu()
        


menu()