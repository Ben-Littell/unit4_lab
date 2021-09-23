import pygame
import math
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (51, 31, 153)
BLACK = (0, 0, 0)
COLORS = [RED, GREEN, BLUE, BLACK]
LIGHT_GREEN = (25, 227, 79)
GRASS = (33, 110, 2)
WHITE_H = (254, 249, 238)
# Math Constants
PI = math.pi

# Game Constants
SIZE = (700, 500)
FPS = 60

GRASS_CORDS = (0, 350, 700, 500)
SKY_CORDS = (0, 0, 700, 350)

#####################################################

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('First Scene')
clock = pygame.time.Clock()

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Background
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRASS, GRASS_CORDS)
    pygame.draw.rect(screen, SKY_BLUE, SKY_CORDS)
    # House
    pygame.draw.rect(screen, WHITE_H, (50, 220, 100, 130))
    pygame.draw.polygon(screen, WHITE_H, [[100, 170], [50, 220], [150, 220]])
    pygame.draw.ellipse(screen, BLACK, (88, 180, 25, 25), 2)
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
