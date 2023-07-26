import pygame, sys
from pygame.locals import *

pygame.init()


DISPLAYSURFACE = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hello World")

WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render("hello world!", True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

while True:
    DISPLAYSURFACE.fill(WHITE)
    DISPLAYSURFACE.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()