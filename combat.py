import pygame
import spritesheet
import config as cfg
import enemy

# basic fight loop
# enemyFormation is a list of strings representing the enemy formation beginning the fight
# "" represents an empty cell. Ie ("","","","Samurai") indicates one samurai at the bottom right cell of the screen
def beginCombat(enemyFormation):
    #ss = spritesheet.spritesheet('playerTemp.png')
    #player_image = ss.image_at((50, 10, 35, 35))
    playerX = 370
    playerY = 480

    # four element list holding each enemy
    # first element corresponds to enemy in top left cell, second to top right, and so on
    # empty cells are represented by None and will just be skipped in the combat loop
    enemies = []
    for i, name in enumerate(enemyFormation):
        if name == "":
            enemies.append(None)
        else:
            speed = 0.0
            dmg = 0
            sprite = None
            if i == 0:
                x = cfg.CANVAS_WIDTH / 4
                y = cfg.CANVAS_HEIGHT / 4
            elif i == 1:
                x = cfg.CANVAS_WIDTH * (3/4)
                y = cfg.CANVAS_HEIGHT / 4
            elif i == 2:
                x = cfg.CANVAS_WIDTH / 4
                y = cfg.CANVAS_HEIGHT * (3/4)
            else:
                x = cfg.CANVAS_WIDTH * (3/4)
                y = cfg.CANVAS_HEIGHT * (3/4)

            if name == "Samurai":
                speed = 0.75
                dmg = 10
                #ss = spritesheet.spritesheet('enemyTemp.png')
                #sprite = ss.image_at((0,0,15,30))
                sprite = cfg.headbutt_img
                sprite = pygame.transform.scale(sprite, (75, 100))
            # adjust the enemy's location based on it's image
            # so it's location will be centered to the center of the actual sprite
            x -= sprite.get_rect().width / 2
            y -= sprite.get_rect().height / 2

            enemies.append(enemy.Enemy(name, x, y, dmg, speed, -1.0, sprite))

    player_action =

    CURSOR_BLIT_SPEED = 300
    cellOne = pygame.Rect(0, 0, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellTwo = pygame.Rect(cfg.CANVAS_WIDTH / 2, 0, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellThree = pygame.Rect(0, cfg.CANVAS_HEIGHT / 2, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellFour = pygame.Rect(cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    quadrants = [cellOne, cellTwo, cellThree, cellFour]

    start_ticks = pygame.time.get_ticks()
    cursor_last_blit = start_ticks
    cursor_drawn = False

    continueFight = True
    cfg.screen.fill((160,160,160))

    # selectedCell represents where the player is currently targeting
    # 0 represents top left, 1 is top right, 2 is bottom left, 3 is bottom right
    selectedCell = 0
    while continueFight:
        curTime = pygame.time.get_ticks()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        cfg.screen.fill((255,255,255));

        # display targeting reticle
        if ((curTime - cursor_last_blit) > CURSOR_BLIT_SPEED):
            print("curTime: " + str(curTime))
            print("last blit: " + str(cursor_last_blit))
            print("blit speed: " + str(CURSOR_BLIT_SPEED))
            if (not cursor_drawn):
                cursor_last_blit = pygame.time.get_ticks()
                cursor_drawn = True
            else:
                cursor_last_blit = pygame.time.get_ticks()
                cursor_drawn = False

#        print(quadrants[selectedCell].topleft)
#        print(quadrants[selectedCell].topright)
#        print(quadrants[selectedCell].bottomleft)
#        print(quadrants[selectedCell].bottomright)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continueFight = False
                cfg.RUN_GAME = False

            # cell targeting selection by the player
            # if the player moves towards the edge, wrap
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if selectedCell == 0 or selectedCell == 2:
                        selectedCell += 1
                    else:
                        selectedCell -= 1
                elif event.key == pygame.K_LEFT:
                    if selectedCell == 1 or selectedCell == 3:
                        selectedCell -= 1
                    else:
                        selectedCell += 1
                elif event.key == pygame.K_DOWN:
                    if selectedCell == 0 or selectedCell == 1:
                        selectedCell += 2
                    else:
                        selectedCell -= 2
                elif event.key == pygame.K_UP:
                    if selectedCell == 2 or selectedCell == 3:
                        selectedCell -= 2
                    else:
                        selectedCell += 2

        if (cursor_drawn):
            cfg.screen.blit(cfg.punch_img, quadrants[selectedCell])

        # each enemy starts with lastAttacked = -1.0
        # start their attack cycle once we are in the gaem loop
        # afterwards, check if curTime - lastAttacked >= speed; if it is, update lastAttacked with curTime and attack
        for i, e in enumerate(enemies):
            if e != None:
                if e.lastAttacked == -1.0:
                    e.lastAttacked = curTime
                elif (curTime - e.lastAttacked >= e.speed):
                    #TODO ATTACK
                    e.lastAttacked = curTime

                cfg.screen.blit(e.sprite, (e.xPos, e.yPos))

        pygame.draw.line(cfg.screen, (0,0,0), (cfg.CANVAS_WIDTH / 2, 0), (cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT), 10)
        pygame.draw.line(cfg.screen, (0,0,0), (0, cfg.CANVAS_HEIGHT / 2), (cfg.CANVAS_WIDTH, cfg.CANVAS_HEIGHT / 2), 10)

        pygame.display.update()