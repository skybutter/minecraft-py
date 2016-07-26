import mcpi.minecraft as minecraft
import mcpi.block as block

SIZE = 26
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

mc.setBlocks(pos.x, pos.y, pos.z, pos.x+SIZE, pos.y+SIZE, pos.z+SIZE, block.AIR.id)
mc.setBlocks(pos.x, pos.y, pos.z-SIZE, pos.x+SIZE, pos.y+SIZE, pos.z, block.AIR.id)