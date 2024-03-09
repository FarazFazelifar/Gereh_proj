import sys

import pygame

from UI import *
from game_assets import *

pygame.init()

resolution = 1920
grid_margin = 30
border_length = 7
default_size = resolution + grid_margin
game_size = 4
cell_length = (default_size - grid_margin - game_size * grid_margin) / game_size
min_w = 300
frame = start_frame = 0
animation_length = 5
start_screen = True
game_screen = False
end_screen = False
move_grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
animating = False

game_board = GameBoard(game_size)

main_window = pygame.Surface((480, 480))
main_display = pygame.display.set_mode((480, 480), pygame.RESIZABLE)
pygame.display.set_caption("The 2048 Game!")

start_button = Button(0, 0, 200, 50, (143, 122, 102), (153, 132, 112), "Start", 40)

clock = pygame.time.Clock()


def main_game(event, saved_grid):

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            direction = 'up'
            game_board.move_tiles(direction)
            game_board.merge_tiles(direction)
            game_board.move_tiles(direction)
            if saved_grid != game_board.grid:
                game_board.spawn_new_tile()

        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
            direction = 'left'
            game_board.move_tiles(direction)
            move_animation("left", saved_grid)
            game_board.merge_tiles(direction)
            game_board.move_tiles(direction)
            if saved_grid != game_board.grid:
                game_board.spawn_new_tile()

        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
            direction = 'down'
            game_board.move_tiles(direction)
            game_board.merge_tiles(direction)
            game_board.move_tiles(direction)
            if saved_grid != game_board.grid:
                game_board.spawn_new_tile()

        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            direction = 'right'
            game_board.move_tiles(direction)
            move_animation("right", saved_grid)
            game_board.merge_tiles(direction)
            game_board.move_tiles(direction)
            if saved_grid != game_board.grid:
                game_board.spawn_new_tile()

        has_zero = False
        for row in saved_grid:
            if 0 in row:
                has_zero = True
                break
        if not has_zero and saved_grid == game_board.grid:
            pygame.quit()
            sys.exit()


def start_menu():
    main_display.fill((250, 248, 239))
    start_screen = True
    game_screen = False
    end_screen = False

    start_button.w = main_display.get_width() * 0.2
    start_button.x = main_display.get_width() * 0.5 - start_button.w // 2
    start_button.y = main_display.get_height() * 0.5 - start_button.h // 2
    start_button.draw(main_display)
    start_button.mouseover(main_display, mouse_rect, click[0])
    #txtToScreen("2048", (main_display.get_width() * 0.5, main_display.get_height() * 0.3), 151, main_display,
                #color=(0, 0, 0), bold=True)
    txtToScreen("2048", (main_display.get_width() * 0.5, main_display.get_height() * 0.3), 150, main_display, color=(112, 104, 95), bold=False)
    pygame.draw.rect(main_display, (143, 122, 102), (0, 0, main_display.get_width(), border_length))
    pygame.draw.rect(main_display, (143, 122, 102), (0, 0, border_length, main_display.get_height()))
    pygame.draw.rect(main_display, (143, 122, 102), (main_display.get_width() - border_length, 0, border_length, main_display.get_height()))
    pygame.draw.rect(main_display, (143, 122, 102), (0, main_display.get_height() - border_length, main_display.get_width(), border_length))
    if start_button.action:
        start_screen = False
        game_screen = True
        end_screen = False
        game_size = 5
        return start_screen, game_screen, end_screen
    return start_screen, game_screen, end_screen


def move_animation(direction, saved_grid):

    if direction == "right":
        for i in range(game_size):
            for j in range(game_size):
                cell_counter = 0
                for k in range(game_size - 1 - j):
                    if saved_grid[i][j] != 0:
                        if saved_grid[i][j + k + 1] == 0 or saved_grid[i][j + k + 1] == saved_grid[i][j]:
                            cell_counter += 1
                        else:
                            break
                    else:
                        break
                move_grid[i][j] = cell_counter

    if direction == "left":
        for i in range(game_size):
            for j in range(game_size):
                cell_counter = 0
                for k in range(game_size - 1 - j):
                    if saved_grid[i][3 - j] != 0:
                        if saved_grid[i][3 - j - k - 1] == 0 or saved_grid[i][3 - j - k - 1] == saved_grid[i][3 - j]:
                            cell_counter -= 1
                        else:
                            break
                    else:
                        break
                move_grid[i][j] = cell_counter

    return move_grid


def draw_animaion_horizontal(move_grid, frame):

    game_surface = pygame.Surface((default_size, default_size))
    main_display.fill((250, 248, 239))
    game_surface.fill((187, 173, 160))

    for i in range(game_size):
        for j in range(game_size):
            text = str(saved_grid[j][i])
            match saved_grid[j][i]:
                case 0:
                    color = (205, 193, 180)
                    text = ""
                case 2:
                    color = (238, 228, 218)
                case 4:
                    color = (237, 224, 200)
                case 8:
                    color = (242, 177, 121)
                case 16:
                    color = (245, 149, 99)
                case 32:
                    color = (246, 124, 95)
                case 64:
                    color = (246, 94, 59)
                case 128:
                    color = (237, 207, 114)
                case 256:
                    color = (237, 204, 97)
                case 512:
                    color = (237, 200, 80)
                case 1024:
                    color = (237, 197, 63)
                case 2048:
                    color = (237, 194, 46)

            if saved_grid[j][i] != 0:
                pygame.draw.rect(game_surface, color, (
                    i * (cell_length + grid_margin) + grid_margin + frame * move_grid[j][i] * cell_length / animation_length,
                    j * (cell_length + grid_margin) + grid_margin,
                    cell_length,
                    cell_length))
                txtToScreen(text,
                            (i * (cell_length + grid_margin) + grid_margin + cell_length // 2 + frame * move_grid[j][i] * cell_length / animation_length,
                             j * (cell_length + grid_margin) + grid_margin + cell_length // 2),
                            150,
                            game_surface)

    game_surface = pygame.transform.scale(game_surface, (
        min(main_display.get_width(), main_display.get_height()),
        min(main_display.get_width(), main_display.get_height())))
    main_display.blit(game_surface, (main_display.get_width() // 2 - game_surface.get_width() // 2,
                                     main_display.get_height() // 2 - game_surface.get_height() // 2))

def draw_current_board():
    game_surface = pygame.Surface((default_size, default_size))
    main_display.fill((250, 248, 239))
    game_surface.fill((187, 173, 160))

    for i in range(game_size):
        for j in range(game_size):
            text = str(game_board.grid[j][i])
            match game_board.grid[j][i]:
                case 0:
                    color = (205, 193, 180)
                    text = ""
                case 2:
                    color = (238, 228, 218)
                case 4:
                    color = (237, 224, 200)
                case 8:
                    color = (242, 177, 121)
                case 16:
                    color = (245, 149, 99)
                case 32:
                    color = (246, 124, 95)
                case 64:
                    color = (246, 94, 59)
                case 128:
                    color = (237, 207, 114)
                case 256:
                    color = (237, 204, 97)
                case 512:
                    color = (237, 200, 80)
                case 1024:
                    color = (237, 197, 63)
                case 2048:
                    color = (237, 194, 46)

            if game_board.grid[j][i] != 0:
                pygame.draw.rect(game_surface, color, (
                    i * (cell_length + grid_margin) + grid_margin,
                    j * (cell_length + grid_margin) + grid_margin,
                    cell_length,
                    cell_length))
                txtToScreen(text,
                            (i * (cell_length + grid_margin) + grid_margin + cell_length // 2,
                             j * (cell_length + grid_margin) + grid_margin + cell_length // 2),
                            150,
                            game_surface)

    game_surface = pygame.transform.scale(game_surface, (
        min(main_display.get_width(), main_display.get_height()),
        min(main_display.get_width(), main_display.get_height())))
    main_display.blit(game_surface, (main_display.get_width() // 2 - game_surface.get_width() // 2,
                                     main_display.get_height() // 2 - game_surface.get_height() // 2))


for _ in range(2):
    game_board.spawn_new_tile()

while True:
    clock.tick(60)

    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 15, 15)

    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            if event.w < min_w or event.h < min_w:
                main_display = pygame.display.set_mode((min_w, min_w), pygame.RESIZABLE)
            else:
                main_display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if start_screen:
            start_screen, game_screen, end_screen = start_menu()

        if game_screen:
            if event.type == pygame.KEYDOWN:
                saved_grid = []
                for row in game_board.grid:
                    saved_grid.append(row.copy())
                frame = 0
                main_game(event, saved_grid)
                move_grid = move_animation(event, saved_grid=saved_grid)
                animating = True

    if game_screen:
        if animating:
            draw_animaion_horizontal(move_grid=move_grid, frame=frame)
        else:
            draw_current_board()
        if frame == animation_length - 1:
            move_grid = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
            animating = False

    frame += 1
    frame %= animation_length

    pygame.display.flip()
