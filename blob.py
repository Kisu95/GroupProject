# Modules
from random import random
from math import radians, degrees, cos, sin, floor, atan2, sqrt
import numpy as np
from numpy.linalg import norm

# Files
from food import Food

class Blob:
    def __init__(self, world, parent):
        self.relativePosition = (0, 0)
        self.position = world.createBlob(self)
        self.home = self.position
        self.food = 0
        self.speed = 1
        # Used for remembering current destination
        self.target = None
        self.updateSurroundingsDetails(world)
        self.planDayRoute(world)

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
                move[i] = floor(self.relativePosition[i] + displacement[i] + 0.5)
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

    # Method to find food target position in surroundings
    def checkSurroundings(self, world):
        surroundings = self.updateSurroundingsDetails(world)
        size = np.shape(surroundings)
        for x in range(0, size[0]):
            for y in range(0, size[1]):
                if (isinstance(surroundings[x, y], Food)):
                    return (self.position[0] + x-1, self.position[1] + y-1)
        raise ValueError('No viable target in range!')

    # Method returns distance to target
    def distanceToTarget(self, target):
        absoultePosition = self.getTruePosition()
        distance = norm(np.array(absoultePosition) - np.array(target))
        return distance

    # Method handling food consumption
    def eat(self, food):
        self.food += 1

    # Method returning direction to target in degrees
    def getDirectionToTarget(self, target):
        positionFromTarget = (target[1] - self.position[1], target[0]- self.position[0])
        directionToTarget = degrees(atan2(*positionFromTarget))
        return directionToTarget

    # Method returning true blob position (with offset)
    def getTruePosition(self):
        return (self.position[0] + self.relativePosition[0], self.position[1] + self.relativePosition[1])

    # Method checking if blob is in home
    def inHome(self):
        return True if (self.position == self.home) else False

    # Method checking if blob is at given position
    def isAt(self, position):
        return True if (self.position == position) else False

    # Method for movement handling
    def move(self, day, world):
        direction = random()*360
        distance = 0
        # Check if has eaten any food
        if (self.food > 0):
            # Check if returned home already
            if (self.inHome()):
                return True
            else:
                direction = self.getDirectionToTarget(self.home)
        else:
            if (self.isAt(self.target)):
                self.target = None
            # Try to find target where to go
            try:
                # Try to use preplanned route first
                if (len(self.plannedRoute) > 0 and (self.target == None)):
                    self.target = self.plannedRoute.pop(0)
                # Check if there is any food nearby
                self.target = self.checkSurroundings(world)
                direction = self.getDirectionToTarget(self.target)
                distance = self.distanceToTarget(self.target)
            except ValueError:
                # No target in range, so we proceed
                pass
        dx, dy = self.calculateDisplacement(direction)
        displacement = (dx, dy)
        # Check if distance to target is lower than maximum displacement length and shorten displacement, so blob cannot overshoot his destination
        if (distance != 0):
            displacementLength = norm(displacement)
            if (displacementLength > distance):
                displacement = (displacement[0] / 2, displacement[1] / 2)
        move = self.calculateMovement(displacement)
        # If movement in selected direction is not possible select another
        while ((move[0] != 0 or move[1] != 0) and (not self.canMove(world, move))):
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

    # Method for daily route planning
    def planDayRoute(self, world):
        route = []
        size = world.getSize()
        for i in range(0,floor(random()*3)):
            x = floor(random()*(size[0]-2))+1
            y = floor(random()*(size[1]-2))+1
            route.append((x, y))
        self.plannedRoute = route

    # Method handling blob replication
    def replicate(self):
        pass

    # Method updates surrounding details by requesting appropriate slice of map
    def updateSurroundingsDetails(self, world):
        chunk = (slice(self.position[0]-1, self.position[0]+1, 1), slice(self.position[1]-1, self.position[1]+1, 1))
        self.surroundings = world.getAreaDetails(chunk)
        return self.surroundings