from .game_state import game_state, GameState
import os
# import rich


def print_board(game_state: game_state):
    # print(f" TODO print board (mines: {game_state.mines})")
    # Task: Implement the method that prints the board
    # 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣🟨 <-- copy and paste
    for y in range(game_state.height):
        for x in range(game_state.width):
            if (x, y) == game_state.cursor:
                print("🟨", end="")
            elif (x, y) in game_state.mines and game_state.game_state != GameState.PLAYING:
                print("💣", end="")
            elif (x, y) in game_state.flags:
                print("🚩", end="")
            elif (x, y) in game_state.revealed:
                number_mines = game_state.number_mines(x, y)
                if number_mines == 0:
                    print("🟫", end="")
                if number_mines == 1:
                    print("\u0031\ufe0f\u20e3 ", end ='')
                if number_mines == 2:
                    print("\u0032\ufe0f\u20e3 ", end ='')
                if number_mines == 3:
                    print("\u0033\ufe0f\u20e3 ", end ='')
                if number_mines == 4:
                    print("\u0034\ufe0f\u20e3 ", end ='')
                if number_mines == 5:
                    print("\u0035\ufe0f\u20e3 ", end ='')
                if number_mines == 6:
                    print("\u0036\ufe0f\u20e3 ", end ='')
                if number_mines == 7:
                    print("\u0037\ufe0f\u20e3 ", end ='')
                if number_mines == 8:
                    print("\u0038\ufe0f\u20e3 ", end ='')
            else:
                print("🟩", end="")
        print()

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    print('\n\n')
    # else:
        # os.system('clear')
