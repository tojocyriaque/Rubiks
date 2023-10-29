import numpy
from faces import *

class Piece:

    def __init__(self, matrix):
        self.light = False

        self.x = matrix[0][3]
        self.y = matrix[1][3]
        self.z = matrix[2][3]

        self.mat = numpy.array([
            [1, 0, 0, self.x],
            [0, 1, 0, self.y],
            [0, 0, 1, self.z],
            [0, 0, 0, 1]
        ])

        self.faces = [
            Face((0, 0,-1), (255, 0, 0)), #front
            Face((0, 0, 1), (255, 150, 0)), #back
            Face((-1,0, 0), (0, 255, 0)),#left
            Face((1, 0, 0), (0, 0, 255)),#right
            Face((0,-1, 0), (255, 255, 0)),#up
            Face((0, 1, 0), (255,255,255))#down
        ]

    def turn_u(self, angle):
        tx = self.mat[0][3]
        y = self.mat[1][3]
        z = self.mat[2][3]

        x = tx * numpy.cos(angle) - z * numpy.sin(angle)
        z = tx * numpy.sin(angle) + z * numpy.cos(angle)

        self.mat = numpy.array([
            [1, 0, 0, round(x)],
            [0, 1, 0, round(y)],
            [0, 0, 1, round(z)],
            [0, 0, 0, 1]
        ])

        self.x = round(x)
        self.y = round(y)
        self.z = round(z)

    def turn_r(self, angle):
        x = self.mat[0][3]
        ty = self.mat[1][3]
        z = self.mat[2][3]

        y = ty * numpy.cos(angle) - z * numpy.sin(angle) 
        z = ty * numpy.sin(angle) + z * numpy.cos(angle)

        self.mat = numpy.array([
            [1, 0, 0, round(x)],
            [0, 1, 0, round(y)],
            [0, 0, 1, round(z)],
            [0, 0, 0, 1]
        ])

        self.x = round(x)
        self.y = round(y)
        self.z = round(z)

    def turn_f(self, angle):
        x = self.mat[0][3]
        ty = self.mat[1][3]
        z = self.mat[2][3]

        y = ty * numpy.cos(angle) - x * numpy.sin(angle)
        x = ty * numpy.sin(angle) + x * numpy.cos(angle)

        self.mat = numpy.array([
            [1, 0, 0, round(x)],
            [0, 1, 0, round(y)],
            [0, 0, 1, round(z)],
            [0, 0, 0, 1]
        ])

        self.x = round(x)
        self.y = round(y)
        self.z = round(z)


