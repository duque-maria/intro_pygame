import pygame
import sys
import random

rojo = (255,0,0)
turquesa = (62, 243, 161)
morado = (169, 62, 243)
rosita = (242, 65, 119 )
marron = (125, 29, 25 )
verde = (54, 242, 22)

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Los cuadrados")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 4
YY = 300 

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(turquesa)
    
    XX = XX + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -4
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 4
    
    pygame.draw.rect(ventana, rojo, (XX, 0, 50, 50))
    pygame.draw.rect(ventana, rosita, (XX, 450, 50, 50))

    YY = YY + MOVIMIENTO

    if YY >= 450:
        YY = 450
        MOVIMIENTO = -4
    elif YY <= 0:
        YY = 0
        MOVIMIENTO = 4

    pygame.draw.rect(ventana, morado, (0, YY, 50, 50))
    pygame.draw.rect(ventana, marron, (450, YY, 50, 50))
    color_aleatorio = ((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255)))
    pygame.draw.rect(ventana, color_aleatorio,(200, 200, 100, 100))
    pygame.draw.rect(ventana, verde, (XX, YY, 50, 50))
    pygame.display.flip()