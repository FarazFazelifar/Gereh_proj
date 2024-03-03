import random


class GameBoard:

    def __init__(self):
        self.grid = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    def spawn_new_tile(self):
        rand = True
        while rand:
            i = random.randint(0, 3)
            j = random.randint(0, 3)
            if self.grid[i][j] == 0:
                self.grid[i][j] = 2
                rand = False

    def __move_tiles(self, direction):
        if direction == 'right':
            for _ in range(3):
                for i in range(1, 4):
                    for j in range(4):
                        if self.grid[j][i] == 0:
                            self.grid[j][i] = self.grid[j][i - 1]
                            self.grid[j][i - 1] = 0

        if direction == 'left':
            for _ in range(3):
                for i in range(1, 4):
                    for j in range(4):
                        if self.grid[j][i - 1] == 0:
                            self.grid[j][i - 1] = self.grid[j][i]
                            self.grid[j][i] = 0

        if direction == 'up':
            for _ in range(3):
                for i in range(1, 4):
                    for j in range(4):
                        if self.grid[i - 1][j] == 0:
                            self.grid[i - 1][j] = self.grid[i][j]
                            self.grid[i][j] = 0

        if direction == 'down':
            for _ in range(3):
                for i in range(1, 4):
                    for j in range(4):
                        if self.grid[4 - i][j] == 0:
                            self.grid[4 - i][j] = self.grid[4 - i - 1][j]
                            self.grid[4 - i - 1][j] = 0

    def __merge_tiles(self, direction):
        if direction == 'right':
            for i in range(3):
                for j in range(4):
                    if self.grid[j][3 - i] == self.grid[j][3 - i - 1]:
                        self.grid[j][3 - i - 1] = 2 * self.grid[j][3 - i]
                        self.grid[j][3 - i] = 0

        if direction == 'left':
            for i in range(3):
                for j in range(4):
                    if self.grid[j][i] == self.grid[j][i + 1]:
                        self.grid[j][i] = 2 * self.grid[j][i]
                        self.grid[j][i + 1] = 0

        if direction == 'up':
            for i in range(3):
                for j in range(4):
                    if self.grid[i][j] == self.grid[i + 1][j]:
                        self.grid[i][j] = 2 * self.grid[i][j]
                        self.grid[i + 1][j] = 0

        if direction == 'down':
            for i in range(3):
                for j in range(4):
                    if self.grid[3 - i][j] == self.grid[3 - i - 1][j]:
                        self.grid[3 - i][j] = 2 * self.grid[3 - i][j]
                        self.grid[3 - i - 1][j] = 0

    def update_grid(self, direction):
        self.__move_tiles(direction)
        self.__merge_tiles(direction)
        self.__move_tiles(direction)
        self.spawn_new_tile()
