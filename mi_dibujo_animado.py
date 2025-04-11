import pygame
import sys
import math

blanco = (255,255,255)
rosado = (255,192,203)
negro = (0,0,0)
gris_claro = (185, 185, 185)
gris_oscuro = (139, 139, 139)
gris_m_oscuro = (113, 112, 112)
gris_m_claro =  (217, 217, 217)
rosado_c =(238, 156, 156)
PI = math.pi

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Lineas Aleatorias")

clock = pygame.time.Clock()

###########################
# Bucle principal del juego
###########################
while 1:
    clock.tick(50)

    # Ciclo para la detención de los eventos del juego
    for event in pygame.event.get():
        # Si se hace click sobre el botón de cerrar la ventana, el juego termina
        if event.type == pygame.QUIT:
            sys.exit()

    # Rellenar la venntana del color
    ventana.fill(rosado)

    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto_1 = fuente_arial.render("Colegio San José De Guanentá", 1, negro)
    texto_2 = fuente_arial.render("Especialidad Sistemas", 1, negro)
    texto_3 = fuente_arial.render("Mariangel Duque", 1, negro)
    ventana.blit(texto_1,(70,5))
    ventana.blit(texto_2,(120,40))
    ventana.blit(texto_3,(150,470))

    # tren 
    pygame.draw.rect(ventana, blanco, (20,80, 458,380))
    pygame.draw.rect(ventana, gris_oscuro, (118,260, 15,130))
    pygame.draw.rect(ventana, rosado_c, (130,250, 250,150))
    pygame.draw.rect(ventana, gris_oscuro, (80,242, 40,164))
    pygame.draw.rect(ventana, gris_oscuro, (145,198, 40,53))
    pygame.draw.rect(ventana, gris_oscuro, (134,175, 63,25))
    pygame.draw.rect(ventana, gris_oscuro, (225,150, 140,100))
    pygame.draw.rect(ventana, gris_m_claro, (243,165, 105,70))
    pygame.draw.rect(ventana, gris_m_oscuro, (215,120, 160,30))
    pygame.draw.rect(ventana, gris_m_oscuro, (225,105, 140,15))


    pygame.display.flip()