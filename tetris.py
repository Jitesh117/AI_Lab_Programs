import pygame
import random

pygame.init()

# Constants
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 0, 0], [1, 1, 1]],
    [[0, 0, 1], [1, 1, 1]],
    [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
]

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

class TetrisGame:
    def __init__(self):
        self.board = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
        self.current_shape = self.get_new_shape()
        self.current_x = (len(self.board[0]) - len(self.current_shape[0])) // 2
        self.current_y = 0

    def get_new_shape(self):
        shape = random.choice(SHAPES)
        return shape

    def draw_board(self):
        screen.fill(WHITE)
        for y, row in enumerate(self.board):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, BLACK, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        for y, row in enumerate(self.current_shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, BLACK, ((self.current_x + x) * BLOCK_SIZE, (self.current_y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def move_shape(self, dx, dy):
        new_x = self.current_x + dx
        new_y = self.current_y + dy
        if self.is_valid_move(self.current_shape, new_x, new_y):
            self.current_x = new_x
            self.current_y = new_y

    def is_valid_move(self, shape, x, y):
        for y_offset, row in enumerate(shape):
            for x_offset, cell in enumerate(row):
                if cell:
                    if y + y_offset >= len(self.board) or x + x_offset < 0 or x + x_offset >= len(self.board[0]) or self.board[y + y_offset][x + x_offset]:
                        return False
        return True

    def place_shape(self):
        for y_offset, row in enumerate(self.current_shape):
            for x_offset, cell in enumerate(row):
                if cell:
                    self.board[self.current_y + y_offset][self.current_x + x_offset] = 1
        self.current_shape = self.get_new_shape()
        self.current_x = (len(self.board[0]) - len(self.current_shape[0])) // 2
        self.current_y = 0

    def remove_completed_rows(self):
        rows_to_remove = []
        for y, row in enumerate(self.board):
            if all(cell for cell in row):
                rows_to_remove.append(y)
        for y in rows_to_remove:
            del self.board[y]
            self.board.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_shape(-1, 0)
                    elif event.key == pygame.K_RIGHT:
                        self.move_shape(1, 0)
                    elif event.key == pygame.K_DOWN:
                        self.move_shape(0, 1)

            self.move_shape(0, 1)

            if not self.is_valid_move(self.current_shape, self.current_x, self.current_y + 1):
                self.place_shape()
                self.remove_completed_rows()

            self.draw_board()
            pygame.display.flip()
            clock.tick(3)

        pygame.quit()

if __name__ == "__main__":
    game = TetrisGame()
    game.run()
