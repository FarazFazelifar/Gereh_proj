import random


class GameBoard:

    def __init__(self, size = 4):
        self.size = size
        self.grid = [[0 for _ in range(self.size)] for _ in range(self.size)]

    def spawn_new_tile(self):
        rand = False
        for row in self.grid:
            if 0 in row:
                rand = True
                break
        while rand:
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)
            if self.grid[i][j] == 0:
                self.grid[i][j] = 2
                rand = False
        return rand

    def __move_tiles(self, direction):
        if direction == 'right':
            for _ in range(self.size - 1):
                for i in range(1, self.size):
                    for j in range(self.size):
                        if self.grid[j][i] == 0:
                            self.grid[j][i] = self.grid[j][i - 1]
                            self.grid[j][i - 1] = 0

        if direction == 'left':
            for _ in range(self.size - 1):
                for i in range(1, self.size):
                    for j in range(self.size):
                        if self.grid[j][i - 1] == 0:
                            self.grid[j][i - 1] = self.grid[j][i]
                            self.grid[j][i] = 0

        if direction == 'up':
            for _ in range(self.size - 1):
                for i in range(1, self.size):
                    for j in range(self.size):
                        if self.grid[i - 1][j] == 0:
                            self.grid[i - 1][j] = self.grid[i][j]
                            self.grid[i][j] = 0

        if direction == 'down':
            for _ in range(self.size - 1):
                for i in range(1, self.size):
                    for j in range(self.size):
                        if self.grid[self.size - i][j] == 0:
                            self.grid[self.size - i][j] = self.grid[self.size - i - 1][j]
                            self.grid[self.size - i - 1][j] = 0

    def __merge_tiles(self, direction):
        if direction == 'right':
            for i in range(self.size - 1):
                for j in range(self.size):
                    if self.grid[j][self.size - 1 - i] == self.grid[j][self.size - 1 - i - 1]:
                        self.grid[j][self.size - 1 - i] = 2 * self.grid[j][self.size - 1 - i]
                        self.grid[j][self.size - 1 - i - 1] = 0

        if direction == 'left':
            for i in range(self.size - 1):
                for j in range(self.size):
                    if self.grid[j][i] == self.grid[j][i + 1]:
                        self.grid[j][i] = 2 * self.grid[j][i]
                        self.grid[j][i + 1] = 0

        if direction == 'up':
            for i in range(self.size - 1):
                for j in range(self.size):
                    if self.grid[i][j] == self.grid[i + 1][j]:
                        self.grid[i][j] = 2 * self.grid[i][j]
                        self.grid[i + 1][j] = 0

        if direction == 'down':
            for i in range(self.size - 1):
                for j in range(self.size):
                    if self.grid[self.size - 1 - i][j] == self.grid[self.size - 1 - i - 1][j]:
                        self.grid[self.size - 1 - i][j] = 2 * self.grid[self.size - 1 - i][j]
                        self.grid[self.size - 1 - i - 1][j] = 0

    def update_grid(self, direction):
        self.__move_tiles(direction)
        self.__merge_tiles(direction)
        self.__move_tiles(direction)
