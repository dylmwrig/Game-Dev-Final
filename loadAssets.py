from pathlib import Path
import pygame
import config as cfg

pygame.font.init()

# load in sprites from a separate file
# allows for windows and python development without directory conflicts

cur_dir = Path.cwd()

punch_icon = pygame.image.load(str(cur_dir/'assets'/'punch.png'))
chop_icon = pygame.image.load(str(cur_dir/'assets'/'chop.png'))
headbutt_icon = pygame.image.load(str(cur_dir/'assets'/'headbutt.png'))
idle_icon = pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'idle_icon.png'))
defend_icon = pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'defend.png'))
defend_no_stam_icon = pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'defendNoStam.png'))

selector_img = pygame.image.load(str(cur_dir/'assets'/'selector.png'))
selector_img = pygame.transform.scale(selector_img, (cfg.quadrants[0].width, cfg.quadrants[0].height))

player_sprites = []
player_sprites.append(pygame.image.load(str(cur_dir/'assets'/'Player'/'player-idle1.png')))
player_sprites.append(pygame.image.load(str(cur_dir/'assets'/'Player'/'player-idle2.png')))
player_sprites.append(pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'punch.png')))
player_sprites.append(pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'chop.png')))

for i,img in enumerate(player_sprites):
    player_sprites[i] = pygame.transform.scale(player_sprites[i], (round(cfg.CANVAS_WIDTH / 4), round(cfg.CANVAS_HEIGHT / 4)))
player_idle1 = player_sprites[0]
player_idle2 = player_sprites[1]
player_punch = player_sprites[2]
player_chop = player_sprites[3]
player_headbutt = pygame.image.load(str(cur_dir/'assets'/'Player'/'actions'/'headbutt.png'))
player_headbutt =  pygame.transform.scale(player_headbutt, (round(cfg.CANVAS_WIDTH / 4), round(cfg.CANVAS_HEIGHT / 4)))

enemySprites = []
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'samurai1.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'samurai2.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'samuraiAttack.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'oni1.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'oni2.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'oniAttack.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'oniWindup.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'ninja1.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'ninja2.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'ninjaAttack.png')))
enemySprites.append(pygame.image.load(str(cur_dir/'assets'/'Enemies'/'ninjaWindup.png')))

for i,img in enumerate(enemySprites):
    img = pygame.transform.scale(img, (180, 180))
    enemySprites[i] = img

samurai_sprite_idle1 = enemySprites[0]
samurai_sprite_idle2 = enemySprites[1]
samurai_sprite_attack = enemySprites[2]
oni_sprite_idle1 = enemySprites[3]
oni_sprite_idle2 = enemySprites[4]
oni_sprite_attack = enemySprites[5]
oni_sprite_windup = enemySprites[6]
ninja_sprite_idle1 = enemySprites[7]
ninja_sprite_idle2 = enemySprites[8]
ninja_sprite_attack = enemySprites[9]
ninja_sprite_windup = enemySprites[10]

menuTitleFont = pygame.font.Font(str(cur_dir/'assets'/'Fonts'/'ARCADECLASSIC.TTF'), 60)
menuOptionsFont = pygame.font.Font(str(cur_dir/'assets'/'Fonts'/'ARCADECLASSIC.TTF'), 40)
actionFont = pygame.font.Font(str(cur_dir/'assets'/'Fonts'/'ARCADECLASSIC.TTF'), 27)
stamHealthFont = pygame.font.Font(str(cur_dir/'assets'/'Fonts'/'ARCADECLASSIC.TTF'), 20)