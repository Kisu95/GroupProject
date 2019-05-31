# Modules
from random import random
from math import radians, degrees, cos, sin, floor, atan2

class Blob:
    def __init__(self, world):
        self.relativePosition = (0, 0)
        self.position = world.createBlob(self)
        self.home = self.position
        self.food = 0
        self.speed = 1

    # Method for displacement calculation
    def calculateDisplacement(self, direction):
        dx = cos(radians(direction)) * self.speed
        dy = sin(radians(direction)) * self.speed
        return dx, dy

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

    # Method checking if movement in desired direction is possible
    def canMove(self, world, move):
        newPosition = (self.position[0] + move[0], self.position[1] + move[1])
        worldSize = world.getSize()
        # Check if new position is outside of the world
        if (newPosition[0] < 0 or newPosition[1] < 0 or newPosition[0] >= worldSize[0] or newPosition[1] >= worldSize[1]):
            return False
        # Check if new position is empty
        return True if world.isEmpty(newPosition) else (True if world.isFood(newPosition) else False)

    # Method returning direction to home in degrees
    def getDirectionToHome(self):
        positionFromHome = (self.position[0] - self.home[0], self.position[1] - self.home[1])
        directionToHome = degrees(atan2(*positionFromHome))
        return directionToHome

    # Method handling food consumption
    def eat(self, food):
        self.food += 1

    # Method checking if blob is in home
    def inHome(self):
        return True if (self.position == self.home) else False

    # Method for movement handling
    def move(self, world):
        direction = random()*360
        # Check if has eaten any food
        if (self.food > 0):
            # Check if returned home already
            if (self.inHome()):
                return True
            else:
                direction = self.getDirectionToHome()
        dx, dy = self.calculateDisplacement(direction)
        displacement = (dx, dy)
        move = self.calculateMovement(displacement)
        # If movement in selected direction is not possible select another
        while (not self.canMove(world, move) and (move[0] != 0 or move[1] != 0)):
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