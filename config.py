import pygame

FRAMERATE = 60
DEBUG = False

WINDOW_X = 600
WINDOW_Y = 600

SCREEN = pygame.display.set_mode((WINDOW_X, WINDOW_Y))  # Create screen on the display
CLOCK = pygame.time.Clock()  # Create the clock object. Useful for implementing the framerate
