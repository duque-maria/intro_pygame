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
amarillo = (255, 252, 0)

# Crear una superficie 
amarillo_superficie = pygame.Surface((200,400))

# Rellenamos la superficie de azul
amarillo_superficie.fill(amarillo)

# Inserto o muevo la superficie en la ventana
ventana.blit(amarillo_superficie, ((0,0)))

# Definimos un color
azul = (0, 53, 255)

# Crear una superficie 
azul_superficie = pygame.Surface((400,200))

# Rellenamos la superficie de azul
azul_superficie.fill(azul)

# Inserto o muevo la superficie en la ventana
ventana.blit(azul_superficie, ((0,200)))

## Definimos un color
amarillo = (255, 252, 0)

# Crear una superficie 
amarillo_superficie = pygame.Surface((400,200))

# Rellenamos la superficie de azul
amarillo_superficie.fill(amarillo)

# Inserto o muevo la superficie en la ventana
ventana.blit(amarillo_superficie, ((0,0)))

# Definimos un color
rojo = (255, 0, 0)

# Crear una superficie 
rojo_superficie = pygame.Surface((400,200))

# Rellenamos la superficie de rojo
rojo_superficie.fill(rojo)

# Inserto o muevo la superficie en la ventana
ventana.blit(rojo_superficie, ((0,300)))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

pygame.quit()