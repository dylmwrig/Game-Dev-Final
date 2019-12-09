import pygame
import loadAssets as assets
import config as cfg

# player class
# equipment is an array which will hold all of the player's powerups
class Player:
    def __init__(self, equipment):
        self.health = 100
        self.stamina = 100
        self.healthColor = (0,255,0)
        self.equipment = equipment

        # action name is displayed; needs to be its own var as headbutt is too long to display
        self.action = "idle"
        self.actionName = "idle"

        # this will be set every time the player takes an action
        self.damage = 0
        self.speed = 10000000
        self.stamCost = 0
        self.lastAttacked = 0
        self.charLastAnim = pygame.time.get_ticks()

        self.parryStart = 0
        self.riposteStart = 0
        self.parryWindow = 500
        self.riposteWindow = 1000

        self.stamChargeRate = 2000
        self.stamLastCharged = pygame.time.get_ticks()

        self.idleSprites = [assets.player_idle1, assets.player_idle2]

        # change the color behind the player depending on what's happening
        self.bgAlpha = 255
        self.bgColor = (0,0,0)
        self.bgAnimating = False
        self.bgAnimSpeed = 10 # num to subtract from alpha at each step; increase for faster anim

        # icon to display in bottom left of player area
        self.actionIcons = [assets.idle_icon, assets.punch_img, assets.chop_img, assets.headbutt_img,
                            assets.defend_icon, assets.defend_no_stam_icon]
        self.actionIcons[0] = pygame.transform.scale(self.actionIcons[0], (80,110))
        self.actionIcons[1] = pygame.transform.scale(self.actionIcons[1], (75,70))
        self.actionIcons[2] = pygame.transform.scale(self.actionIcons[2], (100,90))
        self.actionIcons[3] = pygame.transform.scale(self.actionIcons[3], (75,67))
        self.actionIcons[4] = pygame.transform.scale(self.actionIcons[4], (118,93))
        self.actionIcons[5] = pygame.transform.scale(self.actionIcons[5], (118,93))

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
        if self.action == actionName:
            # if the player is already defending, go idle, allows for timed parries
            if actionName == "defend":
                self.takeAction("idle")
        else:
            self.action = actionName
            if self.action == "idle":
                self.damage = 0
                self.actionName = "idle"
                self.actionIcon = self.actionIcons[0]

            elif self.action == "defend":
                self.parryStart = pygame.time.get_ticks()
                self.damage = 0
                if self.stamina > 0:
                    self.actionName = "defend"
                    self.actionIcon = self.actionIcons[4]
                    self.bgAlpha = 255
                    self.bgColor = (76,0,153)
                    self.bgAnimating = True
                    self.bgAnimSpeed = 10
                else:
                    self.action = "defendNoStam"
                    self.actionName = "no stam"
                    self.actionIcon = self.actionIcons[5]
            else:
                self.lastAttacked = pygame.time.get_ticks()
                if self.action == "punch":
                    self.actionName = "punch"
                    self.damage = 30
                    self.speed = 2500
                    self.stamCost = 10
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

                if (pygame.time.get_ticks() - self.riposteStart) < self.riposteWindow:
                    self.speed = round(self.speed / 2)

    def takeDamage(self, dmg):
        self.health -= dmg
        print("Player health: " + str(self.health))
        cfg.playerHealthRect.width = self.health
        if self.health < 0:
            #TODO GAME OVER
            print("You dead")
        elif self.health < 33:
            self.healthColor = (255,0,0)
        elif self.health < 66:
            self.healthColor = (255,255,0)
        else:
            self.healthColor = (0,255,0)

    # increase user's stamina
    # this happens every game loop even if the user takes an action/gets hit/etc
    # stamina will increase by a larger amount if meditating
    def increaseStam(self, stam):
        if self.stamina < 100:
            self.stamina += stam
            cfg.playerStamRect.width = self.stamina
            if self.action == "defendNoStam":
                self.action = "defend"
                self.actionIcon = self.actionIcons[4]
                self.actionName = "Defend"
    # check if the user has run out of stam whenever stam is reduced
    # for displaying icons and such
    # do nothing if the user's stamina is already 0
    def reduceStam(self, stam):
        if self.stamina > 0:
            self.stamina -= stam
            cfg.playerStamRect.width = self.stamina
            if self.stamina <= 0:
                if self.action == "defend":
                    self.action = "defendNoStam"
                    self.actionIcon = self.actionIcons[5]
                    self.actionName = "no stam"