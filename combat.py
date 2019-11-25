import pygame
import spritesheet
import config as cfg
import enemy

# basic fight loop
# enemyFormation is a list of strings representing the enemy formation beginning the fight
# "" represents an empty cell. Ie ("","","","Samurai") indicates one samurai at the bottom right cell of the screen
def beginCombat(enemyFormation):
    ss = spritesheet.spritesheet('playerTemp.png')
    player_image = ss.image_at((50, 10, 35, 35))
    playerX = 370
    playerY = 480

    # four element list holding each enemy
    # first element corresponds to enemy in top left cell, second to top right, and so on
    # empty cells are represented by None and will just be skipped in the combat loop
    enemies = []
    for name in enemyFormation:
        if name == "":
            enemies.append(None)
        else:
            speed = 0.0
            dmg = 0
            sprite = None
            if name == "Samurai":
                speed = 0.75
                dmg = 10
                ss = spritesheet.spritesheet('playerTemp.png')
                sprite = ss.image_at((0,0,15,15))

            enemies.append(enemy.Enemy(name, dmg, speed, 0.0, sprite))

    start_ticks = pygame.time.get_ticks()
    continueFight = True
    while continueFight:
        cfg.screen.fill((160,160,160))
        pygame.draw.line(cfg.screen, (0,0,0), (cfg.CANVAS_WIDTH / 2, 0), (cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT), 10)
        pygame.draw.line(cfg.screen, (0,0,0), (0, cfg.CANVAS_HEIGHT / 2), (cfg.CANVAS_WIDTH, cfg.CANVAS_HEIGHT / 2), 10)

        curTime = pygame.time.get_ticks()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        cfg.screen.blit(player_image, (playerX, playerY))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continueFight = False

        # each enemy starts with lastAttacked = -1.0
        # start their attack cycle once we are in the gaem loop
        # afterwards, check if curTime - lastAttacked >= speed; if it is, update lastAttacked with curTime and attack
        for e in enemies:
            if e.lastAttacked == -1.0:
                e.lastAttacked = curTime
            elif (curTime - e.lastAttacked >= e.speed):
                #TODO ATTACK
                e.lastAttacked = curTime

        pygame.display.update()