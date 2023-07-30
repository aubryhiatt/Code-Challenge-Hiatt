import random

game_board = [['.','.','.'], ['.','.','.'], ['.','.','.']]

def start_game(game_board):
    print("Rules of Tic-Tac-Toe:")
    print("You can only pick an empty spot, which will look like '.'")
    print("Three in a row means you win")
    print("The top left corner is 0,0: so comment your 'row,collum' on your turn to make a move.")
    display(game_board)
    output = input("Would you like to go first? Y/N ")
    if output == 'Y':
        player_turn(game_board)
    if output == 'y':
        player_turn(game_board)
    if output == 'N':
        computer_turn(game_board)
    if output == 'n':
        computer_turn(game_board)

def display(g_b):
    print(g_b[0][0], g_b[0][1], g_b[0][2])
    print(g_b[1][0], g_b[1][1], g_b[1][2])
    print(g_b[2][0], g_b[2][1], g_b[2][2])

def check_output(gb, row, col):
    if gb[int(row)][int(col)] != '.':
        return False
    return True

def won_game(gb):
    for i in range(3):
        if gb[i][0] == 'X':
            if gb[i][1] == 'X':
                if gb[i][2] == 'X':
                    print('Great Job! You won the game!')
                    output = input("Would you like to play again? Y/N ")
                    if output == 'Y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    if output == 'y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    exit()
    for i in range(3):
        if gb[0][i] == 'X':
            if gb[1][i] == 'X':
                if gb[2][i] == 'X':
                    print('Great Job! You won the game!')
                    output = input("Would you like to play again? Y/N ")
                    if output == 'Y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    if output == 'y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    exit()
    for i in range(3):
        if gb[i][0] == 'O':
            if gb[i][1] == 'O':
                if gb[i][2] == 'O':
                    print('You lost this one, good luck next time!')
                    output = input("Would you like to play again? Y/N ")
                    if output == 'Y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    if output == 'y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    exit()
    for i in range(3):
        if gb[0][i] == 'O':
            if gb[1][i] == 'O':
                if gb[2][i] == 'O':
                    print('You lost this one, good luck next time!')
                    output = input("Would you like to play again? Y/N ")
                    if output == 'Y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    if output == 'y':
                        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                    exit()
    if gb[0][0] == 'X':
        if gb[1][1] == 'X':
            if gb[2][2] == 'X':
                print('Great Job! You won the game!')
                output = input("Would you like to play again? Y/N ")
                if output == 'Y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                if output == 'y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                exit()
    if gb[0][0] == 'O':
        if gb[1][1] == 'O':
            if gb[2][2] == 'O':
                print('You lost this one, good luck next time!')
                output = input("Would you like to play again? Y/N ")
                if output == 'Y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                if output == 'y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                exit()
    if gb[0][2] == 'X':
        if gb[1][1] == 'X':
            if gb[2][0] == 'X':
                print('Great Job! You won the game!')
                output = input("Would you like to play again? Y/N ")
                if output == 'Y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                if output == 'y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                exit()
    if gb[0][2] == 'O':
        if gb[1][1] == 'O':
            if gb[2][0] == 'O':
                print('You lost this one, good luck next time!')
                output = input("Would you like to play again? Y/N ")
                if output == 'Y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                if output == 'y':
                    start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
                exit()

def tie_game(gb):
    for i in range(3):
        for u in range(3):
            if gb[i][u] == '.':
                return
    print("Tie Game. Not bad!")
    output = input("Would you like to play again? Y/N ")
    if output == 'Y':
        start_game([['.','.','.'], ['.','.','.'], ['.','.','.']])
    if output == 'y':
        start_game([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
    exit()

def invalid(output):
    if output[0] != '0':
        if output[0] != '1':
            if output[0] != '2':
                print("Your answer must be formatted 'row','collum' (ex: 0,2)")
                return False
    if output[1] != ',':
        print("Your answer must be formatted 'row','collum' (ex: 0,2)")
        return False
    if output[2] != '0':
        if output[2] != '1':
            if output[2] != '2':
                print("Your answer must be formatted 'row','collum' (ex: 0,2)")
                return False
    if len(output) != 3:
        print("Your answer must be formatted 'row','collum' (ex: 0,2)")
        return False
    return True

def player_turn(game_board):
    output = input("Where would you like to go? ")
    if invalid(output) is False:
        display(game_board)
        player_turn(game_board)
    row, col = output[0], output[2]
    if check_output(game_board, row, col) is True:
        game_board[int(row)][int(col)] = 'X'
        display(game_board)
        won_game(game_board)
        tie_game(game_board)
        computer_turn(game_board)
    print("You can only pick empty spots. Try again.")
    player_turn(game_board)

def get_coordinate(game_board):
    row = random.randrange(3)
    col = random.randrange(3)
    if check_output(game_board, row, col) is True:
        return row, col
    for i in range(3):
        for u in range(3):
            if check_output(game_board, i, u) is True:
                return i, u

def computer_turn(game_board):
    print("Opponent takes turn.")
    row, col = get_coordinate(game_board)
    game_board[int(row)][int(col)] = 'O'
    display(game_board)
    won_game(game_board)
    tie_game(game_board)
    player_turn(game_board)

start_game(game_board)
