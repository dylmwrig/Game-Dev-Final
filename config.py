import pygame
import os

# general game stuff
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
RUN_GAME = True
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

FRAME_RATE = 60

playerArea = pygame.Rect((CANVAS_WIDTH / 4) + 70, CANVAS_HEIGHT * 3/8, CANVAS_WIDTH / 3, CANVAS_WIDTH / 4)
playerBorder = pygame.Rect(playerArea.left - 2, playerArea.top - 2, playerArea.width + 4, playerArea.height + 4)
playerInfoBarRect = pygame.Rect(playerArea.left, playerArea.bottom - 60, playerArea.width, 60)
actionTextRect = pygame.Rect(playerArea.left, playerInfoBarRect.top + 1, 40, 40)
playerHealthRect = pygame.Rect(playerArea.right - 101, playerInfoBarRect.top + 1, 100, 15)
playerStamRect = pygame.Rect(playerArea.right - 101, playerBorder.bottom - 32, 100, 15)

cellOne = pygame.Rect(0, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellTwo = pygame.Rect(CANVAS_WIDTH / 2, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellThree = pygame.Rect(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellFour = pygame.Rect(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
quadrants = [cellOne, cellTwo, cellThree, cellFour]

cursor_last_blit = pygame.time.get_ticks()
cursor_drawn = False

#linux
#punch_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/punch.png")
#chop_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/chop.png")
#headbutt_img = pygame.image.load("/home/fuwafuwatime/PycharmProjects/Game-Dev-Final/assets/headbutt.png")

# easy enemy formations, use these in the beginning
simpleEnemyFormations = [["Samurai", "Samurai", "Samurai", "Samurai"]]