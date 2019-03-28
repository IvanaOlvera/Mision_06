# Autor: Ivana Olvera Mérida
# Dibujar un espirógrafo utilizando ecuaciones paramétricas

import pygame
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800

AZUL = (0, 0, 255)
MORADO = (166, 0, 255)
NARANJA = (255, 97, 0)
VERDE = (124, 255, 0)
BLANCO = (255, 255, 255)


def dibujarEspirografo(r, R, l):
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(BLANCO)

        radio = 100
        for angulo in range(0, r // math.gcd(r, R) * 360, 1):
            a = math.radians(angulo)
            k = r / R
            x = int(R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) / k * a)))
            y = int(R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) / k * a)))
            pygame.draw.circle(ventana, NARANJA, (x + ANCHO // 2, ALTO // 2 - y), 1)


        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    r = int(input("Radio menor: "))
    R = int(input("Radio mayor: "))
    l = float(input("Valor de l: "))
    espirografo = dibujarEspirografo(r, R, l)


main()
