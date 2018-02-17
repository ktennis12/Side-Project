Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> """
Multiple Arrows

Description: What it sounds like 
"""

import pygame

pygame.init()

window = pygame.display.set_mode([500, 500])

arrow_x = 0
arrow_y = 3
index = 0

moving = True
while moving:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                moving = False

        space_b = tsk.Sprite("AlienSpace.jpg", 0, 0)
        space_b.draw()
        #window.fill((255, 255, 255))
        #arrow = pygame.draw.line(window, (100, 100, 100), (arrow_x, arrow_y), (15, 200), 10)
        i = 0        
        print(index)
        while i <= index:
            #space_b = tsk.Sprite("AlienSpace.jpg", 0, 0)
            #space_b.draw()
            ball = pygame.draw.circle(window, (100, 100,100), (arrow_x+10, arrow_y + i* 50), 15)
            #pygame.display.flip()
            i += 1

        arrow_x += 2
        pygame.display.flip()
        pygame.time.wait(10)
        

        if event.type == pygame.K_DOWN and event.key == pygame.K_SPACE:
		index += 1
   
