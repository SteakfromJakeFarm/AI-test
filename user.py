from config import *
import math


class Player:
    def __init__(self, x, y, s=2):
        self.cord_x = x
        self.cord_y = y
        self.size_x, self.size_y = (20, 20)
        self.hitbox = pygame.Rect(self.cord_x, self.cord_y, self.size_x, self.size_y)
        self.speed = s
        self.center = self.cord_x+self.size_x/2, self.cord_y+self.size_y/2

    def movement(self):
        pressed = pygame.key.get_pressed()
        up = ((pressed[pygame.K_UP] == 1) or (pressed[pygame.K_w] == 1))
        down = ((pressed[pygame.K_DOWN] == 1) or (pressed[pygame.K_s] == 1))
        right = ((pressed[pygame.K_RIGHT] == 1) or (pressed[pygame.K_d] == 1))
        left = ((pressed[pygame.K_LEFT] == 1) or (pressed[pygame.K_a] == 1))
        self.speed2 = self.speed
        if pressed[pygame.K_SPACE]:
            self.speed2 = self.speed + 2
        if up and down and right and left:
            pass
        elif up and down and right:
            if self.cord_x < WINDOW_X-self.size_x:
                self.cord_x += 1 * self.speed2
        elif up and down and left:
            if self.cord_x > 0:
                self.cord_x -= 1 * self.speed2
        elif left and right and up:
            if self.cord_y > 0:
                self.cord_y -= 1 * self.speed2
        elif left and right and down:
            if self.cord_y < WINDOW_Y-self.size_y:
                self.cord_y += 1 * self.speed2
        elif up and down:
                pass
        elif left and right:
            pass
        elif up and right:
            if self.cord_x < WINDOW_X-self.size_x and self.cord_y > 0:
                self.cord_x += math.cos(math.pi/4) * self.speed2
                self.cord_y -= math.sin(math.pi/4) * self.speed2
            elif self.cord_x < WINDOW_X-self.size_x:
                self.cord_x += math.cos(math.pi/4) * self.speed2
            elif self.cord_y > 0:
                self.cord_y -= math.sin(math.pi/4) * self.speed2
        elif up and left:
            if self.cord_x > 0 and self.cord_y > 0:
                self.cord_x -= math.cos(math.pi/4) * self.speed2
                self.cord_y -= math.sin(math.pi/4) * self.speed2
            elif self.cord_x > 0:
                self.cord_x -= math.sin(math.pi/4) * self.speed2
            elif self.cord_y > 0:
                self.cord_y -= math.sin(math.pi/4) * self.speed2
        elif down and right:
            if self.cord_x < WINDOW_X-self.size_x and self.cord_y < WINDOW_Y-self.size_y:
                self.cord_x += math.cos(math.pi/4) * self.speed2
                self.cord_y += math.sin(math.pi/4) * self.speed2
            elif self.cord_x < WINDOW_X-self.size_x:
                self.cord_x += math.sin(math.pi/4) * self.speed2
            elif self.cord_y < WINDOW_Y-self.size_y:
                self.cord_y += math.sin(math.pi/4) * self.speed2
        elif down and left:
            if self.cord_x > 0 and self.cord_y < WINDOW_Y-self.size_y:
                self.cord_x -= math.cos(math.pi/4) * self.speed2
                self.cord_y += math.sin(math.pi/4) * self.speed2
            elif self.cord_x > 0:
                self.cord_x -= math.sin(math.pi/4) * self.speed2
            elif self.cord_y < WINDOW_Y-self.size_y:
                self.cord_y += math.sin(math.pi / 4) * self.speed2
        elif up:
            if self.cord_y > 0:
                self.cord_y -= 1 * self.speed2
        elif down:
            if self.cord_y < WINDOW_Y-self.size_y:
                self.cord_y += 1 * self.speed2
        elif right:
            if self.cord_x < WINDOW_X-self.size_x:
                self.cord_x += 1 * self.speed2
        elif left:
            if self.cord_x > 0:
                self.cord_x -= 1 * self.speed2
        else:
            pass
        self.update()

    def update(self):
        self.center = self.cord_x + self.size_x / 2, self.cord_y + self.size_y / 2
        self.hitbox = pygame.Rect(self.cord_x, self.cord_y, self.size_x, self.size_y)
        pygame.draw.rect(SCREEN, (255, 0, 255), self.hitbox)
        if DEBUG:
            x, y = self.center
            self.center_box = pygame.Rect(x-2.5, y-2.5, 5, 5)
            pygame.draw.rect(SCREEN, (255, 255, 255), self.center_box)
