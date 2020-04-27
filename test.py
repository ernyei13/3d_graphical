import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from camera import *


class test():
    def __init__(self, size, eltolas, points, lines):
        self.size = size
        self.points = points
        self.lines = lines
        self.eltolas = eltolas
        self.forgatas = matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
    def rotate(self, direction, degree):
        if direction == 0:
            to_rotate = matrix([[1,0,0],[0, cos(degree), -1 *sin(degree)],[0, sin(degree), cos(degree)]])
        if direction == 1:
            to_rotate = matrix([[cos(degree), 0, sin(degree)],[0,1,0],[-1 *sin(degree), 0, cos(degree)]])
        if direction == 2:
            to_rotate = matrix([[cos(degree), -1*sin(degree), 0],[sin(degree), cos(degree), 0],[0, 0, 1]])
        self.forgatas *= to_rotate

    def tolas(self, t, dir):
        self.eltolas.matrix[dir][0] += sin(t) * 5


    def updatePoints(self):
        return [self.forgatas * point + self.eltolas for point in self.points]
