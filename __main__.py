import pygame
import random
import math
import user

from config import *
import Dott

running = True
i = 0

pygame.init()

user = user.Player(200, 200, s=4)
dott = Dott.Dott(300, 300, (255, 0, 0), t_s=10, s=3, d=100)
#dott2 = Dott.Dott(300, 100, (255, 255, 0), t_s=15, s=4, d=150)
#dott3 = Dott.Dott(400, 100, (0, 0, 255), t_s=15, s=4, d=150)
#dott4 = Dott.Dott(500, 100, (0, 255, 0), t_s=15, s=4, d=150)

foc = 0.0
while 1:
    i += 1
    CLOCK.tick(FRAMERATE)
    SCREEN.fill((255, 255, 200))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_0]:
        foc += 1.0/60
    if keys[pygame.K_1]:
        foc -= 1.0/60

    user.movement()
    dott.search(user)
    #dott2.search(dott)
    #dott3.search(dott2)
    #dott4.search(dott3)
    SCREEN.blit(pygame.font.SysFont("monospace", 16).render(str(dott.found), 1, (0, 0, 0)), (WINDOW_X/2-20, 5*WINDOW_Y/6))

    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    if not running:
        break
