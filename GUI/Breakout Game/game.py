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

game_is_on = True
clock = pygame.time.Clock()

while game_is_on:
    for event in pygame.event.get():
        # condition for quit
        if event.type == pygame.QUIT:
            game_is_on = False

    # main logic of the game

    # customize display
    screen.fill(DARK_BLUE)
    pygame.draw.line(screen, WHITE, [0, 38], [800, 38], 2)
    font = pygame.font.Font(None, 34)
    score_text = font.render(f"Your Score: {score}", 1, WHITE)
    screen.blit(score_text, (20, 10))
    lives_text = font.render(f"Lives left: {lives}", 1, WHITE)
    screen.blit(lives_text, (650, 10))

    # update display
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
