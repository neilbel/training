"""
Neil Bel Hadj
Fractale de Mandelbrot avec pygame

aidé par le site : https://mathete.net/la-fractale-de-mandelbrot/

pour comprendre le principe et récupérer les transformations pour centrer
sur l'ensemble de Mandelbrot

"""

import sys, pygame, random, math
pygame.init()
 
size = width, height = 320, 240
 
#screen = pygame.display.set_mode(size, pygame.FULLSCREEN, vsync = 1)
screen = pygame.display.set_mode(size, vsync = 1)

max_it = 50

zoom = 1.0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #screen.fill(rgb)
    for y in range(height):
        for x in range(width):
            # valeurs tirées de https://mathete.net/la-fractale-de-mandelbrot/
            cx = zoom * (x * (0.5 - (-2.0)) / width + (-2.0))
            cy = zoom * (y * ((-1.25) - 1.25) / height + 1.25)
            X = cx
            Y = cy
            n = 0
            while (X * X + Y * Y) < 4 and n < max_it:
                pX = X
                X = X * X - Y * Y + cx
                Y = 2 * pX * Y + cy
                n += 1
            #rgb = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            if n == max_it:
                rgb = (0, 0, 100)
            else:
                div = 255.0 / math.sqrt(math.sqrt(n + 1))
                rgb = (div, div, div) 
            screen.set_at((x, y), rgb)
    pygame.display.flip()
    zoom *= 0.99
    print(zoom)
