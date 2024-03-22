import pygame
import random

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("img/img1.png")
pygame.display.set_icon(icon)

pygame.image.load("img/target.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))



running = True
while running:
    pass

pygame.quit()