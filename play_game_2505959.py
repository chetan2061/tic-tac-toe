#You will have to import your other module in this module
from noughtsandcrosses_2505959 import *

    
def main():
    """
        The main function first initializes the game board and displays a welcome message than Provides
        a menu with option for user choice. Overall it controls the flow of the program and other function calls inside it.
        """


    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]
    # draw_board(board)
    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye !!!')
            return


    
# Program execution begins here
if __name__ == '__main__':
    main()
