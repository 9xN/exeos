from Utils.Offsets import *

def getClassID(pm, entity):
    buf = pm.read_int(entity + 8)
    buf = pm.read_int(buf + 2 * 4)
    buf = pm.read_int(buf + 1)
    buf = pm.read_int(buf + 20)
    return buf

def Chams(pm, engine, entity, entityTeam, entityHP, first, localPlayer):
    localTeam = pm.read_int(localPlayer + m_iTeamNum)
    if entity and entity != 0:
        if getClassID(pm, entity) == 40:
            ratio = entityHP / 100.0
            Argb = [int(255 * (1 - ratio)), int(255 * ratio), 0]
            Ergb = [int(255 * (1 - ratio)), int(255 * ratio), 0]
            if entityTeam == localTeam and entityTeam != 0 and entity != localPlayer:
                pm.write_uchar(entity + 112, Argb[0])
                pm.write_uchar(entity + 113, Argb[1])
                pm.write_uchar(entity + 114, Argb[2])
            if entityTeam != localTeam and entityTeam != 0 and entity != localPlayer:
                pm.write_uchar(entity + 112, Ergb[0])
                pm.write_uchar(entity + 113, Ergb[1])
                pm.write_uchar(entity + 114, Ergb[2])

            if first:
                buf = 1084227584
                point = pm.read_int(engine + model_ambient - 44)
                xored = buf ^ point
                pm.write_int(engine + model_ambient, xored)

def ResetChams(pm, engine, entity, entityTeam, localPlayer):
    if entity and entity != 0:
        if getClassID(pm, entity) == 40:
            if entityTeam != 0 and entity != localPlayer:
                pm.write_uchar(entity + 112, 255)
                pm.write_uchar(entity + 113, 255)
                pm.write_uchar(entity + 114, 255)
            b = 0
            pointer = pm.read_int(engine + model_ambient - 44)
            xo = b ^ pointer
            pm.write_int(engine + model_ambient, xo)
