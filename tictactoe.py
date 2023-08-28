import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_COLOR = (0, 0, 0)
LINE_WIDTH = 15
BOARD_SIZE = 3
CELL_SIZE = WIDTH // BOARD_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = [['' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Draw the game board
def draw_board():
    for row in range(1, BOARD_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * CELL_SIZE, 0), (row * CELL_SIZE, HEIGHT), LINE_WIDTH)

# Draw the X and O symbols
def draw_symbols():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE), ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, BLACK, (col * CELL_SIZE, (row + 1) * CELL_SIZE), ((col + 1) * CELL_SIZE, row * CELL_SIZE), LINE_WIDTH)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2, LINE_WIDTH)

# Check for a win
def check_win(player):
    for row in range(BOARD_SIZE):
        if all(cell == player for cell in board[row]):
            return True
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True
    if all(board[i][i] == player for i in range(BOARD_SIZE)) or all(board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)):
        return True
    return False

# Main game loop
turn = 'X'
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row = mouseY // CELL_SIZE
            clicked_col = mouseX // CELL_SIZE

            if board[clicked_row][clicked_col] == '':
                board[clicked_row][clicked_col] = turn
                if check_win(turn):
                    game_over = True
                else:
                    turn = 'O' if turn == 'X' else 'X'

    screen.fill(WHITE)
    draw_board()
    draw_symbols()
    pygame.display.update()

pygame.quit()
sys.exit()
