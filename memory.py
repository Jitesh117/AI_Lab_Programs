import pygame
import random
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 100
GRID_SIZE = 4
GRID_ROWS, GRID_COLS = GRID_SIZE, GRID_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

# Load images
card_images = []
for i in range(1, (GRID_ROWS * GRID_COLS) // 2 + 1):
    image = pygame.image.load(f'card_{i}.png')
    image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
    card_images.extend([image.copy(), image.copy()])

# Shuffle the cards
random.shuffle(card_images)

# Create the grid of cards
cards = []
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        card = card_images.pop()
        x = col * CARD_WIDTH + (col + 1) * 10
        y = row * CARD_HEIGHT + (row + 1) * 10
        cards.append((card, (x, y), False))

# Game variables
selected_cards = []
pairs_found = 0
turns = 0

# Fonts
font = pygame.font.Font(None, 36)

# Main game loop
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if len(selected_cards) < 2:
                x, y = event.pos
                for card, (cx, cy), flipped in cards:
                    if not flipped and cx < x < cx + CARD_WIDTH and cy < y < cy + CARD_HEIGHT:
                        selected_cards.append((card, (cx, cy)))
                        if len(selected_cards) == 2:
                            turns += 1
                            if selected_cards[0][0] == selected_cards[1][0]:
                                pairs_found += 1
                                for i in range(len(cards)):
                                    if cards[i][0] == selected_cards[0][0]:
                                        cards[i] = (cards[i][0], cards[i][1], True)
                            pygame.time.wait(500)
                            selected_cards = []

    for card, (x, y), flipped in cards:
        if flipped:
            screen.blit(card, (x, y))
        else:
            card_back = pygame.image.load('card_back.png')
            card_back = pygame.transform.scale(card_back, (CARD_WIDTH, CARD_HEIGHT))
            screen.blit(card_back, (x, y))

    if pairs_found == GRID_ROWS * GRID_COLS // 2:
        text = font.render(f'You won in {turns} turns!', True, BLACK)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
