import pygame
from pygame.sprite import Sprite

BLACK = (0, 0, 0)


class Paddle(Sprite):
    """Represent the paddle, inheritances from Sprite class in pygame."""

    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        # fetch rectangle that has the dimensions of the image
        self.rect = self.image.get_rect()
