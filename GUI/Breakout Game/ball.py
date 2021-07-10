from random import randint

import pygame
from pygame.sprite import Sprite

BLACK = (0, 0, 0)


class Ball(Sprite):
    """Represent the ball, inheritances from Sprite class in pygame."""

    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        # but it will be small square point
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update_position(self):
        """Ball is moving, so it changes the position"""
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        """Ball hits the paddle and bounce back"""
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
