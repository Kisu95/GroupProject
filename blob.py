from random import random
from math import radians, cos, sin, floor

class Blob:
    def __init__(self, world):
        self.relativePosition = (0, 0)
        self.position = world.createBlob(self)
        self.speed = 1

    # Method for displacement calculation
    def calculateDisplacement(self, direction):
        direction = random()*360
        dx = cos(radians(direction)) * self.speed
        dy = sin(radians(direction)) * self.speed
        return dx, dy
        self.relativePosition = (self.relativePosition[0] + dx, self.relativePosition[1] + dy)

    # Method for movement calculation
    def calculateMovement(self, displacement):
        # Calculate cell shift after movement
        move = [0, 0]
        for i in range(2):
            # Check if 0.5 offset barrier was exceeded
            if abs(self.relativePosition[i] + displacement[i]) > 0.5:
                # Calculate cell move accordindly to offset direction (if negative we must substract 0.5 to get correct rounding)
                move[i] = floor(self.relativePosition[i] + displacement[i] + 0.5) if self.relativePosition[i] + displacement[i] > 0 else floor(self.relativePosition[i] + displacement[i] - 0.5)
        return move

    # Method for movement handling
    def move(self, world):
        direction = random()*360
        dx, dy = self.calculateDisplacement(direction)
        displacement = (dx, dy)
        move = self.calculateMovement(displacement)
        # Update position relative to cell
        self.relativePosition = (self.relativePosition[0] + dx, self.relativePosition[1] + dy)
        # Execute movement
        if (abs(move[0])>0 or abs(move[1])>0):
            # Update position relative to cell substracting movement length (to get position in relation to new cell)
            self.relativePosition = (self.relativePosition[0] - move[0], self.relativePosition[1] - move[1])
            self.position = world.moveBlob(self, self.position, move)