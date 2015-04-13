# clearSpace.py
#
# Clear some space around the player

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
size = int(raw_input("size of space to clear?"))
half = size/2

pos = mc.player.getTilePos()
mc.postToChat("BOOM!")
mc.setBlocks(pos.x-half, pos.y-half, pos.z-half,
             pos.x+half, pos.y+half, pos.z+half, block.AIR.id)

