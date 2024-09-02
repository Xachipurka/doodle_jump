import pygame
from player import Player
from platforma import *
import random


pygame.init()
screen = pygame.display.set_mode((470, 550))
running = True

pr = Player()
pl = [Platform() for _ in range(30000)]
ply = 500

for p in pl:
    ply -= 70
    p.y = ply
    p.x = random.randrange(0, 330)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pr.control(event);

    pr.fall_move(platforms=pl)
    screen.fill('black')

    pr.draw(screen)
    for i in pl:
        scroll = 200 - pr.y
        i.draw(screen, scroll)

    pygame.display.flip()
pygame.quit()