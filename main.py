import random
import pygame
import combat
import config as cfg

# game handler

def main():
    pygame.init()

    # title and icon
    pygame.display.set_caption("Kung Fu Escape")

    # something andy is showing us in pygame
    # called "sprite groups", look into it
    #boxes = []
    #for colorName in pygame.color.THECOLORS:
        #boxes.append(Square(pygame.color.Color(colorName)))
    #allSprites = pygame.sprite.Group(boxes)

    # in main loop
    # dirty rect updating
    # rather than redrawing the entire screen when a sprite moves
    # you can simply update the stuff that moved ie the "dirty" part

    #allSprites.clear(screen, background) #background is an "unpolluted" background image stored in the beginning
    #allSprites.update()
    #allSprites.draw(screen)

    # this allows you to check for collision between one sprite and an entire group
    # setting the third param to true makes it delete the element
    #pygame.sprite.spritecollide(circle, squareGroup, False);

    # main loop
    while cfg.RUN_GAME:
        cfg.screen.fill((0,0,0))
        enemyFormation = random.choice(cfg.simpleEnemyFormations)
        combat.beginCombat(enemyFormation)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.RUN_GAME = False

if __name__ == "__main__":
    main()