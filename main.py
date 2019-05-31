# Files
from blob import Blob
from day import Day
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
# Initialize days
Days = []

# Run simulation
for dayNumber in range (0, simulationDuration):
    Days.append(Day(world, foodQuantity))