# snailTrail.py
#
# Build things by leaving a trail of blocks

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

TRAIL_TIME = 20
TRAIL_BLOCK = block.STONE.id

mc = minecraft.Minecraft.create()

timeleft = TRAIL_TIME
mc.postToChat("snail trail active for:" + str(timeleft) + " seconds")

while TRAIL_TIME > 0:
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y, pos.z, TRAIL_BLOCK)
    timeleft -= 1
    time.sleep(1)

mc.postToChat("snail trail has finished")

    
