import pygame
import random
import tkinter as tk

def get_interval():
    time_interval = time_var.get()
    return int(time_interval)  # convert string to integer

root = tk.Tk()
root.geometry('200x100')

time_var = tk.StringVar()

label = tk.Label(root, text='Введите интервал времени в секундах')
label.pack()

time_entry = tk.Entry(root, textvariable=time_var)
time_entry.pack()

button = tk.Button(root, text='Начать игру', command=get_interval)
button.pack()

root.mainloop()  # this should block

pygame.init()

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра ТИР')
icon = pygame.image.load('img/img1.png')
pygame.display.set_icon(icon)

target_image = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

time_interval = get_interval() * 1000  # Преобразование в миллисекунды

hits = 0
misses = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
last_time = pygame.time.get_ticks()

running = True
while running:
    screen.fill(color)

    hit_text = font.render(f'Попадания: {hits}', True, (0, 0, 0))
    miss_text = font.render(f'Промахи: {misses}', True, (0, 0, 0))

    screen.blit(hit_text, (10, 10))
    screen.blit(miss_text, (10, 50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            else:
                misses += 1
    if pygame.time.get_ticks() - last_time >= time_interval:
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        last_time = pygame.time.get_ticks()

    screen.blit(target_image, (target_x, target_y))

    pygame.display.update()
pygame.quit()