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
        self.min_y = self.y
        self.xr = 50
        self.yr = 56
        self.s = 0
        self.t = time.perf_counter()
        self.right = False
        self.left = False
        self.dir = 0
        self.tex = [0, pygame.image.load('dod1.PNG'), pygame.image.load('dod2.PNG'), pygame.image.load('dod3.PNG'), pygame.image.load('dod4.PNG')]
        self.time = time.perf_counter()

        for i in range(1, len(self.tex)):
            self.tex[i] = pygame.transform.scale(self.tex[i], (self.xr, self.yr))

    def draw(self, screen):
        y = 200 + (self.y - self.min_y)
        if time.perf_counter() - self.time > 0.2:
            if self.dir == 0:
                screen.blit(self.tex[1], (self.x, y))
            elif self.dir == 1:
                screen.blit(self.tex[2], (self.x, y))
        else:
            if self.dir == 0:
                screen.blit(self.tex[4], (self.x, y))
            elif self.dir == 1:
                screen.blit(self.tex[3], (self.x, y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.dir = 0
                self.right = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.dir = 1
                self.left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.right = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.left = False

    def fall_move(self, platforms):
        for pl in platforms:
            if collision(self.x, self.y, self.xr, self.yr, pl.x, pl.y, pl.xr, pl.yr) and self.s > 0:
                self.s = -200
                self.time = time.perf_counter()

        self.y += self.s * (time.perf_counter() - self.t)
        self.min_y = min(self.y, self.min_y)
        self.s += 46 * (time.perf_counter() - self.t)
        self.t = time.perf_counter()

        if self.right:
            self.x += 4
        elif self.left:
            self.x -= 4

def f(a, b):
    print(a + b)

f(5, 3)
print(5 + 3)