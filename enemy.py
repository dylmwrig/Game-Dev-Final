# constructor vars are mostly self explanatory
# speed is a float representing how many seconds it takes for an attack
# lastAttacked is a float; update whenever the enemy attacks
# sprite is already extracted from the sprite sheet
class Enemy:
    def __init__(self, name, damage, speed, lastAttacked, sprite):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.lastAttacked = lastAttacked
        self.sprite = sprite