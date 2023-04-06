from Utils.Offsets import *
from math import *
from Utils.Vector3 import Vec3
from Utils.Offsets import *

def checkangles(x, y):
    if x > 89:
        return False
    elif x < -89:
        return False
    elif y > 360:
        return False
    elif y < -360:
        return False
    else:
        return True

def nanchecker(first, second):
    if isnan(first) or isnan(second):
        return False
    else:
        return True

def rcse(pm, player, engine_pointer, oldpunch, newrcs, punch, rcs):
    if pm.read_uint(player + m_iShotsFired) > 2:
        rcs.x = pm.read_float(engine_pointer + dwClientState_ViewAngles)
        rcs.y = pm.read_float(engine_pointer + dwClientState_ViewAngles + 0x4)
        punch.x = pm.read_float(player + m_aimPunchAngle)
        punch.y = pm.read_float(player + m_aimPunchAngle + 0x4)
        newrcs.x = rcs.x - (punch.x - oldpunch.x) * 2
        newrcs.y = rcs.y - (punch.y - oldpunch.y) * 2
        oldpunch.x = punch.x
        oldpunch.y = punch.y
        if nanchecker(newrcs.x, newrcs.y) and checkangles(newrcs.x, newrcs.y):
            pm.write_float(engine_pointer + dwClientState_ViewAngles, newrcs.x)
            pm.write_float(engine_pointer + dwClientState_ViewAngles + 0x4, newrcs.y)
    else:
        oldpunch.x = 0.0
        oldpunch.y = 0.0
        newrcs.x = 0.0
        newrcs.y = 0.0
    return oldpunch
