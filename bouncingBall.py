import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

BOTTOM = (260,180)
TOP = (260,30)
SPEED = [1, 1]
size = width, height = 640, 360
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#IMAGES
icn = pygame.image.load("icnball.png")
ball = pygame.image.load("Red-Ball.png")
back = pygame.image.load("ck.jpg")
ball = pygame.transform.scale(ball, (100,80))


#DISPLAY
DISPLAYSURFACE = pygame.display.set_mode((size))
pygame.display.set_caption("Ball Game")
pygame.display.set_icon(icn)

ballrect = ball.get_rect()

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(SPEED)
    if ballrect.left < 0 or ballrect.right > width:
        SPEED[0] = -SPEED[0]
    if ballrect.top < 0 or ballrect.bottom  > 260:
        SPEED[1] = -SPEED[1]
    
    DISPLAYSURFACE.blit(back,(0, 0))
    DISPLAYSURFACE.blit(ball, ballrect)
    pygame.display.update()
    dt = clock.tick(60)
