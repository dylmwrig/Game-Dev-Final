import pygame
import os

# general game stuff
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
RUN_GAME = True
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

FRAME_RATE = 30

#linux
#punch_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/punch.png")
#chop_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/chop.png")
#headbutt_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/headbutt.png")

# easy enemy formations, use these in the beginning
simpleEnemyFormations = [["", "", "", "Samurai"]]