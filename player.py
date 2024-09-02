import pygame
import time


def collision(x, y, sizeX, sizeY, x2, y2, sizeX2, sizeY2):
    if (x + sizeX >= x2 and x2 + sizeX2 >= x) and (y + sizeY >= y2 and y2 + sizeY2 >= y):
        return True
    return False


class Player:
    def __init__(self):
        print("Player created")
        self.x = 150
        self.y = 50
        self.xr = 30
        self.yr = 36
        self.s = 0
        self.t = time.perf_counter()
        self.right = False
        self.left = False

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, 200, self.xr, self.yr))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_LEFT:
                self.left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_LEFT:
                self.left = False

    def fall_move(self, platforms):
        for pl in platforms:

            if collision(self.x, self.y, self.xr, self.yr, pl.x, pl.y, pl.xr, pl.yr) and self.s > 0:
                self.s = -180

        self.y += self.s * (time.perf_counter() - self.t)
        self.s += 40 * (time.perf_counter() - self.t)
        self.t = time.perf_counter()

        if self.right:
            self.x += 4
        elif self.left:
            self.x -= 4




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