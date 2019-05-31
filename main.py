# Files
from blob import Blob
from food import Food
from world import World

"""
    SCRIPT
"""

# How many days to run simulation for
simulationDuration = 15
# Number of new food generated each day
foodQuantity = 10
# World size (square)
worldSize = 25

# Initialize world
world = World(worldSize)
blobs = []
for i in range(0, 10):
    blobs.append(Blob(world))
# Run simulation
for dayNumber in range (0, simulationDuration):
    world.generateFood(foodQuantity)
    # Show map at the day start
    world.draw()
    for blob in blobs:
        blob.move(world)
    # Show map at the day end
    world.draw()