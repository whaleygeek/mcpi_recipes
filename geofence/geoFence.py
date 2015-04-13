# geoFence.py
#
# Work out if you are standing in a geo-fenced region

import mcpi.minecraft as minecraft
import time

GEO_X1 = 10
GEO_Z1 = 10
GEO_X2 = 20
GEO_Z2 = 30

mc = minecraft.Minecraft.create()
mc.setBlocks(GEO_X1, GEO_Y1, GEO_Z1, GEO_X2, GEO_Y1, GEO_Z2, block.STONE.id)

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if  pos.x >= GEO_X1 and pos.x <= GEO_X2 \
    and pos.z >= GEO_Z1 and pos.z <= GEO_Z2:
        mc.postToChat("You are in the zone")
        
