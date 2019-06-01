from copy import copy

# Files
from blob import Blob


class Day:
    def __init__(self, number, maximumDayLength, world, foodQuantity, Blobs):
        self.dayNumber = number
        self.maximumDayLength = maximumDayLength
        self.dayTime = 0
        self.world = world
        self.world.generateFood(foodQuantity)
        self.aliveBlobs = copy(Blobs)
        self.movingBlobs = copy(Blobs)
        # Start day simulation
        self.startDay()

    # Method removes blob from movingBlobs
    def blobMoveFinished(self, blob):
        self.movingBlobs.remove(blob)

    # Method handling new blob creation
    def createBlob(self, parent):
        blob = Blob(self.world, parent)
        self.aliveBlobs.append(blob)

    # Method handling day end
    def endDay(self):
        print(len(self.movingBlobs))
        for blob in copy(self.aliveBlobs):
            blob.endDay(self, self.world)
        for food in copy(self.world.getRemainingFood()):
            food.removeFromWorld()
        self.world.draw()

    # Method returning all blobs alive
    def getAliveBlobs(self):
        return self.aliveBlobs

    # Method returning current day time
    def getDayTime(self):
        return self.dayTime

    # Method killing blob (removes him from the world and)
    def killBlob(self, blob):
        blobPosition = blob.getPosition()
        self.world.clearPosition(blobPosition)
        self.movingBlobs.remove(blob)
        self.aliveBlobs.remove(blob)

    # Method handling blobs movement (tick based) unitl all are either dead or at home
    def moveBlobs(self):
        while (len(self.movingBlobs) > 0 and self.dayTime < self.maximumDayLength):
            self.world.draw()
            for blob in self.movingBlobs:
                blob.move(self, self.world)
            self.dayTime += 1

    # Method for day start
    def startDay(self):
        print(f"Day {self.dayNumber} started!")
        self.wakeBlobs()
        self.moveBlobs()
        self.endDay()

    # Method for initialization of new day for blobs
    def wakeBlobs(self):
        for blob in self.aliveBlobs:
            blob.newDay(self, self.world)
