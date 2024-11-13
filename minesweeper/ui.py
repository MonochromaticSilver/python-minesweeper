from .game_state import game_state
import os


def print_board(game_state: game_state):
    # print(f" TODO print board (mines: {game_state.mines})")
    # Task: Implement the method that prints the board
    for y in range(game_state.height):
        for x in range(game_state.width):
            if (x, y) == game_state.cursor:
                print("🟨", end="")
            elif (x, y) in game_state.mines:
                print("💣", end="")
            else:
                print("🟫", end="")
        print()

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
