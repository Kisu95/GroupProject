# Modules
import numpy as np
import matplotlib.pyplot as plt
from math import floor
from random import random, choice

# Files
from blob import Blob
from food import Food

class World:
    def __init__(self, size):
        # Initialize area attribute with desired size and object data type
        self.area = np.empty(shape=(size, size), dtype='O')

    # Method selecting position for new blob
    def createBlob(self, blob):
        # Create possible positions on world's border
        availablePositions = ((floor(random()*(self.getSize()[0]-1)), 0), (0, floor(random()*(self.getSize()[0]-1))), ((self.getSize()[0]-1), floor(random()*(self.getSize()[0]-1))), (floor(random()*(self.getSize()[0]-1)), (self.getSize()[0]-1)))
        # Select one randomly
        position = choice(availablePositions)
        # If position is occupied repeat until empty position is found
        while (not self.isEmpty(position)):
            availablePositions = ((floor(random()*(self.getSize()[0]-1)), 0), (0, floor(random()*(self.getSize()[0]-1))), ((self.getSize()[0]-1), floor(random()*(self.getSize()[0]-1))), (floor(random()*(self.getSize()[0]-1)), (self.getSize()[0]-1)))
            position = choice(availablePositions)
        # Set position as occupied by the blob
        self.area[position] = blob
        return position

    # Method for map showing
    def draw(self):
        size = self.getSize()
        area = np.zeros(shape=size)
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                if isinstance(self.area[x, y], Blob):
                    area[x, y] = 2
                elif isinstance(self.area[x, y], Food):
                    area[x, y] = 1
        plt.imshow(area)
        plt.show()

    # Method handling random new food generation on map
    def generateFood(self, count):
        size = self.getSize()[0]
        for i in range(0, count):
            x,y = (floor(random()*size), floor(random()*size))
            # We don't check if there is anything, so we may end up removing something from cell
            self.area[x,y] = Food()

    # Method returning world size as tuple (x,y)
    def getSize(self):
        size = np.shape(self.area)
        return size

    # Method returning true if cell is empty
    def isEmpty(self, position):
        result = True if self.area[position] == None else False
        return result

    # Method handling blob movement
    def moveBlob(self, blob, position, move):
        if (self.area[position] != blob):
            return position
        else:
            newPosition = (position[0] + move[0], position[1] + move[1])
            self.area[newPosition] = blob
            self.area[position] = None
            return newPosition