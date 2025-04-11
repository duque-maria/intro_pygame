import pygame
import sys
import random

blanco = (255,255,255)
rosado = (255,192,203)
negro = (0,0,0)

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

    pygame.draw.rect(ventana, blanco, (50,80, 400,380))

    for i in range(100):

     m_1 = random.randint(50,450)
     m_2 = random.randint(80,450)
     m_3 = random.randint(50,450)
     m_4 = random.randint(80,450)
     color_aleatorio = ((random.randint(1,254)), (random.randint(1,254)), (random.randint(1,254)))
     i = pygame.draw.line(ventana, color_aleatorio,(m_1,m_2), (m_3,m_4))
     print(f" {i}")


     pygame.display.flip()