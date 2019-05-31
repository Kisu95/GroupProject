class Food:
    def __init__(self, world):
        self.position = world.createFood(self)
        self.world = world