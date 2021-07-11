import pygame
from pygame.sprite import Sprite

BLACK = (0, 0, 0)


class Brick(Sprite):
    """Represent the brick, inheritances from Sprite class in pygame."""

    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
