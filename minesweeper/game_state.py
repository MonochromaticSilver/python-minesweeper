from enum import Enum
import random

class GameState(Enum):
    PLAYING = 1
    LOST = 2
    WON = 3

class game_state:
    def __init__(self, width = 9, height = 9, mine_count = 10):
        self.width = width
        self.height = height
        self.mines = []
        self.flags = []
        self.revealed = []
        self.cursor = (0,0)
        self.game_state = GameState.PLAYING
        self._generate_mines(mine_count)

    def _generate_mines(self, mine_count):
        # Task: Implement the method that generates mines based on width/height/mine_count
        # This would involve generating a list of random (x, y) coordinates
        rangeX = (0, self.width)
        rangeY = (0, self.height)

        randPoints = []
        current_generated_mines = 0
        while current_generated_mines < mine_count:
            x = random.randrange(*rangeX)
            y = random.randrange(*rangeY)
            if (x, y) not in randPoints:
                randPoints.append((x, y))
                current_generated_mines += 1
        
        self.mines = randPoints

    def number_mines(self, x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        counted_mines = 0

        for dx, dy in directions:
            mine_check_x = x + dx
            mine_check_y = y + dy

            if (mine_check_x, mine_check_y) in self.mines:
                counted_mines += 1
                # self.shown_listed_mines.append((mine_check_x, mine_check_y))

        return counted_mines




game_instance = game_state()
    