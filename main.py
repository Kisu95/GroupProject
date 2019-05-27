# Files
from blob import Blob
from food import Food
from world import World

"""
    SCRIPT
"""

# Create squared world 25x25
ddd = World(25)
# Randomly generate 10 food
ddd.generateFood(10)
# Show map
ddd.draw()
print("Map with Food: ")
print(ddd.area)
# Food is yellow

# Create Blob
u = Blob()
# Position Blob at 4,4
ddd.area[4,4] = u
# Show map
ddd.draw()
print("Map with Food and Blob: ")
print(ddd.area)
# Blob is now yellow, and food is green