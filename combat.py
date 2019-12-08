import pygame
import spritesheet
import loadAssets as assets
import config as cfg
import player as player_class
import enemy as enemy_class

#def playerTakeAction(action):

CURSOR_BLIT_SPEED = 300
CHAR_ANIM_SPEED = 600

# four element list holding each enemy
# first element corresponds to enemy in top left cell, second to top right, and so on
# empty cells are represented by None and will just be skipped in the combat loop
def createEnemies(enemyFormation):
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
                speed = 1500
                dmg = 15
                health = 100
                #ss = spritesheet.spritesheet('enemyTemp.png')
                #sprite = ss.image_at((0,0,15,30))
                sprite = assets.headbutt_img
                sprite = pygame.transform.scale(sprite, (75, 100))
            # adjust the enemy's location based on it's image
            # so it's location will be centered to the center of the actual sprite
            x -= sprite.get_rect().width / 2
            y -= sprite.get_rect().height / 2

            enemies.append(enemy_class.Enemy(name, health, x, y, dmg, speed, -1.0, sprite))
    return enemies

# basic fight loop
# enemyFormation is a list of strings representing the enemy formation beginning the fight
# "" represents an empty cell. Ie ("","","","Samurai") indicates one samurai at the bottom right cell of the screen
def beginCombat(enemyFormation):
    pygame.init()

    #ss = spritesheet.spritesheet('playerTemp.png')
    #player_image = ss.image_at((50, 10, 35, 35))
    playerX = 370
    playerY = 480

    player = player_class.Player(100, 0)
    enemies = createEnemies(enemyFormation)

    cellOne = pygame.Rect(0, 0, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellTwo = pygame.Rect(cfg.CANVAS_WIDTH / 2, 0, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellThree = pygame.Rect(0, cfg.CANVAS_HEIGHT / 2, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    cellFour = pygame.Rect(cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2, cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT / 2)
    quadrants = [cellOne, cellTwo, cellThree, cellFour]
    selector_img = assets.selector_img
    selector_img = pygame.transform.scale(selector_img, (cellOne.width, cellOne.height))

    playerArea = pygame.Rect((cfg.CANVAS_WIDTH / 4) + 70, cfg.CANVAS_HEIGHT * 3/8, cfg.CANVAS_WIDTH / 3, cfg.CANVAS_WIDTH / 4)
    playerBorder = pygame.Rect(playerArea.left - 2, playerArea.top - 2, playerArea.width + 4, playerArea.height + 4)
    playerInfoBarRect = pygame.Rect(playerArea.left, playerArea.bottom - 60, playerArea.width, 60)
    actionTextRect = pygame.Rect(playerArea.left, playerInfoBarRect.top + 1, 40, 40)
    playerHealthRect = pygame.Rect(playerArea.right - 101, playerInfoBarRect.top + 1, 100, 15)
    playerStamRect = pygame.Rect(playerArea.right - 101, playerBorder.bottom - 32, 100, 15)
    actionIconRect = pygame.Rect(playerHealthRect.left - player.actionIcon.get_rect().width + 4,
                                 playerArea.bottom - player.actionIcon.get_rect().height + 30, 40, 40)

    start_ticks = pygame.time.get_ticks()
    cursor_last_blit = start_ticks
    cursor_drawn = False
    charLastAnim = start_ticks

    continueFight = True
    cfg.screen.fill((160,160,160))

    # selectedCell represents where the player is currently targeting
    # 0 represents top left, 1 is top right, 2 is bottom left, 3 is bottom right
    selectedCell = 0
    while continueFight:
        curTime = pygame.time.get_ticks()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        cfg.screen.fill((255,255,255))

        pygame.draw.line(cfg.screen, (0,0,0), (cfg.CANVAS_WIDTH / 2, 0), (cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT), 10)
        pygame.draw.line(cfg.screen, (0,0,0), (0, cfg.CANVAS_HEIGHT / 2), (cfg.CANVAS_WIDTH, cfg.CANVAS_HEIGHT / 2), 10)

        # display targeting reticle
        if (curTime - cursor_last_blit) > CURSOR_BLIT_SPEED:
            if not cursor_drawn:
                cursor_last_blit = pygame.time.get_ticks()
                cursor_drawn = True
            else:
                cursor_last_blit = pygame.time.get_ticks()
                cursor_drawn = False

        if cursor_drawn:
            cfg.screen.blit(selector_img, quadrants[selectedCell])
        cfg.screen.fill((0, 0, 0), playerBorder)
        cfg.screen.fill((255, 255, 255), playerArea)
        cfg.screen.blit(player.sprite, (playerArea.left + 40, playerArea.top - 15))

        if (curTime - charLastAnim) > CHAR_ANIM_SPEED:
            charLastAnim = pygame.time.get_ticks()
            player.updateSprite()
        pygame.draw.rect(cfg.screen,(0,0,0),playerInfoBarRect)
        if player.action == "idle":
            cfg.screen.blit(player.actionIcon, actionIconRect)
        elif player.action == "punch":
            cfg.screen.blit(player.actionIcon, (actionIconRect.left, actionIconRect.top + 20))
        elif player.action == "chop":
            cfg.screen.blit(player.actionIcon, (actionIconRect.left, actionIconRect.top))
        elif player.action == "headbutt":
            cfg.screen.blit(player.actionIcon, (actionIconRect.left, actionIconRect.top + 20))

        pygame.draw.rect(cfg.screen,player.healthColor,playerHealthRect)
        pygame.draw.rect(cfg.screen,(255,255,0),playerStamRect)

        actionText = assets.actionFont.render('Action', False, (255,255,255))
        cfg.screen.blit(actionText,actionTextRect)
        actionText = assets.actionFont.render(player.actionName, False, (255,255,255))
        cfg.screen.blit(actionText,(actionTextRect.left, actionTextRect.bottom - 5))
        hpText = assets.stamHealthFont.render('Health', False, (255,255,255))
        cfg.screen.blit(hpText,(playerHealthRect.left, playerHealthRect.bottom - 4))
        stamText = assets.stamHealthFont.render('Stamina', False, (255,255,255))
        cfg.screen.blit(stamText,(playerStamRect.left, playerStamRect.bottom - 4))

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

                if event.key == pygame.K_a:
                    player.takeAction("punch")
                elif event.key == pygame.K_s:
                    player.takeAction("chop")
                elif event.key == pygame.K_d:
                    player.takeAction("headbutt")
                elif event.key == pygame.K_SPACE:
                    player.takeAction("defend")

        # player actions
        if (curTime - player.lastAttacked) > player.speed:
            if enemies[selectedCell] is not None:
                enemies[selectedCell].health -= player.damage
                print(enemies[selectedCell].name)
                print(enemies[selectedCell].health)
                if enemies[selectedCell].health <= 0:
                    enemies[selectedCell] = None
            else:
                print("Whiff!")
            player.lastAttacked = pygame.time.get_ticks()

        # each enemy starts with lastAttacked = -1.0
        # start their attack cycle once we are in the game loop
        # afterwards, check if curTime - lastAttacked >= speed; if it is, update lastAttacked with curTime and attack
        for i, e in enumerate(enemies):
            if e is not None:
                if e.lastAttacked == -1.0:
                    e.lastAttacked = curTime
                elif curTime - e.lastAttacked >= e.speed:
                    e.lastAttacked = curTime
                    if player.action == "blocking":
                        print("blocked!")
                    else:
                        player.health -= e.damage
                cfg.screen.blit(e.sprite, (e.xPos, e.yPos))

        pygame.time.Clock().tick(cfg.FRAME_RATE)
        pygame.display.update()