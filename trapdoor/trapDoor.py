# trapDoor.py
#
# A trap door that opens when you stand on it.

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

TRAP_X
TRAP_Y
TRAP_Z
TRAP_BLOCK = block.WOOD_PLANK.id
TRAP_DEPTH = 10

mc = minecraft.Minecraft.create()

mc.setBlock(TRAP_X, TRAP_Y, TRAP_Z, TRAP_BLOCK)
mc.setBlocks(TRAP_X, TRAP_Y-1, TRAP_Z, TRAP_X, TRAP_Y-DEPTH, TRAP_Z, block.AIR.id)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == TRAP_X and pos.y == TRAP_Y and pos.z == TRAP_Z:
        # make sure the player didn't fill in the old tunnel
        mc.setBlocks(TRAP_X, TRAP_Y-1, TRAP_Z, TRAP_X, TRAP_Y-DEPTH, TRAP_Z, block.AIR.id)
        
        # open the trap
        mc.setBlock(TRAP_X, TRAP_Y, TRAP_Z, block.AIR.id)
        mc.postToChat("Trap door!")

        # let the player fall down
        time.sleep(2)

        # close the trap
        mc.setBlock(TRAP_X, TRAP_Y, TRAP_Z, TRAP_BLOCK)

