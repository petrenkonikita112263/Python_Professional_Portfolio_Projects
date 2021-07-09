import pygame

pygame.init()

# COLOR CONSTANTS
WHITE = (255, 255, 255)
DARK_BLUE = (36, 90, 190)
LIGHT_BLUE = (0, 176, 240)
RED = (255, 0, 0)
ORANGE = (255, 100, 0)
YELLOW = (255, 255, 0)

# game parameters
score = 0
lives = 3
size = (800, 600)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
