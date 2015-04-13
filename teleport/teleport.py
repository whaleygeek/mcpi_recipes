# teleport.py
#
# Teleport the player to a particular location

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

FROM_X = 0
FROM_Y = 0
FROM_Z = 0

TO_X = 10
TO_Y = 20
TO_Z = 30

mc = minecraft.Minecraft.create()
mc.setBlock(FROM_X, FROM_Y, FROM_Z, block.DIAMOND_BLOCK.id)
mc.setBlock(TO_X, TO_Y, TO_Z, block.GOLD_BLOCK.id)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    
    if pos.x == FROM_X and pos.y == FROM_Y and pos.z == FROM_Z:
        # now teleport
        mc.postToChat("Teleporting...")
        time.sleep(2)
        mc.player.setTilePos(TO_X, TO_Y, TO_Z)
        mc.postToChat("You have arrived")

    


    
