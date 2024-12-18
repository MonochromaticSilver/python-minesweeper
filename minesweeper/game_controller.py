from collections import deque
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
        if key == 'f' or key == 'F':
            if self.game_state.cursor in self.game_state.flags:
                self.game_state.flags.remove(self.game_state.cursor)
            else:   
                self.game_state.flags.append(self.game_state.cursor)
        if key == 'r' or key == 'R':
            if self.game_state.cursor in self.game_state.mines:
                self.game_state.game_state = 2
            else:
                self._reveal(self.game_state.cursor[0], self.game_state.cursor[1])

    def _reveal(self, x, y):
        queue = deque()
        queue.append((x, y))
        while len(queue) > 0:
            item = queue.popleft()
            if item in self.game_state.revealed:
                continue
            self.game_state.revealed.append(item)
            if self.game_state.number_mines(item[0], item[1]) > 0:
                continue
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

            for dx, dy in directions:
                mine_check_x = item[0] + dx
                mine_check_y = item[1] + dy

                if mine_check_x < 0 or mine_check_x >= self.game_state.width:
                    continue
                if mine_check_y < 0 or mine_check_y >= self.game_state.height:
                    continue
                queue.append((mine_check_x, mine_check_y))
                    
    def print_end_game(self):
        # Task: Implement the method that prints the end game message then waits for the user to push a key (to return to the menu loop)
        clear_console()
        print_board(self.game_state)
        print("Game Over")
        input("Press enter key to return to the main menu")
        pass
