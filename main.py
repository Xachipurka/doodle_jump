import pygame
from player import Player
from platforma import *
import random

with open('record.txt', 'r', encoding='utf-8') as file:
    record = int(file.readline())

pygame.init()
screen = pygame.display.set_mode((470, 550))
running = True

pr = Player()
pl = [Platform() for _ in range(10000)]
ply = 500
font = pygame.font.Font(None, 30)

for p in pl:
    ply -= 70
    p.y = ply
    p.x = random.randrange(0, 330)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pr.control(event);
    if pr.y - pr.min_y > 300:
        running = False
    pr.fall_move(platforms=pl)
    screen.fill('black')

    pr.draw(screen)
    for i in pl:
        scroll = 200 - pr.min_y
        i.draw(screen, scroll)

    text = font.render(f'Высота - {-int(pr.min_y)}', True, (255, 255, 255))
    text_record = font.render(f'Рекорд: {record}', True, (255, 255, 255))

    screen.blit(text, (20, 10))
    screen.blit(text_record, (330, 10))

    pygame.display.flip()
pygame.quit()
if -int(pr.min_y) > record:
    with open('record.txt', 'w', encoding='utf-8') as file:
        file.write(str(-int(pr.min_y)))