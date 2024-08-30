import pygame
import random

class Platform:
    def __init__(self):
        self.x = 30
        self.y = 300

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, 130, 50))

    def random(self):
        self.x = random.randrange(0, 330)
        self.y = random.randrange(60, 490)