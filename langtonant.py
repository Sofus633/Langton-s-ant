import pygame
import pygame.gfxdraw
import math
import time 
import random
mat = [[[0] for i in range(1000)] for i in range(1000)]
states = {}
screen = pygame.display.set_mode((1000, 1000))
ants = [[200, 150, 0], [800, 200, 0]]
for i in range(20):
    ants.append([random.randint(0, 800),random.randint(0, 800) ,random.randint(0, 800)])
while True:
    pygame.event.poll()
    pygame.gfxdraw.pixel(screen, ants[0][0], ants[0][1], (255, 255, 122))

    print(states)
    for i in range(len(ants)):

        ants[i][0] += int(round(math.cos(math.radians(ants[i][2]))))
        ants[i][1] += int(round(math.sin(math.radians(ants[i][2]))))
    
        if states.get(tuple([ants[i][0], ants[i][1]])) is None:
            states[tuple([ants[i][0], ants[i][1]])] = False
        
        if states[tuple([ants[i][0], ants[i][1]])]:
            ants[i][2] -= 90 
        if not states[tuple([ants[i][0], ants[i][1]])]:
            ants[i][2] += 90 
        states[tuple([ants[i][0], ants[i][1]])] = not states[tuple([ants[i][0], ants[i][1]])]
            
    for key in states:
        if states[tuple(key)] == True:
            pygame.gfxdraw.pixel(screen, *key, (122, 255, 122))

    pygame.display.flip()
    screen.fill(0)
