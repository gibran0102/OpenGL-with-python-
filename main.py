import pygame 
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import random


from cubo import Cubo


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(random.randrange(-5,5),random.randrange(-5,5), -40)

    newcube = Cubo()

    max_distance = 100
    cube_dict = {}

    for x in range(60):
        cube_dict[x] = newcube.set_vertices(max_distance)
        

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            newcube.rotate(event)

        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glTranslatef(newcube.x_move,newcube.y_move,.50)

        
        for j in cube_dict:
            newcube.draw(cube_dict[j])

        
        pygame.display.flip()

main()
