import os


board = [" " for _ in range(9)]     # Initialization of an array of size 9


def board_print(board, player, winner):
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i+1] + " | " + board[i+2]  + " ")
        if i >= 6:
            print()
            continue
        print("---+---+---")
    
    if winner:
        print(f"* Game end : Player {player} wins! *")


def is_winner(board):
    if board[0] == board[1] == board[2] != " " or \
        board[3] == board[4] == board[5] != " " or \
        board[6] == board[7] == board[8] != " " or \
        board[0] == board[3] == board[6] != " " or \
        board[1] == board[4] == board[7] != " " or \
        board[2] == board[5] == board[8] != " " or \
        board[0] == board[4] == board[8] != " " or \
        board[2] == board[4] == board[6] != " " :
        return True
    else:
        return False


def morpion():
    player = "X"
    turn = 0

    while turn < 9:
        winner = False
        turn +=1

        os.system("clear")
        board_print(board, player, winner)
    
        print(f"> Turn of player {player}\n(Select a number between 1 and 9.)")
        move = input("> input: ") 
        
        while not move.isdigit() or int(move) not in [1, 2, 3, 4, 5, 6, 7, 8, 9] :
            move = input("> Correct your input: ")
        
        move = int(move) - 1

        if board[move] != " ":
            print("! You can't make this move")
            input("Press enter to continue...")
            continue


        board[move] = player

        if turn >= 5 :
            if is_winner(board):
                winner = True
                board_print(board, player, winner)
                break

            else:
                winner = False
        
        if not winner:
            player = "O" if player == "X" else "X"


morpion()
