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
        self.mine_count = mine_count
        self.mines = []
        self.flags = []
        self.revealed = []
        self.cursor = (0,0)
        self.game_state = GameState.PLAYING
        # self.board = [['☐' for _ in range(self.width)] for _ in range(self.height)] possible solution?
        self._generate_mines()

    def _generate_mines(self):
        # Task: Implement the method that generates mines based on width/height/mine_count
        # This would involve generating a list of random (x, y) coordinates
        rangeX = (0, self.width)
        rangeY = (0, self.height)

        randPoints = []
        current_generated_mines = 0
        while current_generated_mines < self.mine_count:
            x = random.randrange(*rangeX)
            y = random.randrange(*rangeY)
            if (x, y) not in randPoints:
                randPoints.append((x, y))
                current_generated_mines += 1

        
        print(randPoints)

game_instance = game_state()
    