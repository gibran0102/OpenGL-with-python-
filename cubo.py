import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from variables import *
import random


class Cubo():
    def __init__(self):
        self.verticies = verticies
        self.edges = edges
        self.colors = colors
        self.surfaces = surfaces
        self.x_move = 0
        self.y_move = 0


    def draw(self, vertic):
        glBegin(GL_QUADS)
        for surface  in self.surfaces:
            x = 0
            for vertex in surface:
                x+=1
                glColor3fv(self.colors[x])
                glVertex3fv(vertic[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(vertic[vertex])
        glEnd()

    

    def rotate(self, event):
        if(event.type == pygame.KEYDOWN):
            if(event.key == K_d):
                self.x_move = -0.3
            elif (event.key == K_a):
                self.x_move = 0.3
            elif(event.key == K_w):
                self.y_move = -0.3
            elif(event.key == K_s):
                self.y_move = 0.3

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                glTranslatef(0,0,1.0)

            if event.button == 5:
                glTranslatef(0,0,-1.0)


    def set_vertices(self, max_distance):
        x_value_change = random.randrange(-10,10)
        y_value_change = random.randrange(-10,10)
        z_value_change = random.randrange(-1*max_distance,-20)

        new_vertices = []

        for vert in self.verticies:
            new_vert = []

            new_x = vert[0] + x_value_change
            new_y = vert[1] + y_value_change
            new_z = vert[2] + z_value_change

            new_vert.append(new_x)
            new_vert.append(new_y)
            new_vert.append(new_z)

            new_vertices.append(new_vert)

        return new_vertices