# howLong.py
#
# Time how long something takes

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

TREASURE_X = 10
TREASURE_Y = 0
TREASURE_Z = 20

mc = minecraft.Minecraft.create()

mc.setBlock(TREASURE_X, TREASURE_Y, TREASURE_Z, block.GOLD_BLOCK.id)

mc.postToChat("Find the treasure")
starttime = time.time()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == TREASURE_X and pos.y == TREASURE_Y and pos.z == TREASURE_Z:
        now = time.time()
        taken = now - starttime
        mc.postToChat("It took you " + str(taken) + " seconds")
        break
    
