from random import random
from math import radians, cos, sin, floor

class Blob:
    def __init__(self):
        self.relativePosition = (0, 0)
        self.speed = 1

    # Method for movement calculation
    def move(self, world):
        direction = random()*360
        dx = cos(radians(direction)) * self.speed
        dy = sin(radians(direction)) * self.speed
        # Update position relative to cell
        self.relativePosition = (self.relativePosition[0] + dx, self.relativePosition[1] + dy)

        # Calculate cell shift after movement
        move = [0, 0]
        for i in range(2):
            if abs(self.relativePosition[i]) > 0.5:
                move[i] = floor(self.relativePosition[i] + 0.5) if self.relativePosition[i] > 0 else floor(self.relativePosition[i] - 0.5)
        # Execute movement
        for i in range(2):
            self.relativePosition[i] -= move[i]
            self.position = world.moveBlob(self, move)