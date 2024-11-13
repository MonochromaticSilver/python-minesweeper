from .game_state import game_state
import os


def print_board(game_state: game_state):
    # print(f" TODO print board (mines: {game_state.mines})")
    # Task: Implement the method that prints the board
    pass

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
