# Importamos la librería pygame
import pygame
import random

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la ventana
pygame.display.set_caption("Surface")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400,400))

# Definimos un color
azul = (random.randint(0, 255))
rojo = (random.randint(0, 255))
verde = (random.randint(0, 255))
color_aleatorio = (rojo, verde, azul)

# Crear una superficie 
color_aleatorio_superficie = pygame.Surface((200,200))

# Rellenamos la superficie de azul
color_aleatorio_superficie.fill(color_aleatorio)

# Inserto o muevo la superficie en la ventana
ventana.blit(color_aleatorio_superficie, ((100,100)))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()