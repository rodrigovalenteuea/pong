import pygame
from pygame.locals import *
from sys import exit


pygame.init()


COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

SCORE_MAX = 2


largura = 1280
altura = 720

size = (largura, altura)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("MyPong - PyGame Edition - 2023-12-12")

# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 90)
score_text = score_font.render('0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (275, 90)

# score text
score_text2 = score_font.render('0', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect2 = score_text2.get_rect()
score_text_rect2.center = (915, 90)

# ball
ball = pygame.image.load("assets/ball.png")
ball_x = 640
ball_y = 360
ball_dx = 7
ball_dy = 7

'''
# score text
score_font = pygame.font.Font('assets/PressStart2P.ttf', 44)
score_text = score_font.render('00 x 00', True, COLOR_WHITE, COLOR_BLACK)
score_text_rect = score_text.get_rect()
score_text_rect.center = (680, 50)'''

# victory text
victory_font = pygame.font.Font('assets/PressStart2P.ttf', 100)
victory_text = victory_font .render('VICTORY', True, COLOR_WHITE, COLOR_BLACK)
victory_text_rect = score_text.get_rect()
victory_text_rect.center = (450, 350)

# sound effects
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')


class Player:
    def __int__(self, position_x, position_y, moving_down, moving_up, speed_y, score):
        self.position_x = position_x
        self.position_y = position_y
        self.moving_down = moving_down
        self.moving_up = moving_up
        self.speed_y = speed_y
        self.score = score


player_1_img = pygame.image.load("assets/player.png")
player_1 = Player()
player_1.position_x = 50
player_1.position_y = 300
player_1.moving_up = False
player_1.moving_down = False
player_1.speed_y = 1
player_1.score = 0

player_2_img = pygame.image.load("assets/player.png")
player_2 = Player()
player_2.position_x = 1180
player_2.position_y = 300
player_2.moving_up = False
player_2.moving_down = False
player_2.speed_y = 10
player_2.score = 0


# game loop
game_loop = True
game_clock = pygame.time.Clock()

while game_loop:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                player_1.moving_up = True
            if event.key == K_UP:
                player_2.moving_up = True

            if event.key == K_s:
                player_1.moving_down = True
            if event.key == K_DOWN:
                player_2.moving_down = True

        if event.type == KEYUP:
            if event.key == K_w:
                player_1.moving_up = False
            if event.key == K_UP:
                player_2.moving_up = False
            if event.key == K_s:
                player_1.moving_down = False
            if event.key == K_DOWN:
                player_2.moving_down = False

    # checking the victory condition
    if player_1.score < SCORE_MAX and player_2.score < SCORE_MAX:

        screen.fill(COLOR_BLACK)

        # ball collision with the wall
        if ball_y > 700:
            ball_dy *= -1
            bounce_sound_effect.play()
        elif ball_y <= 0:
            ball_dy *= -1
            bounce_sound_effect.play()

        if ball_x > 1260:
            ball_dx *= -1
            bounce_sound_effect.play()
        elif ball_x <= 0:
            ball_dx *= -1
            bounce_sound_effect.play()

        if player_1.moving_up:
            player_1.position_y -= 15
        if player_1.moving_down:
            player_1.position_y += 15

        if player_2.moving_up:
            player_2.position_y -= 15
        if player_2.moving_down:
            player_2.position_y += 15

        if player_1.position_y <= 0:
            player_1.position_y = 0

        if player_1.position_y >= 720:
            player_1.position_y = 650

        # ball movement
        ball_x = ball_x + ball_dx
        ball_y = ball_y + ball_dy

        # update score hud
        score_text = score_font.render(str(player_1.score), True, COLOR_WHITE, COLOR_BLACK)
        score_text2 = score_font.render(str(player_2.score), True, COLOR_WHITE, COLOR_BLACK)

        screen.blit(ball, (ball_x, ball_y))
        screen.blit(score_text, score_text_rect)
        screen.blit(score_text2, score_text_rect2)
        screen.blit(player_1_img, (player_1.position_x, player_1.position_y))
        screen.blit(player_2_img, (player_2.position_x, player_2.position_y))

    pygame.display.flip()
    game_clock.tick(60)

