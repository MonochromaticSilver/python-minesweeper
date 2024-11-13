from minesweeper.game_state import game_state, GameState
from minesweeper.ui import clear_console, print_board
import readchar

class game_controller:
    def __init__(self, game_state: game_state):
        self.game_state = game_state

    def play_until_end(self):
        while self.game_state.game_state == GameState.PLAYING:
            self.play_game_turn()
        self.print_end_game()

    def play_game_turn(self):
        clear_console()
        print_board(self.game_state)
        # Task: Implement the method that plays a single turn of the game (including printing the UI)
        
        #for now, we'll just loose the game
        #self.game_state.game_state = GameState.LOST
        key = readchar.readkey()
        if key == readchar.key.LEFT:
            self.game_state.cursor = (max(0, self.game_state.cursor[0] - 1), self.game_state.cursor[1])
        if key == readchar.key.RIGHT:
            self.game_state.cursor = (min(self.game_state.width - 1, self.game_state.cursor[0] + 1), self.game_state.cursor[1])
        if key == readchar.key.DOWN:
            self.game_state.cursor = (self.game_state.cursor[0], min(self.game_state.height - 1, self.game_state.cursor[1] + 1))
        if key == readchar.key.UP:
            self.game_state.cursor = (self.game_state.cursor[0], max( 0, self.game_state.cursor[1] - 1))

    def print_end_game(self):
        # Task: Implement the method that prints the end game message then waits for the user to push a key (to return to the menu loop)
        clear_console()
        print_board(self.game_state)
        print("Game Over")
        input("Press enter key to return to the main menu")
        pass
