"""
Neil Bel Hadj
mon premier programme qui dessine des pixels avec pygame
il met des pixels random sur tout l'écran
"""

import sys, pygame, random
pygame.init()
 
size = width, height = 320, 240
 
# le FULLSCREEN ne fonctionne pas toujours très bien
# screen = pygame.display.set_mode(size, pygame.FULLSCREEN, vsync = 1)
screen = pygame.display.set_mode(size, vsync = 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #screen.fill(rgb)
    for y in range(height):
        for x in range(width):
            rgb = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            screen.set_at((x, y), rgb)
    pygame.display.flip()

    
