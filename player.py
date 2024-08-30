import pygame
import time


class Player:
    def __init__(self):
        print("Player created")
        self.x = 0
        self.y = 50
        self.s = 0
        self.t = time.perf_counter()

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, 50, 50))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.x += 1
            if event.key == pygame.K_LEFT:
                self.x -= 1

    def fall(self):
        self.y += self.s * (time.perf_counter() - self.t)
        self.s += 56 * (time.perf_counter() - self.t)
        self.t = time.perf_counter()


'''
player = Player()
print(player.x, player.y)
player.move(10, 10)
print(player.x, player.y)
'''

def f(a, b):
    print(a + b)

f(5, 3)
print(5 + 3)