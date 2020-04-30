import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from camera import *
from test import *
from objects import *


logging.basicConfig(filename='kocka.log',level=logging.DEBUG)

pygame.init()
screenwidth = 600
screenheight = 600           
screen = pygame.display.set_mode((screenwidth, screenheight))


kam = camera(0.035) #meter


def display():
    diplaying = kam.toDisplay(objects)
    for i in range(len(diplaying)):
        for line in objects[i].lines:
            pygame.draw.line(screen, (0, 20, 100), diplaying[i][line[0]], diplaying[i][line[1]], 2)
        #for line in objects[i].lines[:6]:
        #    for line2 in objects[i].lines[6:]: #display sides
        #        pygame.draw.polygon(screen, (100, 20, 100), [diplaying[i][line[0]], diplaying[i][line[1]], diplaying[i][line2[0]], diplaying[i][line2[1]]], 0)

def main():
    run = True
    screen.fill((100,180,180))
    t = 0
    pygame.mouse.set_pos([300,300])
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.fill((10,190,200))

        mouse_pos = pygame.mouse.get_pos()
        kam.rotate(mouse_pos)
        pygame.mouse.set_pos([300,300])
        pressed_keys = pygame.key.get_pressed()
        kam.move(pressed_keys)

        #for o in objects:
        #    o.rotate(0, 0.02)
        #    o.rotate(1, 0.02)
        #    o.rotate(2, 0.02)
            #if o.points[0].matrix[0][0] < 0:
            #    o.move(t, 1)

        #if pygame.mouse.get_pressed()[0]:
        #    print("ohh helo")
        #    newobject.addPoint(kam)
        #    newobject.addLine()

        display()
        t += 0.01
        pygame.display.flip()
main()
