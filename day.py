class Day:
    def __init__(self, number, world, foodQuantity, Blobs):
        self.dayNumber = number
        self.world = world
        self.world.generateFood(foodQuantity)
        self.aliveBlobs = Blobs
        self.movingBlobs = Blobs

    # Method returning all blobs alive
    def getAliveBlobs(self):
        return self.aliveBlobs

    # Method killing blob (removes him from the world and)
    def killBlob(self, blob):
        pass