import pygame
import random

class Platform:
    def __init__(self):
        self.x = 30
        self.y = 300
        self.xr = 70
        self.yr = 14
        self.tex = pygame.image.load('plat.PNG')
        self.tex = pygame.transform.scale(self.tex, (self.xr, self.yr))
    def draw(self, screen, scroll):
        screen.blit(self.tex, (self.x, self.y + scroll))

    def random(self):
        self.x = random.randrange(0, 330)
        self.y = random.randrange(60, 490)