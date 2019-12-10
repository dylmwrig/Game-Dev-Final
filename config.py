import pygame
import os

# general game stuff
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
RUN_GAME = True
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

FRAME_RATE = 60

playerArea = pygame.Rect((CANVAS_WIDTH / 4) + 70, CANVAS_HEIGHT * 3/8, CANVAS_WIDTH / 3, CANVAS_WIDTH / 4)
playerInfoBarRect = pygame.Rect(playerArea.left, playerArea.bottom - 60, playerArea.width, 60)
actionTextRect = pygame.Rect(playerArea.left, playerInfoBarRect.top + 1, 40, 40)
playerHealthRect = pygame.Rect(playerArea.right - 101, playerInfoBarRect.top + 1, 100, 15)

generalInfoArea = pygame.Rect(playerArea.left, playerArea.top - (CANVAS_HEIGHT / 4), playerArea.width, CANVAS_HEIGHT / 4)
waveNumArea = pygame.Rect(generalInfoArea.left, generalInfoArea.top, generalInfoArea.width, generalInfoArea.height / 4)
wavesLeftArea = pygame.Rect(generalInfoArea.left, waveNumArea.bottom, generalInfoArea.width, generalInfoArea.height / 4)
killCountArea = pygame.Rect(generalInfoArea.left, wavesLeftArea.bottom, generalInfoArea.width, generalInfoArea.height / 4)
waveCompleteArea = pygame.Rect(generalInfoArea.left, killCountArea.bottom, generalInfoArea.width, generalInfoArea.height / 4)

playerBorder = pygame.Rect(playerArea.left - 2, generalInfoArea.top - 2, playerArea.width + 4, playerArea.height + generalInfoArea.height + 4)
playerStamRect = pygame.Rect(playerArea.right - 101, playerBorder.bottom - 32, 100, 15)

cellOne = pygame.Rect(0, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellTwo = pygame.Rect(CANVAS_WIDTH / 2, 0, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellThree = pygame.Rect(0, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
cellFour = pygame.Rect(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2)
quadrants = [cellOne, cellTwo, cellThree, cellFour]

cursor_last_blit = pygame.time.get_ticks()
cursor_drawn = False

# easy enemy formations, use these in the beginning
startingFormations = [["Samurai", "", "", "Ninja"],
                         ["", "Oni", "", "Samurai"],
                         ["Ninja", "", "Oni", ""],
                         ["","Oni","Samurai",""]]

# each list represents all reinforcements for a given wave
# ie respawnWaves [1] contains all reinforcements for wave 2
# elements selected from list randomly so ordering doesn't matter
respawnWaves = [[],#["Samurai", "Oni", "Ninja"],
                []]