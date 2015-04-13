# health.py
#
# A simple health monitor

import mcpi.minecraft as minecraft
import time

health = 20

mc = minecraft.Minecraft.create()

while health > 0:
    time.sleep(1)
    health -= 1
    mc.postToChat("health:" + str(health))
    
