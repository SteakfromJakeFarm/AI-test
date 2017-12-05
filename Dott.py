import pygame
import math

from config import *


class Dott:
    def __init__(self, x=0, y=0, c=(0, 0, 0), t_d=1, t_s=1, s=1, d=2):
        self.turn_direction = t_d
        self.distance = d
        self.turn_speed = t_s
        self.cord_x = x
        self.cord_y = y
        self.size_x = 20
        self.size_y = 20
        self.center = self.cord_x+self.size_x/2, self.cord_y+self.size_y/2
        self.hitbox = pygame.Rect(self.cord_x, self.cord_y, self.size_x, self.size_y)
        self.speed = s
        self.color = c
        self.focus = 0  # Direction it is looking
        self.view = View(self.cord_x, self.cord_y, self.focus, d)
        self.found = False

    def update(self, f=""):
        if not f == "":
            self.focus = f
        self.hitbox = pygame.Rect(self.cord_x, self.cord_y, self.size_x, self.size_y)
        pygame.draw.rect(SCREEN, self.color, self.hitbox, 0)
        self.view.update(self.cord_x, self.cord_y, self.focus)

    def search(self, goal):
        self.found = False
        for point in self.view.points_list:
            if goal.hitbox.collidepoint(point):
                self.movement()
                self.found = True
                cx, cy = goal.center
                try:
                    angle_needed = math.atan2(cx-(self.cord_x+10), cy-(self.cord_y+10))
                except ZeroDivisionError:
                    angle_needed = math.pi/2
                #print(angle_needed)
                self.focus = angle_needed
                break
        if not self.found:
            self.focus += (self.turn_speed*1.0/FRAMERATE)*self.turn_direction
        self.update()

    def movement(self):
        self.center = self.cord_x+self.size_x/2, self.cord_y+self.size_y/2
        self.cord_x += math.sin(self.focus) * self.speed
        self.cord_y += math.cos(self.focus) * self.speed
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(self.cord_x+9, self.cord_y+9, 2, 2))


class View:
    def __init__(self, x, y, f, d):
        self.cord_x = x+10
        self.cord_y = y+10
        self.color = (0, 0, 0)
        self.thickness = 4
        self.length = d
        self.view_x = math.sin(f) * self.length
        self.view_y = math.cos(f) * self.length
        self.points_list = []

    def update(self, x, y, f):
        self.cord_x = x+10
        self.cord_y = y+10
        self.view_x = math.sin(f) * self.length
        self.view_y = math.cos(f) * self.length
        self.points_list = []

        for i in range(0, 500, 1):
            self.points_list.append((math.sin(f) * (i*self.length/500.0) + self.cord_x,
                                     math.cos(f) * (i*self.length/500.0) + self.cord_y))

        if DEBUG:
            pygame.draw.lines(SCREEN, self.color, False,
                              [(self.cord_x, self.cord_y),
                               (self.cord_x + self.view_x, self.cord_y + self.view_y)],
                              self.thickness)
