# Files
from blob import Blob
from day import Day
from food import Food
from world import World

class Universe:
    def __init__(self, initialBlobsCount, worldSize, simulationDuration, foodQuantity):
        self.world = self.initializeWorld(worldSize)
        self.Blobs = self.initializeBlobs(initialBlobsCount)
        self.Days = []
        self.simulationDuration = simulationDuration
        self.foodQuantity = foodQuantity

        self.runSimulation()

    # Method initializing Blobs
    def initializeBlobs(self, initialBlobsCount):
        Blobs = []
        for i in range(0,initialBlobsCount):
            Blobs.append(Blob(self.world, None))
        return Blobs

    # Method initializing World
    def initializeWorld(self, worldSize):
        return World(worldSize)

    # Method running simulation
    def runSimulation(self):
        for i in range(0, self.simulationDuration):
            aliveBlobs = self.Blobs
            if (i > 0):
                aliveBlobs = self.Days[i-1].getAliveBlobs()
            currentDay = Day(i, self.world, self.foodQuantity, aliveBlobs)
            self.Days.append(currentDay)