
from random import randrange
import time


def init_board():
    # Initializes the board as a 3x3 array with numbers 1-9 to represent the squares
    global board
    board = [[" " for row in range(3)] for col in range(3)]
    num = 0
    for row in range(3):
        for col in range(3):
            num += 1
            board[row][col] = num


def display_board(board):
    # Takes the board in its current state and displays it in a user-friendly format
    for row in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|  ", board[row][0], "  |  ", board[row][1], "  |  ", board[row][2], "  |")
        print("|       |       |       |")
    else:
        print("+-------+-------+-------+")
        time.sleep(1)


def enter_move(board):
    # Accepts the user's move, checks if it's valid, and updates the board accordingly.
    user_move = int(input("\nIt's your turn. \nWhat's your next move? (1-9): "))
    if user_move < 1 or user_move > 9 or type(user_move) is not int:
        print("Invalid input. Please enter a number between 1 and 9.")
        return enter_move(board)
    elif user_move not in [board[row][col] for row in range(3) for col in range(3)]:
        print("Oops, that's taken. Please choose another square.")
        return enter_move(board)
    else:
        for row in range(3):
            for col in range(3):
                if board[row][col] == user_move:
                    board[row][col] = 'O'
                    print("\nYou chose square", user_move, "\nHere's the board now:")
                    break
    return display_board(board)
  

def make_list_of_free_fields(board):
    # The function scans the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in range(3):
        for col in range(3):
            if type(board[row][col]) is int:
                free_fields.append((row, col))
    return free_fields


def computer_move(board):
    # The function draws the computer's move and updates the board.
    if board[1][1] != 'X':
        board[1][1] = 'X'
        print("\nComputer has made its move.\nHere's the board now:")
        display_board(board)
        return
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'
        print("\nComputer has made its move.\nHere's the board now:")
        display_board(board)    
    else:
        return False

    
def victory_for(board, sign):
    """
    Pass 'O' or 'X' as 'sign' argument. The function analyzes the board's status in order to check if
    the player using 'O's or 'X's has won the game.  
    """
    # Conditions for victory:
    #   if row n contains sign in cols 0,1,2
    #   if col n contains sign in rows 0,1,2
    #   diagonal_a, row 0 col 0, row 1 col 1, row 2 col 2
    #   diagonal_b, row 2 col 0, row 1 col 1, row 0 col 2
    for row in range(3):
        if all(board[row][col] == sign for col in range(3)):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True   
    # diagonal_a
    if all(board[row][col] == sign for row, col in [(0, 0), (1, 1), (2, 2)]): 
        return True
    # diagonal_b
    if all(board[row][col] == sign for row, col in [(2, 0), (1, 1), (0, 2)]): 
        return True
    else:
        return False


def tie_game(board):
    # The function checks if the game is a tie.
    free_fields = make_list_of_free_fields(board)
    if not free_fields:
        return True
    return False


def any_winner(board):
    if victory_for(board, 'O'):
        return "Congratulations! You win!"
    elif victory_for(board, 'X'):
        return "Computer wins! Better luck next time."
    elif tie_game(board):
        return "It's a tie!\n"
    else:
        return False


def start_game():
    print("Here's the game board.")
    time.sleep(1)
    display_board(board)
    print("\nThe computer will play with X's and make the first move.")
    time.sleep(1)
    print("Your moves will be represented by O's.")
    time.sleep(1)
    print("Here comes the computer's first move:\n")
    time.sleep(1)


def play_again():
    # Asks the user if they want to play again and either restarts the game or exits.
    again = input("\nWould you like to play again? (y/n): ")
    if again.lower() == 'y':
        init_board()
        start_game()
        play(board)
    else:
        print("\nThanks for playing! Goodbye!")


def play(board):
    # The main game loop that alternates between the computer and the user until there's a winner or a tie.
    while any_winner(board) == False:
        computer_move(board)
        if any_winner(board) != False:
            print(any_winner(board))
            break
        enter_move(board)
        if any_winner(board) != False:
            print(any_winner(board))
            break
    return play_again()


# First time initialization of the board and starting the game
print("""
Welcome to Tic-Tac-Toe!

X--O--X
O--X--O
X--O--X

Let's Begin!\n
""")
time.sleep(2)
init_board()
start_game()
play(board)

