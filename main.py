import pygame
import combat
import config as cfg
import loadAssets as assets

# game handler

def main():
    pygame.init()
    # title and icon
    pygame.display.set_caption("Kung Fu Escape")
    titleRect = pygame.Rect(round(cfg.CANVAS_WIDTH / 4), 50, 100, 50)
    titleText = assets.menuTitleFont.render("Kung Fu Escape", False, (255,255,255))
    options = ["EASY", "MEDIUM", "HARD"]
    menuSelection = 0

    # main loop
    while cfg.RUN_GAME:
        cfg.screen.fill((0,0,0))
        cfg.screen.blit(titleText, titleRect)

        for i,option in enumerate(options):
            if i == menuSelection:
                color = (255,0,0)
            else:
                color = (255, 255, 255)
            text = assets.menuOptionsFont.render(option, False, color)
            cfg.screen.blit(text, ((titleRect.right / 2), titleRect.bottom + ((i + 1) * 50)))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cfg.RUN_GAME = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    combat.beginCombat(options[menuSelection])
                if event.key == pygame.K_UP:
                    if menuSelection == 0:
                        menuSelection = len(options) - 1
                    else:
                        menuSelection -= 1
                if event.key == pygame.K_DOWN:
                    if menuSelection == len(options) - 1:
                        menuSelection = 0
                    else:
                        menuSelection += 1

        pygame.display.update()

if __name__ == "__main__":
    main()