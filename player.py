import pygame
import loadAssets as assets

# player class
# equipment is an array which will hold all of the player's powerups
class Player:
    def __init__(self, health, equipment):
        self.health = health
        self.healthColor = (0,255,0)
        self.equipment = equipment

        # action name is displayed; needs to be its own var as headbutt is too long to display
        self.action = "idle"
        self.actionName = "idle"

        # this will be set every time the player takes an action
        self.damage = 0
        self.speed = 10000000
        self.lastAttacked = 0

        self.idleSprites = [assets.player_idle1, assets.player_idle2]

        # icon to display in bottom left of player area
        self.actionIcons = [assets.idle_icon, assets.punch_img, assets.chop_img, assets.headbutt_img,
                            assets.defend_icon]
        self.actionIcons[0] = pygame.transform.scale(self.actionIcons[0], (80,110))
        self.actionIcons[1] = pygame.transform.scale(self.actionIcons[1], (75,70))
        self.actionIcons[2] = pygame.transform.scale(self.actionIcons[2], (100,90))
        self.actionIcons[3] = pygame.transform.scale(self.actionIcons[3], (75,67))
        self.actionIcons[4] = pygame.transform.scale(self.actionIcons[4], (118,93))

        self.actionIcon = self.actionIcons[0]

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
            # idle state entered after an action has completed
            if self.action == "idle":
                self.actionName = "idle"
                self.actionIcon = self.actionIcons[0]

            elif self.action == "defend":
                self.actionName = "defend"
                self.actionIcon = self.actionIcons[4]


            else:
                self.lastAttacked = pygame.time.get_ticks()
                if self.action == "punch":
                    self.actionName = "punch"
                    self.damage = 30
                    self.speed = 2500
                    #self.spriteArr = punchFrames
                    self.actionIcon = self.actionIcons[1]
                if self.action == "chop":
                    self.actionName = "chop"
                    self.damage = 10
                    self.speed = 1000
                    #self.spriteArr = chopFrames
                    self.actionIcon = self.actionIcons[2]
                if self.action == "headbutt":
                    self.actionName = "hedbut"
                    self.actionIcon = self.actionIcons[3]

    def takeDamage(self, dmg):
        self.health -= dmg
        if self.health < 0:
            #TODO GAME OVER
            print("You dead")
        elif self.health < 33:
            self.healthColor = (255,0,0)
        elif self.health < 66:
            self.healthColor = (255,255,0)
        else:
            self.healthColor = (0,255,0)