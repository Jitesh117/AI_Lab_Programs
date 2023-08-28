import pygame
import random

# Initialize pygame
pygame.init()

# Game settings
width, height = 640, 480
cell_size = 20
FPS = 10

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Create the game display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Snake class
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = (1, 0)

    def move(self, direction):
        self.direction = direction
        head_x, head_y = self.body[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail_x, tail_y = self.body[-1]
        self.body.append((tail_x, tail_y))

    def get_head_position(self):
        return self.body[0]

    def get_body(self):
        return self.body

# Apple class
class Apple:
    def __init__(self):
        self.position = (random.randint(0, width // cell_size - 1),
                         random.randint(0, height // cell_size - 1))

    def respawn(self):
        self.position = (random.randint(0, width // cell_size - 1),
                         random.randint(0, height // cell_size - 1))

    def get_position(self):
        return self.position

# Heuristic function
def heuristic(snake, apple):
    snake_head = snake.get_head_position()
    apple_position = apple.get_position()
    distance = abs(snake_head[0] - apple_position[0]) + abs(snake_head[1] - apple_position[1])
    return -distance

# Main game loop
def main():
    clock = pygame.time.Clock()
    snake = Snake()
    apple = Apple()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # AI-controlled movement using heuristic
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        best_direction = directions[0]
        best_score = heuristic(snake, apple)
        for direction in directions:
            new_head = (snake.get_head_position()[0] + direction[0],
                        snake.get_head_position()[1] + direction[1])
            if 0 <= new_head[0] < width // cell_size and 0 <= new_head[1] < height // cell_size:
                new_snake = Snake()
                new_snake.body = [new_head] + snake.get_body()
                new_score = heuristic(new_snake, apple)
                if new_score > best_score:
                    best_score = new_score
                    best_direction = direction

        snake.move(best_direction)

        # Check for collisions
        if snake.get_head_position() == apple.get_position():
            snake.grow()
            apple.respawn()

        # Draw everything
        screen.fill(black)
        for segment in snake.get_body():
            pygame.draw.rect(screen, green, (segment[0] * cell_size, segment[1] * cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, red, (apple.get_position()[0] * cell_size, apple.get_position()[1] * cell_size, cell_size, cell_size))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
