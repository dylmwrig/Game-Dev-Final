# constructor vars are mostly self explanatory
# speed is a float representing how many seconds it takes for an attack
# lastAttacked is a float; update whenever the enemy attacks
class Enemy:
    def __init__(self, name, health, xPos, yPos, damage, speed, startAttackTime, idleSprites, attackSprite, windupSprite):
        self.name = name
        self.health = health
        self.xPos = xPos
        self.yPos = yPos
        self.damage = damage
        self.speed = speed
        self.startAttackTime = startAttackTime
        self.lastAttacked = -1
        self.sprite = idleSprites[0]
        self.idleSprites = idleSprites
        self.attackSprite = attackSprite
        self.idleIndex = 0
        self.lastAnim = 0
        self.windupSprite = windupSprite
        self.windUpAnim = False

        # keeps track of the attack animation
        # -1 means the enemy is not attacking
        self.attackAnimTime = -1