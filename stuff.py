import pygame
import math
import random

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (51, 31, 153)
BLACK = (0, 0, 0)
LIGHT_GREEN = (25, 227, 79)
GRASS = (33, 110, 2)
HOUSE_C = (21, 42, 71)
COLORS = [RED, GREEN, BLUE, LIGHT_GREEN]
# Math Constants
PI = math.pi

# Game Constants
WIDTH = 700
SIZE = (WIDTH, 500)
FPS = 60

GRASS_CORDS = (0, 350, 700, 500)
SKY_CORDS = (0, 0, 700, 350)

#####################################################

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('First Scene')
clock = pygame.time.Clock()

cloud_x1 = 50
cloud_x2 = 60
cloud_x3 = 40
cloud_x4 = 75

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    cloud_x1 += 3
    cloud_x2 += 3
    cloud_x3 += 3
    cloud_x4 += 3
    if cloud_x4 > WIDTH + 50:
        cloud_x1 = -275      # 0
        cloud_x2 = -265     # + 10
        cloud_x3 = -285    # - 10
        cloud_x4 = -250     # + 25

    # Background
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRASS, GRASS_CORDS)
    pygame.draw.rect(screen, SKY_BLUE, SKY_CORDS)
    # Houses
    for numb in range(4):
        change_h = numb * 150
        # House
        pygame.draw.rect(screen, HOUSE_C, (50 + change_h, 220, 100, 130))
        pygame.draw.polygon(screen, HOUSE_C, [[100 + change_h, 170], [50 + change_h, 220], [150 + change_h, 220]])
        # Windows
        pygame.draw.ellipse(screen, BLACK, (88 + change_h, 184, 25, 25), 2)
        pygame.draw.rect(screen, BLACK, (65 + change_h, 230, 25, 25))
        pygame.draw.rect(screen, BLACK, (110 + change_h, 230, 25, 25))
        pygame.draw.rect(screen, BLACK, (65 + change_h, 275, 25, 25))
        pygame.draw.rect(screen, BLACK, (110 + change_h, 275, 25, 25))
        # Door
        pygame.draw.rect(screen, COLORS[numb], (88 + change_h, 310, 30, 40))
    # Clouds
    for numb in range(3):
        change_cx = numb * 110
        change_cy = numb * 20
        pygame.draw.ellipse(screen, WHITE, (cloud_x1 + change_cx, 30 + change_cy, 50, 30))
        pygame.draw.ellipse(screen, WHITE, (cloud_x2 + change_cx, 45 + change_cy, 50, 30))
        pygame.draw.ellipse(screen, WHITE, (cloud_x3 + change_cx, 35 + change_cy, 50, 30))
        pygame.draw.ellipse(screen, WHITE, (cloud_x4 + change_cx, 33 + change_cy, 50, 30))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
