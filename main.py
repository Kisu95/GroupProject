# Files
from blob import Blob
from day import Day
from food import Food
from universe import Universe
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
# Number of Blobs created at start
initialBlobsCount = 10

universe = Universe(initialBlobsCount, worldSize, simulationDuration, foodQuantity)