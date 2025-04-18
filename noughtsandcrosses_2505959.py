import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    This function just draws the current state of the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    pass

def welcome(board):
    """
    This function prints a welcome message and displays the initial layout of the board.
    """
    print("Welcome to the 'Unbetable Noughts and Crosses' game.",)
    print("The board layout is shown below:")
    print("  -------------")
    print("  | 1 | 2 | 3 |")
    print("  -------------")
    print("  | 4 | 5 | 6 |")
    print("  -------------")
    print("  | 7 | 8 | 9 |")
    print("  -------------")
    print("\nWhen prompted, enter the number corresponding to the square you want.\n")
    # prints the welcome message
    # display the board by calling draw_board(board)
    pass

def initialise_board(board):
    """
    This function initializes the game board by setting all cells to empty spaces.
    And it returns a new board with filled spaces.
    """

    return [[' ' for _ in range(3)] for _ in range(3)]

    
def get_player_move(board):
    """
    The function prompts the player to input their move and ensures it is valid.
    and the function returns (row, col) indicating the player's chosen cell.
    """
    while True:
        try:
            print("                             1  2  3")
            print("                             4  5  6")
            move = int(input(f"Enter the cell number (1-9): 7  8  9 : ")) - 1
            if move not in range(9):
                print("Invalid cell number. Choose between 1-9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell is already taken. Try another.")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


def choose_computer_move(board):
    """
    This function randomly chooses a valid cell for the computer's move and returns
    (row, col) indicating the valid chosen cell.
    """
    moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']
    return random.choice(moves)



def check_for_win(board, mark):
    """
    This function checks if a given player or computer has won and it
    returns True if the player has won, False otherwise.
    """
    lines = [
        [board[i] for i in range(3)],
        [[board[i][j] for i in range(3)] for j in range(3)],
        [[board[i][i] for i in range(3)]],
        [[board[i][2 - i] for i in range(3)]]
    ]
    return any(all(cell == mark for cell in line) for group in lines for line in group)


def check_for_draw(board):
    """
    Checks if the game has ended in a draw
    and it returns True if all cells are occupied, False otherwise.
    """
    return all(cell != ' ' for row in board for cell in row)

        
def play_game(board):
    """
    The function manages the flow of the game, alternating between player and computer moves.
    and it returns 1 if the player wins, -1 if the computer wins, and 0 for a draw.
    """
    board = initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        board[row][col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("YOU WIN !")
            return 1
        if check_for_draw(board):
            print("DRAW !")
            return 0

        row, col = choose_computer_move(board)
        board[row][col] = 'O'
        print("Computer's move:")
        draw_board(board)
        if check_for_win(board, 'O'):
            print("YOU LOSE !")
            return -1
        if check_for_draw(board):
            print("DRAW !")
            return 0

                
def menu():
    """
    Displays the game menu and prompts the user for a choice and returns
    the user's choice as a string.
    """
    option=["1","2","3","q"]
    while True:
        print("\nMenu:")
        print("1 - Play the game")
        print("2 - Save score in file 'leaderboard.txt'")
        print("3 - Load and display the scores from 'leaderboard.txt'")
        print("q - Quit the game")
        choice = input("Enter your choice: ").lower()
        if choice in option:
            return choice
            # break
        print("Invalid choice. Please select a valid option.")

def load_scores():
    """
    This function check the path of the leaderboard.txt file and handles the error.
    """
    if os.path.exists('leaderboard.txt'):
        try:
            with open('leaderboard.txt', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Corrupted leaderboard. Starting fresh.")
    return

def save_score(score):
    """
    This function takes the user input and saves the player's name and
     score to 'leaderboard.txt' in json format.
    """

    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = leaders.get(name, 0) + score
    with open('leaderboard.txt', 'w') as file:
        json.dump(leaders, file)
    return

def display_leaderboard(leaders):
    """
    This function displays the leaderboard sorted by scores in
    dictionary with player names as keys and scores as values.
    """
    print(leaders)
    # Print with aligned columns
    data=leaders
    for key, value in data.items():
        print(f"{key}: {value}")
    pass


