import pygame, sys

from game_assets import *
from UI import *

pygame.init()

grid_margin = 10
default_size = 960 + grid_margin
game_size = int(input("size: "))
cell_length = (default_size - grid_margin - game_size * grid_margin) / game_size
min_w = 300

game_board = GameBoard(game_size)

main_window = pygame.Surface((default_size, default_size))
main_display = pygame.display.set_mode((default_size, default_size), pygame.RESIZABLE)
pygame.display.set_caption("The 2048 Game!")

clock = pygame.time.Clock()

for _ in range(2):
    game_board.spawn_new_tile()

while True:
    clock.tick(60)

    game_surface = pygame.Surface((default_size, default_size))
    main_display.fill((250,248,239))
    game_surface.fill((187,173,160))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            if event.w < min_w or event.h < min_w:
                main_display = pygame.display.set_mode((min_w, min_w), pygame.RESIZABLE)
            else:
                main_display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.KEYDOWN:
            saved_grid = game_board.grid.copy()
            if event.key == pygame.K_w:
                game_board.update_grid('up')
                if saved_grid == game_board.grid:
                    game_board.spawn_new_tile()
                for row in game_board.grid:
                    print(row)
                print("")
                print("")
            
            if event.key == pygame.K_a:
                game_board.update_grid('left')
                if saved_grid == game_board.grid:
                    game_board.spawn_new_tile()
                for row in game_board.grid:
                    print(row)
                print("")
                print("")

            if event.key == pygame.K_s:
                game_board.update_grid('down')
                if saved_grid == game_board.grid:
                    game_board.spawn_new_tile()
                for row in game_board.grid:
                    print(row)
                print("")
                print("")

            if event.key == pygame.K_d:
                game_board.update_grid('right')
                if saved_grid == game_board.grid:
                    game_board.spawn_new_tile()
                for row in game_board.grid:
                    print(row)
                print("")
                print("")
    
    for i in range(game_size):
        for j in range(game_size):
            match game_board.grid[j][i]:
                case 0: 
                    color = (205,193,180)
                case 2:
                    color = (238,228,218)
                case 4:
                    color = (237,224,200)
                case 8:
                    color = (242,177,121)
                case 16:
                    color = (245,149,99)
                case 32:
                    color = (246,124,95)
                case 64:
                    color = (246,94,59)
                case 128:
                    color = (237,207,114)
                case 256:
                    color = (237,204,97)
                case 512:
                    color = (237,200,80)
                case 1024:
                    color = (237,197,63)
                case 2048:
                    color = (237,194,46)

            pygame.draw.rect(game_surface, color, (i * (cell_length + grid_margin) + grid_margin, j * (cell_length + grid_margin) + grid_margin, cell_length, cell_length))

    game_surface = pygame.transform.scale(game_surface, (min(main_display.get_width(), main_display.get_height()), min(main_display.get_width(), main_display.get_height())))
    main_display.blit(game_surface, (main_display.get_width() // 2 - game_surface.get_width() // 2, main_display.get_height() // 2 - game_surface.get_height() // 2))
                    
    pygame.display.flip()
