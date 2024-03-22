import pygame
pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIGTH = 800
screen = pygame.display.set_mode((SCREEN_WIGTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра ТИР")
icon = pygame.image.load("/img/icon1.jpg")
pygame.display.set_icon(icon)


running = True
while running:
    pass

pygame.quit()