import pygame
from math import *
import random
from pygame import locals
import logging
from matrix import *
from test import *



class camera():
    def __init__(self, focus):
        self.mouse_sensitivity = 10
        self.focus = focus
        self.perspektív = matrix([[focus, 0, 0],[0, focus, 0],[0,0,1]])
        self.eltolas = vector([0,0,0])
        self.forgatas = matrix([[1, 0, 0],[0, 1, 0],[0, 0, 1]])
        self.mouse_pos = [0,0]
        self.speed = 0.03

    def move(self, keys):

        if keys[pygame.K_w]:

            self.eltolas.matrix[2][0] -= self.speed * self.forgatas.matrix[2][2]
            self.eltolas.matrix[0][0] -= self.speed * self.forgatas.matrix[2][0]

        if keys[pygame.K_s]:
            self.eltolas.matrix[2][0] += self.speed * self.forgatas.matrix[2][2]
            self.eltolas.matrix[0][0] += self.speed * self.forgatas.matrix[2][0]

        if keys[pygame.K_d]:
            self.eltolas.matrix[2][0] -= self.speed * -self.forgatas.matrix[2][0]
            self.eltolas.matrix[0][0] -= self.speed * self.forgatas.matrix[2][2]

        if keys[pygame.K_a]:
            self.eltolas.matrix[2][0] += self.speed * -self.forgatas.matrix[2][0]
            self.eltolas.matrix[0][0] += self.speed * self.forgatas.matrix[2][2]

        if keys[pygame.K_LSHIFT]:
            self.eltolas.matrix[1][0] -= self.speed
        if keys[pygame.K_SPACE]:
            self.eltolas.matrix[1][0] += self.speed




    def rotate(self, position):
        self.mouse_pos[0] -= position[0]-300
        self.mouse_pos[1] += position[1]-300
        position =  [self.mouse_pos[1]/self.mouse_sensitivity  , self.mouse_pos[0]/self.mouse_sensitivity ]

        to_rotate = matrix([[1,0,0],[0, cos(radians(position[0])), -1 *sin(radians(position[0]))],[0, sin(radians(position[0])), cos(radians(position[0]))]])
        to_rotate *= matrix([[cos(radians(position[1])), 0, sin(radians(position[1]))],[0,1,0],[-1 * sin(radians(position[1])), 0, cos(radians(position[1]))]])
        
        self.forgatas = to_rotate


    def collisionDetect(self):
        pass #will be added

    def toDisplay(self, objects):
        middleOfScreen = [300,300]
        meterToPixel = 10000
        objects_toDisplay =[]
        tav = []
        for obj in objects: 
            pontok = []
            kifele = False
            for p in obj.updatePoints():
            #transforming space according to the relative position of the camera
                relativeP = self.forgatas * (self.eltolas + p)
                if relativeP.matrix[2][0] < self.focus:
                    kifele = True
            #perspektivikus transzformacio
                perspectiveP = self.perspektív *  relativeP
                pontok = [*pontok, perspectiveP]

            tavolsag = self.eltolas - obj.updatePoints()[0]
 #sorrend tovolsag szerint
            tav.append(sqrt(tavolsag.matrix[0][0]**2 + tavolsag.matrix[1][0]**2 + tavolsag.matrix[2][0]**2))

            onPlane = [[point.matrix[0][0]/point.matrix[2][0], point.matrix[1][0]/point.matrix[2][0]] for point in pontok]
            #scale to screen
            if kifele:
                continue
            objects_toDisplay.append([[middleOfScreen[0]+ meterToPixel * point[0], middleOfScreen[1]+ meterToPixel * point[1] ] for point in onPlane])
        sortedlist = [x for _, x in sorted(zip(tav, objects_toDisplay), reverse = True)]
        return sortedlist #objects_toDisplay
