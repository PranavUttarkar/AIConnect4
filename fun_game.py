# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Joshua Landgraf
#               Pranav Uttarkar
#               Milan Guddeti
#               Braydyn Godley
#               Bokai Liao
# Section:      216
# Assignment:   Lab 13 Team
# Date:         11/25/2024


import numpy as np
import pygame
import sys
import math
import os

# Colors
COLOR_BLUE = (1, 0, 200)
COLOR_BLACK = (0, 0, 0)
COLOR_RED = (200, 0, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_WHITE = (255, 255, 255)

ROWS = 6
COLUMNS = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)

# File to save the score
SCORE_FILE = "connect4_scores.txt"


def make_grid():
    """Creates and returns an empty game grid."""
    grid = np.zeros((ROWS, COLUMNS))
    return grid


def place_disc(grid, row, col, disc):
    """Places a disc in the specified row and column."""
    grid[row][col] = disc


def is_column_valid(grid, col):
    """Checks if the selected column is valid for placing a disc."""
    return grid[ROWS - 1][col] == 0


def find_next_open_row(grid, col):
    """Finds the next open row in the specified column."""
    for row in range(ROWS):
        if grid[row][col] == 0:
            return row


def check_victory(grid, disc):
    """Checks if the given disc has won the game."""
    # Check horizontal connections
    for col in range(COLUMNS - 3):
        for row in range(ROWS):
            if all(grid[row][col + i] == disc for i in range(4)):
                return True

    # Check vertical connections
    for col in range(COLUMNS):
        for row in range(ROWS - 3):
            if all(grid[row + i][col] == disc for i in range(4)):
                return True

    # Check diagonals (positive slope)
    for col in range(COLUMNS - 3):
        for row in range(ROWS - 3):
            if all(grid[row + i][col + i] == disc for i in range(4)):
                return True

    # Check diagonals (negative slope)
    for col in range(COLUMNS - 3):
        for row in range(3, ROWS):
            if all(grid[row - i][col + i] == disc for i in range(4)):
                return True

    return False


def draw_grid(grid, screen, height):
    """Draws the game grid using Pygame."""
    for col in range(COLUMNS):
        for row in range(ROWS):
            pygame.draw.rect(screen, COLOR_BLUE, (col * SQUARESIZE, row * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, COLOR_BLACK, (int(col * SQUARESIZE + SQUARESIZE / 2),
                                                     int(row * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for col in range(COLUMNS):
        for row in range(ROWS):
            if grid[row][col] == 1:
                pygame.draw.circle(screen, COLOR_RED,
                                   (int(col * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
            elif grid[row][col] == 2:
                pygame.draw.circle(screen, COLOR_YELLOW,
                                   (int(col * SQUARESIZE + SQUARESIZE / 2), height - int(row * SQUARESIZE + SQUARESIZE / 2)),
                                   RADIUS)
    pygame.display.update()


def display_menu(screen, font):
    """Displays the game menu."""
    screen.fill(COLOR_WHITE)
    title = font.render("Connect 4 Menu", True, COLOR_BLUE)
    screen.blit(title, (200, 50))

    options = ["1. Show Rules", "2. Display Scores", "3. Start Game", "4. Quit"]
    for i, option in enumerate(options):
        label = font.render(option, True, COLOR_BLACK)
        screen.blit(label, (200, 150 + i * 50))

    pygame.display.update()


def load_scores():
    """Loads scores from a file. If the file doesn't exist, it makes the scores."""
    if not os.path.exists(SCORE_FILE):
        return {"Player 1": 0, "Player 2": 0}
    with open(SCORE_FILE, "r") as file:
        try:
            scores = eval(file.read())
        except Exception:
            scores = {"Player 1": 0, "Player 2": 0}
    return scores


def save_scores(scores):
    """Saves the scores to a file."""
    with open(SCORE_FILE, "w") as file:
        file.write(str(scores))


def show_rules(screen, font):
    """Displays the game rules on the screen."""
    screen.fill(COLOR_WHITE)
    rules = [
        "1. Players take turns dropping a disc into a column.", "2. The first player to connect 4 discs wins.", "3. If all columns are filled, the game is a draw."]
    y_offset = 100
    for rule in rules:
        label = font.render(rule, True, COLOR_BLACK)
        screen.blit(label, (50, y_offset))
        y_offset += 50

    pygame.display.update()
    pygame.time.wait(15000)



pygame.init()
width = COLUMNS * SQUARESIZE
height = (ROWS + 1) * SQUARESIZE
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("comicsans", 20)

# make game state
grid = make_grid()
scores = load_scores()
game_over = False
turn = 0
in_menu = True

while True:
    if in_menu:
        display_menu(screen, font)
    else:
        draw_grid(grid, screen, height)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_scores(scores)
            pygame.quit()
            sys.exit()

        if in_menu:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    show_rules(screen, font)
                elif event.key == pygame.K_2:
                    print(f"Scores: {scores}")
                elif event.key == pygame.K_3:
                    in_menu = False
                elif event.key == pygame.K_4:
                    save_scores(scores)
                    pygame.quit()
                    sys.exit()

        elif not in_menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                col = int(math.floor(posx / SQUARESIZE))
                if is_column_valid(grid, col):
                    row = find_next_open_row(grid, col)
                    place_disc(grid, row, col, turn + 1)

                    if check_victory(grid, turn + 1):
                        draw_grid(grid, screen, height)
                        print(f"Player {turn + 1} wins!")
                        scores[f"Player {turn + 1}"] += 1
                        save_scores(scores)
                        pygame.time.wait(3000)
                        in_menu = True
                        grid = make_grid()

                    turn = (turn + 1) % 2
 