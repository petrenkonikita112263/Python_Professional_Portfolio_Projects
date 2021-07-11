import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick

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

# same with ball
ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195

# list than contains all sprites for game, add paddle to this list
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddle)
all_sprites_list.add(ball)

all_bricks_list = pygame.sprite.Group()
for i in range(7):
    brick = Brick(RED, 80, 30)
    brick.rect.x = 60 + i * 300
    brick.rect.y = 60
    all_sprites_list.add(brick)
    all_bricks_list.add(brick)
for i in range(7):
    brick = Brick(ORANGE, 80, 30)
    brick.rect.x = 60 + i * 300
    brick.rect.y = 100
    all_sprites_list.add(brick)
    all_bricks_list.add(brick)
for i in range(7):
    brick = Brick(YELLOW, 80, 30)
    brick.rect.x = 60 + i * 300
    brick.rect.y = 140
    all_sprites_list.add(brick)
    all_bricks_list.add(brick)

game_is_on = True
clock = pygame.time.Clock()

while game_is_on:
    for event in pygame.event.get():
        # condition for quit
        if event.type == pygame.QUIT:
            game_is_on = False

    # move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddle.move_right(5)

    # main logic of the game
    all_sprites_list.update()
    ball.update_position()

    # ball can bounce out of 4 walls(right, left, top and bottom)
    if ball.rect.x >= 790:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 590:
        ball.velocity[1] = -ball.velocity[1]
        # lose the live when ball hits bottom wall of screen(not paddle)
        lives -= 1
        if lives == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("GAME OVER", 1, WHITE)
            screen.blit(text, (250, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            game_is_on = False
    if ball.rect.y < 40:
        ball.velocity[1] = -ball.velocity[1]

    # collision detection with paddle
    if pygame.sprite.collide_mask(ball, paddle):
        ball.rect.x -= ball.velocity[0]
        ball.rect.y -= ball.velocity[1]
        ball.bounce()

    # collision with bricks, destroying the brick will increment the score
    brick_collision_list = pygame.sprite.spritecollide(ball, all_bricks_list, False)
    for brick in brick_collision_list:
        ball.bounce()
        score += 1
        brick.kill()
        if len(all_bricks_list) == 0:
            font = pygame.font.Font(None, 74)
            text = font.render("LEVEL COMPLETE", 1, WHITE)
            screen.blit(text, (200, 300))
            pygame.display.flip()
            pygame.time.wait(3000)
            game_is_on = False

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
