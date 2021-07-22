# making the game window

import pygame
import time
import random

pygame.init()    # Initializes all of the imported Pygame modules

# colors
grass = (147, 194, 198)
pink = (253, 177, 150)
yellow = (251, 231, 163)
red = (255, 0, 0)
milk = (255, 253, 246)

# Takes a tuple or a list as its parameter to create a surface
dispW = 600
dispH = 400
disp = pygame.display.set_mode((dispW, dispH))
pygame.display.set_caption("Emo the Worm by Tofu")

clock = pygame.time.Clock()

worm_size = 10
wormSpeed = 10

font_style = pygame.font.SysFont("bahnschrift", 20, False, True)
score_font = pygame.font.SysFont("bahnschrift", 14, False, True)


def disp_score(score):
    value = score_font.render(
        "Your glizzy is  " + str(score) + " inches long!", True, milk)
    disp.blit(value, [0, 0])


def emo_worm(worm_size, worm_list):
    for x in worm_list:
        pygame.draw.circle(disp, pink, [x[0], x[1]], worm_size, 7)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    disp.blit(mesg, [dispW/5.2, dispH/2.2])


def gameLoop():  # the whole game function
    game_over = False
    game_close = False

    x = dispW / 2
    y = dispH / 2

    x_move = 0
    y_move = 0

    worm_list = []
    len_worm = 1

    x_food = round(random.randrange(0, dispW - worm_size) / 10.0) * 10.0
    y_food = round(random.randrange(0, dispH - worm_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            disp.fill(grass)
            message("You're bad Kid! Press Q (Quit) or R (Restart)", milk)
            disp_score(len_worm - 1)
            pygame.display.update()

            for event in pygame.event.get():    # key event to check if you want to quit or restart game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:     # q to quit
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:     # r to restart
                        gameLoop()

        for event in pygame.event.get():  # print out all the action that takes place on screen
            if event.type == pygame.QUIT:  # when click 'X' the screen should close
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -worm_size
                    y_move = 0
                if event.key == pygame.K_RIGHT:
                    x_move = worm_size
                    y_move = 0
                if event.key == pygame.K_UP:
                    x_move = 0
                    y_move = -worm_size
                if event.key == pygame.K_DOWN:
                    x_move = 0
                    y_move = worm_size

        # this is the condition that checks if the worm touches the border then the game ends

        if x >= dispW or x < 0 or y >= dispH or y < 0:
            game_close = True

        x += x_move
        y += y_move
        disp.fill(grass)
        pygame.draw.circle(disp, yellow, [x_food, y_food], worm_size)

        worm_Head = []
        worm_Head.append(x)
        worm_Head.append(y)
        worm_list.append(worm_Head)
        if len(worm_list) > len_worm:
            del worm_list[0]

        for i in worm_list[:-1]:
            if i == worm_Head:
                game_close = True

        emo_worm(worm_size, worm_list)
        disp_score(len_worm - 1)
        pygame.display.update()  # updates changes on the screen

        if x == x_food and y == y_food:
            x_food = round(random.randrange(
                0, dispW - worm_size) / 10.0) * 10.0
            y_food = round(random.randrange(
                0, dispH - worm_size) / 10.0) * 10.0
            len_worm += 1

        clock.tick(wormSpeed)

    pygame.quit()  # closes everything
    quit()


gameLoop()
