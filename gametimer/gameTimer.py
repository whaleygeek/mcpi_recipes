# gameTimer.py
#
# A simple timer that runs the game for a fixed amount of time

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

TIME = 30

mc = minecraft.Minecraft.create()
timeleft = TIME

while timeleft > 0:
    time.sleep(1)
    timeleft -= 1
    mc.postToChat("Time left:" + str(timeleft))

mc.postToChat("Time up!")


