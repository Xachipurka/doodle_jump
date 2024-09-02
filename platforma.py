import pygame
import random

class Platform:
    def __init__(self):
        self.x = 30
        self.y = 300
        self.xr = 70
        self.yr = 10

    def draw(self, screen, scroll):
        pygame.draw.rect(screen, (150, 150, 150), (self.x, self.y + scroll, self.xr, self.yr))

    def random(self):
        self.x = random.randrange(0, 330)
        self.y = random.randrange(60, 490)