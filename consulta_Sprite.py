# Para entender la clase Sprite, debemos de entender primero el modulo sprite.
# pygame.sprite : es un módulo dentro de Pygame diseñado para facilitar la gestión de objetos en movimiento, conocidos como sprites, en un juego. Hace más fácil manejar muchos objetos.
# clase Sprite: Un Sprite es cualquier objeto del juego que puede moverse.

# pygame.sprite.Sprite: es la clase base para cualquier objeto individual que quieras manejar como sprite. 
# ejemplos: pygame.sprite.Sprite.update, pygame.sprite.Sprite.add, pygame.sprite.Sprite.remove.

# Ahora vamos a usar pygame.sprite.Group, que es una herramienta súper útil cuando estás manejando muchos sprites. Te permite actualizarlos, dibujarlos y detectar colisiones entre ellos de forma más organizada.
# pygame.sprite.Group: una clase contenedora para almacenar y administrar múltiples objetos Sprite.

import pygame
import random
import sys

pygame.init()

ANCHO, ALTO = 640, 480
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atrapa la moneda")

AZUL = (0, 0, 255)
DORADO = (255, 215, 0)
BLANCO = (255, 255, 255)
NEGRO = (0,0,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(AZUL)
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:  self.rect.x -= 5
        if teclas[pygame.K_RIGHT]: self.rect.x += 5
        if teclas[pygame.K_UP]:    self.rect.y -= 5
        if teclas[pygame.K_DOWN]:  self.rect.y += 5

        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > ANCHO: self.rect.right = ANCHO
        if self.rect.top < 0: self.rect.top = 0
        if self.rect.bottom > ALTO: self.rect.bottom = ALTO

class Moneda(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(DORADO)
        self.rect = self.image.get_rect()
        self.nueva_posicion()

    def nueva_posicion(self):
        self.rect.x = random.randint(0, ANCHO - 30)
        self.rect.y = random.randint(0, ALTO - 30)

jugador = Jugador()
moneda = Moneda()

sprites = pygame.sprite.Group()
sprites.add(jugador)
sprites.add(moneda)

puntos = 0
fuente = pygame.font.SysFont(None, 36)

tiempo = 30  # 30 segundos
fuente_tiempo = pygame.font.SysFont(None, 48)

reloj = pygame.time.Clock()
jugando = True

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Actualizar sprites
    sprites.update()

    # Comprobar colisión
    if pygame.sprite.collide_rect(jugador, moneda):
        puntos += 1
        moneda.nueva_posicion()

    tiempo -= 1 / 60  # 1/60 por cada frame (60 FPS)
    if tiempo <= 0:
        jugando = False  # Terminar el juego cuando el tiempo se acaba

    # Dibujar todo
    pantalla.fill(BLANCO)
    sprites.draw(pantalla)

    # Mostrar puntuación
    texto = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pantalla.fill(BLANCO)
texto_final = fuente.render(f"¡Juego Terminado! Puntos: {puntos}", True, NEGRO)
pantalla.blit(texto_final, (ANCHO // 2 - 150, ALTO // 2 - 20))
pygame.display.flip()

pygame.time.wait(3000)

pygame.quit()
sys.exit()