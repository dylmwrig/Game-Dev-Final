import pygame

# player class
# equipment is an array which will hold all of the player's powerups
class Player:
    def __init__(self, health, equipment):
        self.health = health
        self.eqipment = equipment
        self.action = "idle"

        # this will be set every time the player takes an action
        self.damage = 0
        self.speed = 10000000
        self.lastAttacked = 0
    # for each string in the equipment array, alter the player's stats
    # call this when combat starts
    # should be cleaner than directly buffing stats, allows for more flexibility
    # def equip():

    def takeAction(self, actionName):
        self.action = actionName
        if (self.action == "punch"):
            self.damage = 50
            self.speed = 4000
            self.lastAttacked = pygame.time.get_ticks()