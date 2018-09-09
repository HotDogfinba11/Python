import random
import pygame
import sys
from pygame import *

pygame.init()
fps = pygame.time.Clock()


white = (255, 255, 255)
orange = (255,140,0)
green = (0, 255, 0)
black = (0, 0, 0)


width = 800
height = 400
balrad = 20
padwid = 8
padheig = 80
halfpadwid = padwid // 2
halfpadheig = padheig // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
gameIcon = pygame.image.load('pong.png')
pygame.display.set_icon(gameIcon)


def ball_init(right):
    global ball_pos, ball_vel
    ball_pos = [width // 2, height // 2]
    horz = random.randrange(2, 4)
    vert = random.randrange(1, 3)

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]


def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, l_score, r_score  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [halfpadwid - 1, height // 2]
    paddle2_pos = [width + 1 - halfpadwid, height //2]
    l_score = 0
    r_score = 0
    if random.randrange(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)


def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score

    canvas.fill(black)
    pygame.draw.line(canvas, white, [width // 2, 0], [width // 2, height], 1)
    pygame.draw.line(canvas, white, [padwid, 0], [padwid, height], 1)
    pygame.draw.line(canvas, white, [width - padwid, 0], [width - padwid, height], 1)


    if paddle1_pos[1] > halfpadheig and paddle1_pos[1] < height - halfpadheig:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == halfpadheig and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == height - halfpadheig and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] > halfpadheig and paddle2_pos[1] < height - halfpadheig:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == halfpadheig and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == height - halfpadheig and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel


    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])


    pygame.draw.circle(canvas, white, ball_pos, 20, 0)
    pygame.draw.polygon(canvas, white, [[paddle1_pos[0] - halfpadwid, paddle1_pos[1] - halfpadheig],
                                        [paddle1_pos[0] - halfpadwid, paddle1_pos[1] + halfpadheig],
                                        [paddle1_pos[0] + halfpadwid, paddle1_pos[1] + halfpadheig],
                                        [paddle1_pos[0] + halfpadwid, paddle1_pos[1] - halfpadheig]], 0)
    pygame.draw.polygon(canvas, white, [[paddle2_pos[0] - halfpadwid, paddle2_pos[1] - halfpadheig],
                                        [paddle2_pos[0] - halfpadwid, paddle2_pos[1] + halfpadheig],
                                        [paddle2_pos[0] + halfpadwid, paddle2_pos[1] + halfpadheig],
                                        [paddle2_pos[0] + halfpadwid, paddle2_pos[1] - halfpadheig]], 0)


    if int(ball_pos[1]) <= balrad:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= height + 1 - balrad:
        ball_vel[1] = -ball_vel[1]


    if int(ball_pos[0]) <= balrad + padwid and int(ball_pos[1]) in range(paddle1_pos[1] - halfpadheig,
                                                                                 paddle1_pos[1] + halfpadheig, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) <= balrad + padwid:
        r_score += 1
        ball_init(True)

    if int(ball_pos[0]) >= width + 1 - balrad - padwid and int(ball_pos[1]) in range(
            paddle2_pos[1] - halfpadheig, paddle2_pos[1] + halfpadheig, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.1
        ball_vel[1] *= 1.1
    elif int(ball_pos[0]) >= width + 1 - balrad - padwid:
        l_score += 1
        ball_init(False)


    myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
    label1 = myfont1.render("Score " + str(l_score), 1, (white))
    canvas.blit(label1, (50, 20))

    myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
    label2 = myfont2.render("Score " + str(r_score), 1, (white))
    canvas.blit(label2, (680, 20))


def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8


def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0


init()

  

while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

            
    pygame.display.update()
    fps.tick(60)
