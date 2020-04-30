import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from camera import *
from test import *
from objects import *


cube1 = test( 10000, vector([0,0,5]),
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


cube = test( 10000, vector([0,0,15]),
    [
    vector([-2, -1, -1]),
    vector([-2, -1,  1]),
    vector([-2,  1, -1]),
    vector([-2,  1,  1]),
    vector([ 2, -1, -1]),
    vector([ 2, -1,  1]),
    vector([ 2,  1, -1]),
    vector([ 2,  1,  1]),
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


newobject = test(50, vector([0,0,15]),
    [
#will be added by click (points)
    ],
    [
#will add automaticly (lines)
    ])

def random_object_gen():
    toobj = []
    for p in range(10):
        posy = p*2
        for i in range(10):
            posx = i *2
            cubik = test( 1000, vector([random.randint(25, 100),random.randint(25, 100),random.randint(25, 100)]),
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
            toobj.append(cubik)
    return toobj

def rubicCube_gen():
    toobj = []
    for z in range(5):
        posz = z*3
        for y in range(5):
            posy = y*3
            for x in range(5):
                posx = x*3
                cubik = test(1000, vector([posx,posy,posz]),     # vector([random.randint(25, 100),random.randint(25, 100),random.randint(25, 100)]),
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
                toobj.append(cubik)
    return toobj





objects = [cube, cube1] # rubicCube_gen()

