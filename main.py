import pygame
from player import Player
from platforma import *


pygame.init()
screen = pygame.display.set_mode((470, 550))
running = True

pr = Player()
pl = [Platform() for _ in range(10)]
for i in pl:
    i.random()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pr.control(event);

    pr.fall()
    screen.fill('black')

    pr.draw(screen)
    for i in pl:
        i.draw(screen)

    pygame.display.flip()
pygame.quit()