from copy import copy

class Day:
    def __init__(self, number, maximumDayLength, world, foodQuantity, Blobs):
        self.dayNumber = number
        self.maximumDayLength = maximumDayLength
        self.world = world
        self.world.generateFood(foodQuantity)
        self.aliveBlobs = copy(Blobs)
        self.movingBlobs = copy(Blobs)

        self.startDay()

    # Method handling day end
    def endDay(self):
        print(len(self.movingBlobs))
        for blob in copy(self.movingBlobs):
            self.killBlob(blob)
        self.world.draw()

    # Method returning all blobs alive
    def getAliveBlobs(self):
        return self.aliveBlobs

    # Method killing blob (removes him from the world and)
    def killBlob(self, blob):
        blobPosition = blob.getPosition()
        self.world.clearPosition(blobPosition)
        self.movingBlobs.remove(blob)
        self.aliveBlobs.remove(blob)

    def blobMoveFinished(self, blob):
        self.movingBlobs.remove(blob)

    # Method handling blobs movement (tick based) unitl all are either dead or at home
    def moveBlobs(self):
        dayLength = 0
        while (len(self.movingBlobs) > 0 and dayLength < self.maximumDayLength):
            self.world.draw()
            for blob in self.movingBlobs:
                blob.move(self, self.world)
            dayLength += 1

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