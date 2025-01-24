import pygame
from config import *
from classlevel import level

#init
pygame.init()
clock = pygame.time.Clock()

#open window
displaysurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("race under time")


level = level(displaysurface)

aregamerunning = True
while aregamerunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            aregamerunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                aregamerunning = False
    
    level.run()

    pygame.display.flip()
    clock.tick(60)

#close pygame
pygame.quit()