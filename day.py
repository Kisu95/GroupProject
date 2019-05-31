class Day:
    def __init__(self, world, foodQuantity):
        world.generateFood(foodQuantity)
        # Show map at the day end
        world.draw()