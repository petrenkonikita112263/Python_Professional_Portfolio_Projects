import pygame
from paddle import Paddle

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

# create and position the paddle
paddle = Paddle(WHITE, 100, 10)
paddle.rect.x = 350
paddle.rect.y = 560

# list than contains all sprites for game, add paddle to this list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)

game_is_on = True
clock = pygame.time.Clock()

while game_is_on:
    for event in pygame.event.get():
        # condition for quit
        if event.type == pygame.QUIT:
            game_is_on = False

    # main logic of the game
    all_sprites_list.update()

    # customize display
    screen.fill(DARK_BLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    score_text = font.render(f"Your Score: {score}", 1, WHITE)
    screen.blit(score_text, (20, 10))
    lives_text = font.render(f"Lives left: {lives}", 1, WHITE)
    screen.blit(lives_text, (650, 10))

    # draw all sprites
    all_sprites_list.draw(screen)

    # update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
