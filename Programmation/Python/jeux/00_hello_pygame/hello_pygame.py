"""
Mon premier code pygame
je teste juste une balle qui rebombit et émet du son

Neil BELHADJ
27/11/2022
"""
 
import pygame
from pygame import mixer

import random

# Initialize the game engine
pygame.init()

# Pareil pour le son
mixer.init() 
mixer.music.load('beep.mp3')
mixer.music.set_volume(0.2)


# des couleurs
white = (255, 255, 255)
 
# écran (dimensions et création
size = [800, 600]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Avant Pong")
 
# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()


# infos sur ma balle
# todo : à mettre dans une classe
x = 50
y = 50
r = 10

vx = 20 * random.random();
vy = 20 * random.random();

couleur = (0, 0, 255)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(white)
  
    pygame.draw.circle(screen, couleur, [x, y], r)

    x += vx
    y += vy
    if( (x + r > size[0] and vx > 0) or (x - r < 0 and vx < 0) ):
        vx = -vx;
        couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        mixer.music.play()
    if( (y + r > size[1] and vy > 0) or (y - r < 0 and vy < 0) ):
        vy = -vy;
        couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        mixer.music.play()
    
 
    # update l'écran
    pygame.display.flip()
 
    # met ma vitesse fps.
    clock.tick(100)
 
# fin
pygame.quit()
