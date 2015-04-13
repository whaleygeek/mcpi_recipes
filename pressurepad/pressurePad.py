# pressurePad.py
#
# work out if you are standing on a pressure pad
# The pad is at a specific location

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

PAD_X   = 10
PAD_Y   = 0
PAD_Z   = 12
MESSAGE = "You are standing on the mat"

mc.setBlock(PAD_X, PAD_Y, PAD_Z, block.WOOL.id, 7)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == PAD_X and pos.y == PAD_Y and pos.z == PAD_Z:
        mc.postToChat(MESSAGE)
        
