import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Kung Fu Escape")


# main loop
keepGoing = True
while keepGoing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepGoing = False

    screen.fill((0,0,0))


    pygame.display.update()