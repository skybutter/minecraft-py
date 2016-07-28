import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

# Define the size of the Castle
SIZE=24
HEIGHT=7

# Function to build Turret
def buildTower(x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.COBBLESTONE.id)
    mc.setBlocks(x1+1, y1, z1+1, x2 - 1, y2, z2 - 1, block.AIR.id)

# Get current position
pos = mc.player.getTilePos()

# Set reference position
x = pos.x + 2
y = pos.y
z = pos.z + 2


# Build Main Castle
mainCastleLen = SIZE - 2
mainCastleHt = HEIGHT - 2
x1 = x + 1
y1 = y
z1 = z + 1
x2 = x1 + mainCastleLen
y2 = y1 + mainCastleHt
z2 = z1 + mainCastleLen
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.COBBLESTONE.id)
x1 = x1 + 1
y1 = y
z1 = z1 + 1
x2 = x2 - 1
y2 = y2
z2 = z2 - 1
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)

# Build Doorway (Clear out wall) & Trench Bridge
x1 = x + 1
y1 = y
z1 = z + SIZE/2 - 1
x2 = x1
y2 = y + 2
z2 = z1 + 2
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)
x1 = x-1
y1 = y1-1
#z1 = z1
x2 = x
y2 = y1
#z2 = z2
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.WOOD.id)

# Building Tower
TOWERLEN = 5  # Best be odd number
towerHt = HEIGHT-1
# Build Tower 1 (North-West)
x1 = x
y1 = y
z1 = z
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 2 (South-West)
x1 = x
y1 = y
z1 = z + SIZE - TOWERLEN
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 3 (North-East)
x1 = x + SIZE - TOWERLEN
y1 = y
z1 = z
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 4 (South-East)
x1 = x + SIZE - TOWERLEN
y1 = y
z1 = z + SIZE - TOWERLEN
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)

