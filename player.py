import pygame
import loadAssets as assets

# player class
# equipment is an array which will hold all of the player's powerups
class Player:
    def __init__(self, health, equipment):
        self.health = health
        self.healthColor = (0,255,0)
        self.equipment = equipment
        self.action = "idle"

        # this will be set every time the player takes an action
        self.damage = 0
        self.speed = 10000000
        self.lastAttacked = 0

        self.idleSprites = [assets.player_idle1, assets.player_idle2]

        self.sprite = assets.player_idle1
        self.spriteArr = self.idleSprites
        self.animIndex = 0
    # for each string in the equipment array, alter the player's stats
    # call this when combat starts
    # should be cleaner than directly buffing stats, allows for more flexibility
    # def equip():

    def updateSprite(self):
        if self.animIndex + 1 >= len(self.spriteArr):
            self.animIndex = 0
        else:
            self.animIndex += 1
        self.sprite = self.spriteArr[self.animIndex]

    def takeAction(self, actionName):
        if self.action != actionName:
            self.action = actionName
            if self.action == "punch":
                self.damage = 30
                self.speed = 2500
                self.lastAttacked = pygame.time.get_ticks()
                #self.spriteArr = punchFrames
            if self.action == "chop":
                self.damage = 10
                self.speed = 1000
                self.lastAttacked = pygame.time.get_ticks()
                #self.spriteArr = chopFrames

    def takeAction(self):
        if self.health < 33:
            self.healthColor = (255,0,0)
        elif self.health < 66:
            self.healthColor = (255,255,0)
        else:
            self.healthColor = (0,255,0)