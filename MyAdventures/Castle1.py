import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

# Define the size of the Castle
SIZE=26
HEIGHT=7

# Function to build Turret
def buildTower(x1, y1, z1, x2, y2, z2):
    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.STONE_BRICK.id)
    mc.setBlocks(x1+1, y1, z1+1, x2 - 1, y2, z2 - 1, block.AIR.id)
    # Build block on wall every other block - West
    a = x1
    b = y2 + 1
    c = z1
    while c <= z2:
        mc.setBlock(a, b, c, block.STONE_BRICK.id)
        c = c + 2
    # Build block on wall every other block - East
    a = x2
    b = y2 + 1
    c = z1
    while c <= z2:
        mc.setBlock(a, b, c, block.STONE_BRICK.id)
        c = c + 2
    # Build block on wall every other block - North
    a = x1
    b = y2 + 1
    c = z1
    while a <= x2:
        mc.setBlock(a, b, c, block.STONE_BRICK.id)
        a = a + 2
    # Build block on wall every other block - South
    a = x1
    b = y2 + 1
    c = z2
    while a <= x2:
        mc.setBlock(a, b, c, block.STONE_BRICK.id)
        a = a + 2

# Get current position
pos = mc.player.getTilePos()

# Set reference position
x = pos.x + 2
y = pos.y
z = pos.z + 2

# Build Trench
# width of trench
trenchWidth = 2
x1 = x
y1 = y-1
z1 = z
x2 = x1 + SIZE
y2 = y1
z2 = z1 + SIZE
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.WATER.id)
x1 = x+trenchWidth
y1 = y-1
z1 = z+trenchWidth
x2 = x1 + SIZE - (2*trenchWidth)
y2 = y1
z2 = z1 + SIZE - (2*trenchWidth)
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.WOOL.id)
#
# Build Main Castle
#
mainCastleLen = SIZE - (2*trenchWidth) - 2
mainCastleHt = HEIGHT - 3
x1 = x + trenchWidth + 1
y1 = y
z1 = z + trenchWidth + 1
x2 = x1 + mainCastleLen
y2 = y1 + mainCastleHt
z2 = z1 + mainCastleLen
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.COBBLESTONE.id)
thick = 2
x1 = x1 + thick
y1 = y
z1 = z1 + thick
x2 = x2 - thick
y2 = y2
z2 = z2 - thick
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)
# Build block on wall every other block - West
a = x + trenchWidth + 1
b = y2 + 1
c = z + trenchWidth + 1
while c < z2 :
    c = c + 2
    mc.setBlock(a, b, c, block.COBBLESTONE.id)
# Build block on wall every other block - East
a = x + trenchWidth + 1 + mainCastleLen
b = y2 + 1
c = z + trenchWidth + 1
while c < z2 :
    c = c + 2
    mc.setBlock(a, b, c, block.COBBLESTONE.id)
# Build block on wall every other block - North
a = x + trenchWidth + 1
b = y2 + 1
c = z + trenchWidth + 1
while a < x2 :
    a = a + 2
    mc.setBlock(a, b, c, block.COBBLESTONE.id)
# Build block on wall every other block - South
a = x + trenchWidth + 1
b = y2 + 1
c = z + trenchWidth + 1 + mainCastleLen
while a < x2 :
    a = a + 2
    mc.setBlock(a, b, c, block.COBBLESTONE.id)


# Build Doorway (Clear out wall) & Trench Bridge
x1 = x + trenchWidth + 1
y1 = y
z1 = z + SIZE/2 - 1
x2 = x1
y2 = y + 2
z2 = z1 + 2
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.AIR.id)
x1 = x-1
y1 = y1-1
#z1 = z1
x2 = x + trenchWidth
y2 = y1
#z2 = z2
mc.setBlocks(x1, y1, z1, x2, y2, z2, block.WOOD.id)

# Building Tower
TOWERLEN = 4  # Best be even number
towerHt = HEIGHT-1
# Build Tower 1 (North-West)
x1 = x + trenchWidth
y1 = y
z1 = z + trenchWidth
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 2 (South-West)
x1 = x + trenchWidth
y1 = y
z1 = z + SIZE - trenchWidth - TOWERLEN
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 3 (North-East)
x1 = x + SIZE - trenchWidth - TOWERLEN
y1 = y
z1 = z + trenchWidth
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)
# Build Tower 4 (South-East)
x1 = x + SIZE - trenchWidth - TOWERLEN
y1 = y
z1 = z + SIZE - trenchWidth - TOWERLEN
x2 = x1 + TOWERLEN
y2 = y1 + towerHt
z2 = z1 + TOWERLEN
buildTower(x1, y1, z1, x2, y2, z2)

