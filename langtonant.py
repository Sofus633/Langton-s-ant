import pygame
import pygame.gfxdraw
import math
import time 

mat = [[[0] for i in range(1000)] for i in range(1000)]
states = {}
screen = pygame.display.set_mode((1000, 1000))
ant_p = [100, 100]
angle = 0
while True:
    pygame.event.poll()
    pygame.gfxdraw.pixel(screen, *ant_p, (255, 255, 122))
    print(states)
    print(int(round(math.cos(angle))),  int(round(math.sin(angle))), angle)
    ant_p[0] += int(round(math.cos(math.radians(angle))))
    ant_p[1] += int(round(math.sin(math.radians(angle))))
    
    if states.get(tuple(ant_p)) is None:
        states[tuple(ant_p)] = False
        
    if states[tuple(ant_p)]:
        angle -= 90 
    if not states[tuple(ant_p)] :
        angle += 90 
    states[tuple(ant_p)] = not states[tuple(ant_p)]
            
    for key in states:
        if states[tuple(key)] == True:
            pygame.gfxdraw.pixel(screen, *key, (122, 255, 122))

    pygame.display.flip()
    screen.fill(0)