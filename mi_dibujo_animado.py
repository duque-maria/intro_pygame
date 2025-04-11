import pygame
import sys
import math

blanco = (255,255,255)
rosado = (255,192,203)
negro = (0,0,0)
rojo = (255,0,0)
gris_claro = (185, 185, 185)
gris_oscuro = (139, 139, 139)
gris_m_oscuro = (113, 112, 112)
gris_m_claro =  (217, 217, 217)
negro = (0,0,0)
rosado_c =(238, 156, 156)
piel = (255, 210, 132)
cafe = (156, 117, 50)
lila = (227, 156, 238)
morado = (193, 0, 222)
PI = math.pi

pygame.init()

ventana = pygame.display.set_mode((500,500))

pygame.display.set_caption("Veloznina")

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
    texto_4 = fuente_arial.render("Veloznina", 2, morado)
    ventana.blit(texto_1,(70,5))
    ventana.blit(texto_2,(120,40))
    ventana.blit(texto_3,(150,470))

    # tren 
    pygame.draw.rect(ventana, blanco, (20,80, 458,380))
    # trompa
    pygame.draw.circle(ventana, lila, (100, 325), 68)
    # parte pequeña de al lado
    pygame.draw.rect(ventana, gris_oscuro, (118,260, 15,130))
    # parte grande
    pygame.draw.rect(ventana, rosado_c, (130,250, 250,150))
    # nombre
    ventana.blit(texto_4,(200,310))
    # parte de al lado de la pequeña
    pygame.draw.rect(ventana, morado, (80,242, 40,164))
    # chimenea
    pygame.draw.rect(ventana, morado, (145,198, 40,53))
    pygame.draw.rect(ventana, gris_oscuro, (134,175, 63,25))
    # Cuadrado pequeño grande
    pygame.draw.rect(ventana, lila, (225,150, 140,100))
    # cuadrado de adentro
    pygame.draw.rect(ventana, rosado_c, (243,165, 105,70))
    # parte de arriba
    pygame.draw.rect(ventana, morado, (215,120, 160,30))
    pygame.draw.rect(ventana, gris_m_oscuro, (225,105, 140,15))
    # llanta izquierda
    pygame.draw.circle(ventana, negro, (175, 400), 35)
    # llanta del centro
    pygame.draw.circle(ventana, negro, (270, 400), 35)
    # llanta derecha
    pygame.draw.circle(ventana, negro, (365, 400), 35)
    # lineas que unen las llantas
    pygame.draw.line(ventana, gris_m_oscuro, (190,400), (255,400), 20)
    pygame.draw.line(ventana, gris_m_oscuro, (290,400), (355,400), 20)
    # cara (rostro)
    pygame.draw.circle(ventana, piel, (295,200), 40)
    # cejas
    pygame.draw.line(ventana, negro, (270,180), (290,195), 4)
    pygame.draw.line(ventana, negro, (320,180), (300,195), 4)
    # ojo izquierdo
    pygame.draw.circle(ventana, blanco, (275, 205), 13)
    # ojo  derecho
    pygame.draw.circle(ventana, blanco, (315, 205), 13)
    # pupila izquierda
    pygame.draw.circle(ventana, cafe, (275, 205), 5)
    # pupila derecha
    pygame.draw.circle(ventana, cafe, (315, 205), 5)
    # boca
    mostrar_boca = pygame.draw.circle(ventana, rojo, (295, 225), 10)
    if mostrar_boca:
            pygame.draw.circle(ventana, rojo, (295, 225), 10)
    else:
           pygame.draw.line(ventana, rojo, (280,225), (310,225), 2)
    

    pygame.display.flip()