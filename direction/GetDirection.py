# direction.py  14/01/2015  D.J.Whale
#
# Show how to 'guess' at the players move/facing direction in Minecraft Pi edition

import mcpi.minecraft as minecraft
import time

# Rate (in seconds) to report updates to chat
REPORT_RATE = 1

# How long you stand still (in seconds) before the "facing" direction is invalidated
FACING_TIMEOUT = 4

# Create a connection to minecraft
mc = minecraft.Minecraft.create()

# Sample the initial position
pos = mc.player.getTilePos()
xold = pos.x
yold = pos.y
zold = pos.z

# These 3 variables maintain movement direction information (0=none)
mxdirn = 0
mydirn = 0
mzdirn = 0

# These 3 variables maintain facing direction information (0=unknown)
fxdirn = 0
fydirn = 0
fzdirn = 0

# Use time() horizons, so we can run the game loop quickly to avoid
# glitching in sampling directions, but still report messages on the
# chat at a slowish rate
lastReportTime = time.time()
lastMoveTime = time.time()


def dirn(old, new):
    """Turn two values into a signed direction (ignoring magnitude)"""
    if new > old:
        return +1
    elif new < old:
        return -1
    return 0


def compass(d, minus, plus):
    """Turn a direction into text"""
    if d > 0:
        return plus
    elif d < 0:
        return minus
    return ""


def updateMoving():
    """Sample players direction and update variables"""
    global mxdirn, mydirn, mzdirn, xold, yold, zold, lastMoveTime

    # Sample players movement direction each time round the loop
    pos = mc.player.getTilePos()
    mxdirn = dirn(xold, pos.x)
    mydirn = dirn(yold, pos.y)
    mzdirn = dirn(zold, pos.z)

    # If we have moved, remember time we moved, and update old position
    if mxdirn !=0 or mydirn != 0 or mydirn != 0:
        lastMoveTime = time.time()
        
    # Update old position   
    xold = pos.x
    yold = pos.y
    zold = pos.z


def updateFacing():
    """Update the facing direction based on the movement direction"""
    global fxdirn, fydirn, fzdirn
    
    # The facing direction is a sticky version of the movement direction
    # i.e. if moving, update facing direction, else remember old facing direction

    if mxdirn != 0 or mydirn !=0 or mzdirn != 0:
        # we are moving, so set facing direction to moving direction
        fxdirn = mxdirn
        fydirn = mydirn
        fzdirn = mzdirn
        
    else:
        # we are not moving, timeout the sticky facing direction after FACING_TIMEOUT
        # so that if you don't move for ages, we "invalidate" the facing estimation as it
        # has a high probability of being wrong.
        nowtime = time.time()
        if nowtime > lastMoveTime + FACING_TIMEOUT:
            fxdirn = 0
            fydirn = 0
            fzdirn = 0
        


def getMoving():
    if mxdirn != 0 or mydirn != 0 or mzdirn != 0:
        # player is moving
        return ("Moving: "  
            + compass(mzdirn, "north", "south") + " "
            + compass(mxdirn, "west", "east") + " "
            + compass(mydirn, "down", "up"))
    else:
        return "Not Moving"
    

def getFacing():
    if fxdirn != 0 or fydirn !=0 or fzdirn != 0L:
        # Facing direction is known
        return ("Facing: "
            + compass(fzdirn, "north", "south") + " "
            + compass(fxdirn, "west", "east") + " "
            + compass(fydirn, "down", "up"))
    else:
        return "Not sure which way you are facing"
    

# Game loop

while True:
    time.sleep(0.1)
    updateMoving()
    updateFacing()

    # Report movement direction and facing direction on chat, every few seconds
    now = time.time()
    if now > lastReportTime + REPORT_RATE:
        lastReportTime = now
        
        mc.postToChat(getFacing())

        if mxdirn !=0 or mydirn != 0 or mzdirn != 0:
            # Only report movement direction if player is moving
            mc.postToChat(getMoving())
# END

