# Files
from blob import Blob
from day import Day
from food import Food
from world import World


class Universe:
    def __init__(self, initialBlobsCount, worldSize, simulationDuration, maximumDayLength, foodQuantity):
        self.world = self.initializeWorld(worldSize)
        self.Blobs = self.initializeBlobs(initialBlobsCount)
        self.Days = []
        self.simulationDuration = simulationDuration
        self.maximumDayLength = maximumDayLength
        self.foodQuantity = foodQuantity

        self.runSimulation()

    # Method initializing Blobs
    def initializeBlobs(self, initialBlobsCount):
        Blobs = []
        for i in range(0, initialBlobsCount):
            Blobs.append(Blob(self.world, None))
        return Blobs

    # Method initializing World
    def initializeWorld(self, worldSize):
        return World(worldSize)

    # Method running simulation
    def runSimulation(self):
        for i in range(0, self.simulationDuration):
            if (i > 0):
                self.Blobs = self.Days[i-1].getAliveBlobs()
            if (len(self.Blobs) == 0):
                return False
            currentDay = Day(i, self.maximumDayLength, self.world,
                             self.foodQuantity, self.Blobs)
            self.Days.append(currentDay)
