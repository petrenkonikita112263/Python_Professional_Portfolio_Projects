from random import random
from typing import Tuple

from tic_tac import TicTacToeGame

game_board = [" "] * 10
tic_tac_toe = TicTacToeGame(game_board)


def player_input_marker() -> Tuple[str, str]:
    """Function that takes in a player input and assign their marker as 'X' or 'O'
    asks in while loop"""
    marker = ""
    while not (marker == "X" or marker == "O"):
        marker = input("Player 1: What do you choose 'X' or 'O'? ").upper()
    if marker == "X":
        return "X", "O"
    else:
        return "O", "X"


def choose_first() -> str:
    """Return which player will be first move"""
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def player_input_choice() -> int:
    """Function that takes the player input as the position for his|her marker"""
    marker_position = 0
    while marker_position not in range(1, 10) or not tic_tac_toe.check_the_cell(marker_position):
        marker_position = int(input("Choose the position for your marker from 1 to 9: "))
    return marker_position


def re_run_game() -> bool:
    """Function that asks for new game or stops playing"""
    return input("Would you like to play another game 'Y' or 'N'? ").lower().startswith("y")


while True:
    player1_figure, player2_figure = player_input_marker()
    player_turn = choose_first()
    print(f"{player_turn} makes first move")
    play_game = input("Do you want to play the game? 'Y' or 'N' ").lower()
    if play_game == "y":
        game_on = True
    else:
        game_on = False
    while game_on:
        if player_turn == "Player 1":
            tic_tac_toe.display_board()
            position = player_input_choice()
            tic_tac_toe.place_marker(player1_figure, position)
            if tic_tac_toe.have_winning_position(player1_figure):
                tic_tac_toe.display_board()
                print("Player 1 have won the game")
                game_on = False
            else:
                if tic_tac_toe.check_the_board():
                    tic_tac_toe.display_board()
                    print("Win the draw")
                    break
                else:
                    player_turn = "Player 2"
        else:
            tic_tac_toe.display_board()
            position = player_input_choice()
            tic_tac_toe.place_marker(player2_figure, position)
            if tic_tac_toe.have_winning_position(player2_figure):
                tic_tac_toe.display_board()
                print("Player 2 have won the game")
                game_on = False
            else:
                if tic_tac_toe.check_the_board():
                    tic_tac_toe.display_board()
                    print("Win the draw")
                    break
                else:
                    player_turn = "Player 1"

    if not re_run_game():
        break
    else:
        game_board = [" "] * 10
        tic_tac_toe = TicTacToeGame(game_board)
