from Utils.Offsets import *
import time

def SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager, entity_glow):
    ratio = entity_hp / 100.0
    r, g, b = max(min(int(510 * (1 - ratio)), 255), 0), max(min(int(510 * ratio) - 255, 255), 0), 0
    if entity_team_id == 2 and (
            localTeam != 2) and not entity_dormant:
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A
        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)  # Enable
    elif entity_team_id == 3 and (
            localTeam != 3) and not entity_dormant:
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(r))  # R
        pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(g))  # G
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(b))  # B
        pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(255))  # A
        pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)  # Enable

def GetEntityVars(pm, entity):
    while True:
        try:
            entity_glow = pm.read_uint(entity + m_iGlowIndex)
            entity_team_id = pm.read_uint(entity + m_iTeamNum)
            entity_isdefusing = pm.read_uint(entity + m_bIsDefusing)
            entity_hp = pm.read_uint(entity + m_iHealth)
            entity_dormant = pm.read_uint(entity + m_bDormant)
        except Exception as e:
            time.sleep(0.2)
            continue
        return entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant
