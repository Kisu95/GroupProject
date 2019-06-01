class Food:
    def __init__(self, world):
        self.position = world.createFood(self)
        self.world = world

    # Method returning food's position in the world
    def getPosition(self):
        return self.position

    # Method for food removal from the world
    def removeFromWorld(self):
        self.world.removeFood(self)