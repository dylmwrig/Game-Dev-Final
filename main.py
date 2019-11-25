import random
import pygame
import spritesheet
import combat
import config as cfg

# game handler

def main():
    pygame.init()

    # title and icon
    pygame.display.set_caption("Kung Fu Escape")

    # main loop
    keepGoing = True
    while keepGoing:
        cfg.screen.fill((0,0,0))
        enemyFormation = random.choice(cfg.enemyFormations)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    combat.beginCombat(enemyFormation)

if __name__ == "__main__":
    main()