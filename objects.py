import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from camera import *
from test import *
from objects import *


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




objects = [cube]

