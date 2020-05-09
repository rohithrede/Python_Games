import random
    #By Rohith Reddy 
def draw_Board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    Marker = ''
    while not (Marker == 'x' or Marker == 'o'):
        Marker = input("player_1: Choose X or O; ").upper()
        if Marker == 'x':
            return('X','O')
        else:
            return('O','X')

def place_marker(board,Marker,position):
    board[position] = Marker

def win_check(board,Marker):
    return(( board[7] == board[8] == board[9] == Marker) or
    (board[4] == board[5] == board[6] == Marker) or 
    (board[1] == board[2] == board[3] == Marker) or 
    (board[7] == board[4] == board[1] == Marker) or 
    (board[8] == board[5] == board[2] == Marker) or
    (board[9] == board[6] == board[3] == Marker) or
    (board[7] == board[5] == board[2] == Marker) or
    (board[1] == board[5] == board[2] == Marker))

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player_2'
    else:
        return 'Player_1'

def space_check(board,position):
    return board[position] == ' '

def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    choice = int(input("choose a number from 1-9: "))
    if space_check(board,choice):
        return +choice
    else:
        return False

def replay():
    return input('Do you want to play again? Enter Yes or No').upper().startswith('Y')

print("Welcome to Tic Tac Toe!")

while True:
    #reset the board
    Board = [' '] * 10
    player1_Marker , player2_Marker = player_input()
    turn = choose_first()
    print(turn +' will go first')

    play_game = input("Are you ready to play? Enter Yes or No")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player_1':
            #player_1 's turn

            draw_Board(Board)
            position = player_choice(Board)
            place_marker(Board, player1_Marker, position)

            if win_check(Board,player1_Marker):
                draw_Board(Board)
                print('Player 1 won the game!!!')
                game_on = False
            else:
                if full_check(Board):
                    draw_Board(Board)
                    print('The game is draw!!')
                    break
                else:
                    turn ='Player_2'

        else:
            #player_2 's turn

            draw_Board(Board)
            position = player_choice(Board)
            place_marker(Board, player2_Marker, position)

            if win_check(Board, player2_Marker):
                draw_Board(Board)
                print("Player 2 won the game!!!")
                game_on = False
            else:
                if full_check(Board):
                    draw_Board(Board)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player_1'

    if not replay():
        break