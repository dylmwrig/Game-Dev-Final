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
    while cfg.RUN_GAME:
        cfg.screen.fill((0,0,0))
        enemyFormation = random.choice(cfg.simpleEnemyFormations)
        combat.beginCombat(enemyFormation)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.RUN_GAME = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    print("pepeLaugh")

if __name__ == "__main__":
    main()