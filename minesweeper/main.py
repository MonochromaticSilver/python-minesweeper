from minesweeper.game_state import game_state
from minesweeper.game_controller import game_controller
from minesweeper.ui import clear_console

def main():
    # Application loop
    while True:
        # Task: Implement more options (e.g. different game difficulties, etc.)
        clear_console()
        print("  == Minesweeper ==")
        print("Main Menu")
        print("1. Play Minesweeper")
        print("2. Exit\n")
        option = input("Choose an option: ")
        if option == "1":
            # for this option, we'll just use the default game state configuration
            main_game_state = game_state()
            main_game_controller = game_controller(main_game_state)
            main_game_controller.play_until_end()
        elif option == "2":
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
