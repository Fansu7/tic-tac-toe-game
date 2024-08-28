def create_board():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    return board


def print_board(board):
    print("    1    2    3")
    print("------------------")
    for row in range(len(board)):
        print(f"{row + 1} |", board[row][0], " |", board[row][1], " |", board[row][2], " |")
        print("------------------")


def check_selection(board, row, column):
    #Checking out of range
    if (row > 2) or (column > 2):
        print("Invalid position, select again.")
        return False
    #Checking blank position
    elif board[row][column] != ' ':
        print("Invalid position, select again.")
        return False
    else:
        return True


#Used in the start_game function to change de rows of the board that the program creates at the start of each game.
def change_row(board, row, column, mark):
    board[row][column] = mark


def introduction(board):
    print("Welcome to this Tic Tac Toe game. "
          "Here are the rules: \n"
          "There are 2 players, Player1 ('X') and Player2 ('O')\n"
          f"Each player have 1 turn to put his mark in the board selecting the row and column, the first that get 1 "
          f"full line wins.")
    print_board(board)


#Start the turn count and allow players to select the position they want to mark.
#Each turn it will print the board and check for winners.
def start_game(board):
    turn = 1
    player = ''
    while turn < 10:
        if turn % 2 != 0:
            player = 'X'
        else:
            player = 'O'
        print(f"Player('{player}'), choose row and column:\n")
        row = int(input("Row: ")) - 1
        column = int(input("Column: ")) - 1
        while not check_selection(board, row, column):
            row = int(input("Row: ")) - 1
            column = int(input("Column: ")) - 1
        change_row(board, row, column, player)
        print_board(board)
        turn += 1
        if check_winner(board, player):
            print(f"Player('{player}'), you won!")
            break
    replay(board, player)


# Checks each turn if there's a winner. In case winner == True breaks the while loop in the start_game function a
# finish the current game.
def check_winner(board, player):
    #Check rows
    winner = False
    for r in range(len(board)):
        if board[r][0] == board[r][1] == board[r][2] == player:
            winner = True
    #Check columns
    for c in range(len(board)):
        if board[0][c] == board[1][c] == board[2][c] == player:
            winner = True
    #Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        winner = True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        winner = True
    return winner


def replay(board, player):
    if not check_winner(board, player):
        again = input("There's a tie. Do you want to play again?(Y/N) ").upper()
    else:
        again = input(f"Congratulations player('{player}'). Do you want to play again?(Y/N) ").upper()
    if again == 'Y':
        main()


#Main function, it creates the board, prints the rules and starts the game.
def main():
    board = create_board()
    introduction(board)
    start_game(board)


main()
