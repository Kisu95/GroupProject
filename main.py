# Files
from blob import Blob
from food import Food
from world import World

"""
    SCRIPT
"""

# How many days to run simulation for
simulationDuration = 3
# Number of new food generated each day
foodQuantity = 10
# World size (square)
worldSize = 25

# Initialize world
world = World(worldSize)
for i in range(0, 30):
    blob1 = Blob(world)
# Run simulation
for dayNumber in range (0, simulationDuration):
    world.generateFood(foodQuantity)
    # Show map at the day end
    world.draw()