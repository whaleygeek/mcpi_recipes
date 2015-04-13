# repeat.py
#
# Make things happen at precise repeat intervals

import mcpi.minecraft as minecraft
import time

BASE  = 1
RATE1 = 5
RATE2 = 7

mc = minecraft.Minecraft.create()

now = time.time()
timer1 = now + RATE1
timer2 = now + RATE2

while True:
    time.sleep(BASE)

    now = time.time()
    if now > timer1:
        mc.postToChat("Timer 1")
        timer1 = now + RATE1

    if now > timer2:
        mc.postToChat("Timer 2")
        timer2 = now + RATE2
        
