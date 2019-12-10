import pygame
import loadAssets as assets
import config as cfg
import player as player_class
import enemy as enemy_class

#def playerTakeAction(action):

CURSOR_BLIT_SPEED = 300
CHAR_ANIM_SPEED = 600

player = player_class.Player(0)

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
                speed = 2300
                dmg = 7
                health = 100
                sprite = assets.samurai_sprite_idle1
                sprite = pygame.transform.scale(sprite, (75, 100))
                idleSprites = [assets.samurai_sprite_idle1, assets.samurai_sprite_idle2]
                attackSprite = assets.samurai_sprite_attack
                windupSprite = assets.oni_sprite_windup
            elif name == "Ninja":
                speed = 1800
                dmg = 3
                health = 100
                sprite = assets.ninja_sprite_idle1
                idleSprites = [assets.ninja_sprite_idle1, assets.ninja_sprite_idle2]
                attackSprite = assets.ninja_sprite_attack
                windupSprite = idleSprites[1] # ninja is so fast he doesn't need a wind up
            elif name == "Oni":
                speed = 2800
                dmg = 10
                health = 100
                sprite = assets.oni_sprite_idle1
                idleSprites = [assets.oni_sprite_idle1, assets.oni_sprite_idle2]
                attackSprite = assets.oni_sprite_attack
                windupSprite = assets.oni_sprite_windup

            # adjust the enemy's location based on it's image
            # so it's location will be centered to the center of the actual sprite
            #x -= sprite.get_rect().width / 2
            x -= 65
            y -= 90

            print(str(x) + " " + str(y))
            enemies.append(enemy_class.Enemy(name, health, x, y, dmg, speed, sprite, idleSprites, attackSprite, windupSprite))
    return enemies

def drawScreen(selectedCell, enemies):
    cfg.screen.fill((255, 255, 255))

    pygame.draw.line(cfg.screen, (0, 0, 0), (cfg.CANVAS_WIDTH / 2, 0), (cfg.CANVAS_WIDTH / 2, cfg.CANVAS_HEIGHT), 10)
    pygame.draw.line(cfg.screen, (0, 0, 0), (0, cfg.CANVAS_HEIGHT / 2), (cfg.CANVAS_WIDTH, cfg.CANVAS_HEIGHT / 2), 10)

    actionIconRect = pygame.Rect(cfg.playerHealthRect.left - player.actionIcon.get_rect().width + 4,
                                 cfg.playerArea.bottom - player.actionIcon.get_rect().height + 30, 40, 40)

    curTime = pygame.time.get_ticks()
    # display targeting reticle
    if (curTime - cfg.cursor_last_blit) > CURSOR_BLIT_SPEED:
        if not cfg.cursor_drawn:
            cfg.cursor_last_blit = pygame.time.get_ticks()
            cfg.cursor_drawn = True
        else:
            cfg.cursor_last_blit = pygame.time.get_ticks()
            cfg.cursor_drawn = False

    if not player.bgAnimating:
        cfg.screen.fill((0, 0, 0), cfg.playerBorder)
        cfg.screen.fill((255, 255, 255), cfg.playerArea)

    else:
        playerBackground = pygame.Surface((cfg.playerArea.width, cfg.playerArea.height))
        playerBackground.fill(player.bgColor)
        cfg.screen.fill((0, 0, 0), cfg.playerBorder)
        cfg.screen.fill((255, 255, 255), cfg.playerArea)
        if player.bgAlpha > 0:
            playerBackground.set_alpha(player.bgAlpha)
            cfg.screen.blit(playerBackground, (cfg.playerArea.left, cfg.playerArea.top))
            player.bgAlpha -= player.bgAnimSpeed
        else:
            player.bgAlpha = 255
            player.bgColor = (255,255,255)
            player.bgAnimating = False

    if cfg.cursor_drawn:
        cfg.screen.blit(assets.selector_img, cfg.quadrants[selectedCell])
    cfg.screen.blit(player.sprite, (cfg.playerArea.left + 40, cfg.playerArea.top - 15))

    if not player.curAnimating:
        if (curTime - player.charLastAnim) > CHAR_ANIM_SPEED:
            player.charLastAnim = pygame.time.get_ticks()
            player.updateSprite()
    elif (curTime - player.startAnim) > 500:
        player.curAnimating = False

    pygame.draw.rect(cfg.screen, (0, 0, 0), cfg.playerInfoBarRect)
    if player.action == "idle":
        cfg.screen.blit(player.actionIcon, actionIconRect)
    elif player.action == "punch":
        cfg.screen.blit(player.actionIcon, (actionIconRect.left - 5, actionIconRect.top - 20))
    elif player.action == "chop":
        cfg.screen.blit(player.actionIcon, (actionIconRect.left + 23, actionIconRect.top - 20))
    elif player.action == "headbutt":
        cfg.screen.blit(player.actionIcon, (actionIconRect.left - 5, actionIconRect.top - 22))
    elif player.action == "defend" or player.action == "defendNoStam":
        cfg.screen.blit(player.actionIcon, (actionIconRect.left + 10, actionIconRect.top + 5))

    if cfg.playerHealthRect.width > 0:
        pygame.draw.rect(cfg.screen, player.healthColor, cfg.playerHealthRect)
    if cfg.playerStamRect.width > 0:
        pygame.draw.rect(cfg.screen, (255, 255, 0), cfg.playerStamRect)

    actionText = assets.actionFont.render('Action', False, (255, 255, 255))
    cfg.screen.blit(actionText, cfg.actionTextRect)
    actionText = assets.actionFont.render(player.actionName, False, (255, 255, 255))
    cfg.screen.blit(actionText, (cfg.actionTextRect.left, cfg.actionTextRect.bottom - 5))
    hpText = assets.stamHealthFont.render('Health', False, (255, 255, 255))
    cfg.screen.blit(hpText, (cfg.playerHealthRect.left, cfg.playerHealthRect.bottom - 4))
    stamText = assets.stamHealthFont.render('Stamina', False, (255, 255, 255))
    cfg.screen.blit(stamText, (cfg.playerStamRect.left, cfg.playerStamRect.bottom - 4))

    for e in enemies:
        if e is not None:
            if e.attackAnimTime != -1:
                # attack sprite will linger on screen for 500ms for now
                # longer if I introduce some character based recovery time system
                if (curTime - e.attackAnimTime) <= 500:
                    e.sprite = e.attackSprite
                # attack animation has completed
                else:
                    e.attackAnimTime = -1

            elif e.windUpAnim:
                e.sprite = e.windupSprite

            elif (curTime - e.lastAnim) > CHAR_ANIM_SPEED:
                e.idleIndex = (e.idleIndex + 1) % 2
                e.sprite = e.idleSprites[e.idleIndex]
                e.lastAnim = curTime
            cfg.screen.blit(e.sprite, (e.xPos, e.yPos))

            healthRect = pygame.Rect(e.xPos + 10, e.yPos + e.sprite.get_rect().height + 5, e.health, 10)
            healthColor = (0,255,0)
            if e.health < 33:
                healthColor = (255,0,0)
            elif e.health < 66:
                healthColor = (255, 255, 0)
            pygame.draw.rect(cfg.screen, healthColor, healthRect)

# basic fight loop
# enemyFormation is a list of strings representing the enemy formation beginning the fight
# "" represents an empty cell. Ie ("","","","Samurai") indicates one samurai at the bottom right cell of the screen
def beginCombat(enemyFormation):
    pygame.init()

    enemies = createEnemies(enemyFormation)
    start_ticks = pygame.time.get_ticks()

    continueFight = True

    # selectedCell represents where the player is currently targeting
    # 0 represents top left, 1 is top right, 2 is bottom left, 3 is bottom right
    selectedCell = 0
    while continueFight:
        curTime = pygame.time.get_ticks()
        #seconds = (pygame.time.get_ticks() - start_ticks) / 1000

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

                if event.key == pygame.K_SPACE:
                    player.takeAction("defend")
                elif event.key == pygame.K_a:
                    player.takeAction("punch")
                elif event.key == pygame.K_s:
                    player.takeAction("chop")
                elif event.key == pygame.K_d:
                    player.takeAction("headbutt")
                #elif event.key == pygame.K_q:
                #    player.takeAction("meditate")
                # allows the player to go in and out of defense for parries
                elif event.key == pygame.K_SPACE:
                    player.takeAction("defend")

        # player actions
        if (curTime - player.lastAttacked) > player.speed:
            if player.damage > 0:
                print(player.action)
                player.curAnimating = True
                player.startAnim = pygame.time.get_ticks()
                if player.action == "punch":
                    player.sprite = assets.player_punch
                elif player.action == "chop":
                    player.sprite = assets.player_chop
                elif player.action == "headbutt":
                    player.sprite = assets.player_headbutt
                    enemies[selectedCell].lastAttacked = pygame.time.get_ticks()
                if enemies[selectedCell] is not None:
                    enemies[selectedCell].health -= player.damage
                    if enemies[selectedCell].health <= 0:
                       enemies[selectedCell] = None
                else:
                    print("Whiff!")
                player.lastAttacked = pygame.time.get_ticks()
                player.reduceStam(player.stamCost)
                player.takeAction("idle")

        # recharge player stamina
        if (curTime - player.stamLastCharged) > player.stamChargeRate:
            player.stamLastCharged = curTime
            if player.action == "meditating":
                print("Meditating")
            else:
                player.increaseStam(5)

        # each enemy starts with lastAttacked = -1.0
        # start their attack cycle once we are in the game loop
        # afterwards, check if curTime - lastAttacked >= speed; if it is, update lastAttacked with curTime and attack
        for i, e in enumerate(enemies):
            if e is not None:
                if e.lastAttacked == -1.0:
                    e.lastAttacked = curTime
                elif curTime - e.lastAttacked >= e.speed:
                    e.windUpAnim = False
                    e.lastAttacked = curTime
                    e.attackAnimTime = curTime
                    # if the player is blocking and out of stamina, they take full damage
                    # otherwise they will take stamina damage
                    if player.action == "defend":
                        if player.stamina > 0:
                            player.reduceStam(e.damage)
                            # player hit their parry, give them a second long riposte window
                            if (curTime - player.parryStart) <= player.parryWindow:
                                player.riposteStart = pygame.time.get_ticks()
                                player.bgAlpha = 255
                                player.bgColor = (255,0,0)
                                player.bgAnimating = True
                                player.bgAnimSpeed = 5
                        else:
                            player.takeDamage(e.damage)
                    else:
                        player.takeDamage(e.damage)
                elif curTime - e.lastAttacked + 500 >= e.speed:
                    e.windUpAnim = True

        pygame.time.Clock().tick(cfg.FRAME_RATE)
        pygame.display.update()
        drawScreen(selectedCell, enemies)