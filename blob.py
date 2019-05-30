from random import random
from math import radians, cos, sin

class Blob:
    def __init__(self):
        self.relativePosition = (0, 0)
        self.speed = 1

    def move(self):
        direction = random()*360
        dx = cos(radians(direction)) * self.speed
        dy = sin(radians(direction)) * self.speed
        self.relativePosition = (self.relativePosition[0] + dx, self.relativePosition[1] + dy)