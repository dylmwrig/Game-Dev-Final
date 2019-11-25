import pygame

CANVAS_HEIGHT = 600
CANVAS_WIDTH = 800
screen = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))

# loading in sprites should probably happen here??
punch_img = pygame.image.load("assets/punch.png")
chop_img = pygame.image.load("assets/chop.png")
headbutt_img = pygame.image.load("assets/headbutt.png")

# easy enemy formations, use these in the beginning
simpleEnemyFormations = [["", "", "", "Samurai"]]