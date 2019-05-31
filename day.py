class Day:
    def __init__(self, number, maximumDayLength, world, foodQuantity, Blobs):
        self.dayNumber = number
        self.maximumDayLength = maximumDayLength
        self.world = world
        self.world.generateFood(foodQuantity)
        self.aliveBlobs = Blobs
        self.movingBlobs = Blobs

        self.startDay()

    # Method handling day end
    def endDay(self):
        self.world.draw()

    # Method returning all blobs alive
    def getAliveBlobs(self):
        return self.aliveBlobs

    # Method killing blob (removes him from the world and)
    def killBlob(self, blob):
        pass

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
        self.moveBlobs()
        self.endDay()