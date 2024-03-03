import random

import pygame

from game_assets import *
from UI import *

pygame.init()

game_board = GameBoard()

for _ in range(2):
    game_board.spawn_new_tile()

while True:
    for _ in range(4):
        print(game_board.grid[_])
    print("")
    print("")
    direction = input('->')
    game_board.update_grid(direction)
