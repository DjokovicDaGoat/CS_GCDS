import random
import time

"""
Name: Joaquin Urrutia
Description: tic tace toe game for 3x3 and 5x5(s)
Bugs: None known
Date: 9/27/2026
Bonuses:board size, score tracker, 
Log: Initial version: 10/10/2026
     10/27/2026 Updated to include a menu and character search functionality
"""
def color_text(text, color_name):
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m',
    }

    color_code = colors.get(color_name.lower(), '\033[37m')
    return f"{color_code}{text}\033[0m"


def print_colored_text(text, color):
    print(color_text(text, color))


def input_colored_text(text, color):
    return input(color_text(text, color))

def get_player_info():
    '''
    Gets the name of players and saves it

        Args:
            none

        Returns:
            the name of player1 and player2
    '''
    player1 = input("What is your name?: ")
    print(f"OK so you are {player1}")
    player2 = input("What is your name?: ")
    print(f"OK so your are {player2}")
    return player1, player2

def get_players_play_order(player1, player2):
    '''
    Randomly chooses a player to go first. Also asks the player who is going first what symbol (X, or O) and returns it

        Args:
            player1(string)
            player2(string)

        Returns:
            the order of player between player1 and player2
            the symbol for both players in accoradance to order
    '''
    first = random.choice([player1, player2])
    print("Choosing who is going first.")
    time.sleep(2)
    print("AND...")
    time.sleep(1)
    print("--------")
    print(first, "will go first.")
    time.sleep(1)
    symbol = input(first + ", do you want to be X or O?: ").upper()

    while symbol != "X" and symbol != "O":
        symbol = input("Choose X or O: ").upper()

    return first, symbol


def tik_tac_toe_board(board):
    '''
    Displays tik take toe board with rown and clumn numbers to help user make their move

        Args
            board(list)

    Allows user to see that all the spaces in the board are currently open with "-"
    '''
    print("    1   2    3")
    print("1", "|", board[0][0], "|", board[0][1], "|", board[0][2], "|")
    print("   -------------")
    print("2", "|", board[1][0], "|", board[1][1], "|", board[1][2], "|")
    print("   ------------")
    print("3", "|", board[2][0], "|", board[2][1], "|", board[2][2], "|")


def get_player_move(board, player):
    '''
    Gets player move depending on the order of play taken from get get_players_play_order().

        Args:
            board(list)
            player(str)

    Returns moves so that the check winner function can check if the inputed move causes a win, and the ceck_draw function checks for draw.

    '''
    while True:
        print("Now it's your turn, Player", player)

        try:
            row = int(input("Enter Row (1-3): ")) - 1
            column = int(input("Enter Column (1-3): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if row not in range(3) or column not in range(3):
            print("Please enter numbers between 1 and 3.")
        elif board[row][column] == "-":
            board[row][column] = player
            break
        else:
            print("That square is already taken. Try again.")


def check_winner(board, player):
    '''
    Checks all the possible ways a player can win. This function is used every turn untill there actually is a winner
        Args:
            board(list)
            player(str)

    Returns the result dpending on which player won.
    '''
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    elif board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    else:
        return False


def check_draw(board):
    '''
    checks if the board displays a draw, meaning no ones wins.

        Args:
            board(list)
    Checks if the board has a draw, meaning that no one one and that no points are added to the scoreboard function

    '''
    if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        return True
    else:
        return False


def display_scoreboard(player1, player1_score, player2, player2_score):
    '''
    Displays scoreboard of both players on total wins

        Args:
            player1(str)
            player1_score
            player2
            player2_score
    '''
    print("------ SCOREBOARD ------")
    print(f"{player1}: {player1_score}")
    print(f"{player2}: {player2_score}")
    print("------------------------")
    return player1, player1_score, player2, player2_score


def play_again():
    '''
    Prompts the user of they want to play again a 3x3 tic tac toe.

        Args:
            none

    if true return
    if false return
    This will determine whether the game repeats or if the next prompt will be displayed
    '''

    while True:
        choice = input_colored_text("Would you like to play again? (yes/no): ", "cyan").lower().strip()

        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            print_colored_text("Thanks for playing Tic-Tac-Toe!" , "green")
            return False
        else:
            print("Please enter yes or no.")


def get_player_decisons(othergame):
    '''
    Prompts the user whether they want to play 5x5 version of tic tac toe

        Args:
            othergame(str)

    Returns if user tyes yes or no or any variation of them. This will decide if the next game is played or if the program ends.
    '''
    while True:
        othergame = input_colored_text("Would you like to play 5x5 Tic-Tac-Toe? (yes/no): ","cyan" ).lower().strip()

        if othergame in ["yes", "y"]:
            break
        elif othergame in ["no", "n"]:
            print_colored_text("Thanks for playing Tic-Tac-Toe!", "green")
            return
        else:
            print("Please type yes or no!")


def five_by_five_tic_tac_toe_board(board_2):
    '''
    Displays tik take toe board with rown and clumn numbers to help user make their move

        Args
            board(list)

    Allows user to see that all the spaces in the board are currently open if space is "-"
    '''

    print("    1   2    3    4   5")
    print("1", "|", board_2[0][0], "|", board_2[0][1], "|",  board_2[0][2], "|",board_2[0][3],"|", board_2[0][4], "|")
    print("   -------------------")
    print("2", "|", board_2[1][0], "|", board_2[1][1], "|", board_2[1][2], "|", board_2[1][3],"|", board_2[1][4], "|")
    print("   -------------------")
    print("3", "|", board_2[2][0], "|", board_2[2][1], "|", board_2[2][2], "|", board_2[2][3],"|", board_2[2][4], "|")
    print("   -------------------")
    print("4", "|", board_2[3][0], "|", board_2[3][1], "|", board_2[3][2], "|", board_2[3][3],"|", board_2[3][4], "|")
    print("   -------------------")
    print("5", "|", board_2[4][0], "|", board_2[4][1], "|", board_2[4][2], "|", board_2[4][3],"|", board_2[4][4], "|")


def get_player_move_5x5(board_2, player):
    '''
    Gets the move of the first player for the 5x5.

        Args:
            board_2(list)
            player(str)

    retruns the move and adds it to the board
    '''
    while True:
        print("Now it's your turn, Player", player)

        try:
            row = int(input("Enter Row (1-5): ")) - 1
            column = int(input("Enter Column (1-5): ")) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if row not in range(5) or column not in range(5):
            print("Please enter numbers between 1 and 5.")
        elif board_2[row][column] == "-":
            board_2[row][column] = player
            break
        else:
            print("That square is already taken. Try again.")


def check_winner_5x5(board_2, player):
    '''
    Checks winner for 5x5 board specifically every move

        Args
            board_2(list)
            player(str)

    Returns if a player makes a winning move and returns to scoreboard function
    '''
    if board_2[0][0] == player and board_2[0][1] == player and board_2[0][2] == player and board_2[0][3] == player and board_2[0][4] == player:
        return True
    elif board_2[1][0] == player and board_2[1][1] == player and board_2[1][2] == player and board_2[1][3] == player and board_2[1][4] == player:
        return True
    elif board_2[2][0] == player and board_2[2][1] == player and board_2[2][2] == player and board_2[2][3] == player and board_2[2][4] == player:
        return True
    elif board_2[3][0] == player and board_2[3][1] == player and board_2[3][2] == player and board_2[3][3] == player and board_2[3][4] == player:
        return True
    elif board_2[4][0] == player and board_2[4][1] == player and board_2[4][2] == player and board_2[4][3] == player and board_2[4][4] == player:
        return True

    elif board_2[0][0] == player and board_2[1][0] == player and board_2[2][0] == player and board_2[3][0] == player and board_2[4][0] == player:
        return True
    elif board_2[0][1] == player and board_2[1][1] == player and board_2[2][1] == player and board_2[3][1] == player and board_2[4][1] == player:
        return True
    elif board_2[0][2] == player and board_2[1][2] == player and board_2[2][2] == player and board_2[3][2] == player and board_2[4][2] == player:
        return True
    elif board_2[0][3] == player and board_2[1][3] == player and board_2[2][3] == player and board_2[3][3] == player and board_2[4][3] == player:
        return True
    elif board_2[0][4] == player and board_2[1][4] == player and board_2[2][4] == player and board_2[3][4] == player and board_2[4][4] == player:
        return True

    elif board_2[0][0] == player and board_2[1][1] == player and board_2[2][2] == player and board_2[3][3] == player and board_2[4][4] == player:
        return True
    elif board_2[0][4] == player and board_2[1][3] == player and board_2[2][2] == player and board_2[3][1] == player and board_2[4][0] == player:
        return True

    else:
        return False


def main():
    '''
    Organizes varibles and functions to create an organize order for the tic tac toe functions to be ran

        Args:
            none

    Returns the user inputs from the functions
    '''
    player1_score = 0
    player2_score = 0

    player1, player2 = get_player_info()

    while True:

        first, symbol = get_players_play_order(player1, player2)

        player1_symbol = symbol if first == player1 else ("O" if symbol == "X" else "X")
        player2_symbol = "O" if player1_symbol == "X" else "X"

        board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ]

        current_player = first
        player = player1_symbol if current_player == player1 else player2_symbol

        while True:
            tik_tac_toe_board(board)
            get_player_move(board, player)

            if check_winner(board, player):
                tik_tac_toe_board(board)
                print_colored_text(current_player + " wins!", "green")

                if current_player == player1:
                    player1_score += 1
                else:
                    player2_score += 1

                break

            if check_draw(board):
                tik_tac_toe_board(board)
                print_colored_text("It's a tie!", "yellow")
                break

            if current_player == player1:
                current_player = player2
                player = player2_symbol
            else:
                current_player = player1
                player = player1_symbol

        display_scoreboard(player1, player1_score, player2, player2_score)

        if play_again():
            continue

        while True:
            othergame = input_colored_text("Would you like to play 5x5 Tic-Tac-Toe? (yes/no): ","cyan" ).lower().strip()

            if othergame in ["yes", "y"]:
                break
            elif othergame in ["no", "n"]:
                print_colored_text("Thanks for playing Tic-Tac-Toe!", "green")
                return
            else:
                print("Please type yes or no!")

        board_2 = [
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-"]
        ]

        current_player = first
        player = player1_symbol if current_player == player1 else player2_symbol

        while True:
            five_by_five_tic_tac_toe_board(board_2)
            get_player_move_5x5(board_2, player)

            if check_winner_5x5(board_2, player):
                five_by_five_tic_tac_toe_board(board_2)
                print_colored_text(current_player + " wins!", "green")

                if current_player == player1:
                    player1_score += 1
                else:
                    player2_score += 1

                break

            if check_draw(board_2):
                five_by_five_tic_tac_toe_board(board_2)
                print_colored_text("It's a tie!", "yellow")
                break

            if current_player == player1:
                current_player = player2
                player = player2_symbol
            else:
                current_player = player1
                player = player1_symbol

        display_scoreboard(player1, player1_score, player2, player2_score)

        if not play_again():
            print_colored_text("Thanks for playing Tic-Tac-Toe!", "green")
            break


main()