# constructor vars are mostly self explanatory
# speed is a float representing how many seconds it takes for an attack
# lastAttacked is a float; update whenever the enemy attacks
class Enemy:
    def __init__(self, name, health, xPos, yPos, damage, speed, sprite, idleSprites, attackSprite):
        self.name = name
        self.health = health
        self.xPos = xPos
        self.yPos = yPos
        self.damage = damage
        self.speed = speed
        self.lastAttacked = -1
        self.sprite = sprite
        self.idleSprites = idleSprites
        self.attackSprite = attackSprite
        self.idleIndex = 0
        self.lastAnim = 0

        # keeps track of the attack animation
        # -1 means the enemy is not attacking
        self.attackAnimTime = -1