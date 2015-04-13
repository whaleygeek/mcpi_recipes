# score.py
#
# A simple game scoring system

import mcpi.minecraft as minecraft
import time

score = 0

mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    score += 1
    mc.postToChat("score:" + str(score))
    
