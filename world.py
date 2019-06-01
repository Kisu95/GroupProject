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
        self.Food = []

    # Method for object removal by position
    def clearPosition(self, position):
        self.area[position] = None

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

    # Method selecting position for new food
    def createFood(self, food):
        size = self.getSize()[0]
        # Create position not on world's border
        position = (floor(random()*(size-2))+1, floor(random()*(size-2))+1)
        # If position is occupied repeat until empty position is found
        while (not self.isEmpty(position)):
            position = (floor(random()*(size-2))+1, floor(random()*(size-2))+1)
        # Set position as occupied by the food
        self.area[position] = food
        return position

    # Method for map showing
    def draw(self):
        size = self.getSize()
        area = np.zeros(shape=size)
        # Find all objects on the map and store them as numbers (for image generation)
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                if isinstance(self.area[x, y], Blob):
                    area[x, y] = 2
                elif isinstance(self.area[x, y], Food):
                    area[x, y] = 1
        plt.pause(0.1)
        plt.imshow(area, origin='lower')

    # Method handling random new food generation on map
    def generateFood(self, count):
        for i in range(0, count):
            self.Food.append(Food(self))

    # Method returning area details (map section)
    def getAreaDetails(self, chunk):
        return self.area[chunk]

    # Method returning remaning food on the world
    def getRemainingFood(self):
        return self.Food

    # Method returning world size as tuple (x,y)
    def getSize(self):
        size = np.shape(self.area)
        return size

    # Method returning true if cell is empty
    def isEmpty(self, position):
        result = True if self.area[position] == None else False
        return result

    # Method returning true if object (or object on position) is food
    def isFood(self, obj):
        if (isinstance(obj, tuple)):
            obj = self.area[obj]
        return True if isinstance(obj, Food) else False

    # Method handling blob movement
    def moveBlob(self, blob, position, move):
        if (self.area[position] != blob):
            return position
        else:
            newPosition = (position[0] + move[0], position[1] + move[1])
            obj = self.area[newPosition]
            if (self.isFood(obj)):
                blob.eat(obj)
            self.area[newPosition] = blob
            self.area[position] = None
            return newPosition

    # Method removes food from world's food array
    def removeFood(self, food):
        foodPosition = food.getPosition()
        self.area[foodPosition] = None
        self.Food.remove(food)