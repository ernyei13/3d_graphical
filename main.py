import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from camera import *
from test import *


logging.basicConfig(filename='kocka.log',level=logging.DEBUG)

pygame.init()
screenwidth = 600
screenheight = 600           
screen = pygame.display.set_mode((screenwidth, screenheight))










def readin():
    with open("data1.txt", "r") as data:
        d = data.read().split()


kam = camera(0.035) #meter


cube = test( 10000,
    [
    vector([-1, -1, -1]),
    vector([-1, -1,  1]),
    vector([-1,  1, -1]),
    vector([-1,  1,  1]),
    vector([ 1, -1, -1]),
    vector([ 1, -1,  1]),
    vector([ 1,  1, -1]),
    vector([ 1,  1,  1]),
    ],
    [[0, 1],
    [1, 3],
    [3, 2],
    [2, 0],
    [4, 5],
    [5, 7],
    [7, 6],
    [6, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7],
    ])




objects = [cube]#, cube1]



def display():
    diplaying = kam.toDisplay(objects)
    for i in range(len(diplaying)): 
        for line in objects[i].lines:
            pygame.draw.line(screen, (0, 20, 100), diplaying[i][line[0]], diplaying[i][line[1]], 2)

def main():
    logging.info("Kezdodik")
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

        pressed_keys = pygame.key.get_pressed()
        kam.move(pressed_keys)


        mouse_pos = pygame.mouse.get_pos()
        kam.rotate(mouse_pos)
        pygame.mouse.set_pos([300,300])

        display()
        t += 0.03
        pygame.display.flip()
main()
