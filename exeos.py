import threading, time, ctypes, argparse
from Utils.PlayerVars import *
from Utils.Vector3 import Vec3
from Utils.Bhop import Bhop
from Utils.Chams import Chams, ResetChams
from Utils.Triggerbot import shootTrigger
from Utils.Utilities import GetWindowText, GetForegroundWindow, is_pressed
from Utils.WallhackFunctions import SetEntityGlow, GetEntityVars
from Utils.rcs import rcse

def main():
    triggerkey = "mouse4"
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--legit', action='store_true', help='Enable legit mode')
    args = parser.parse_args()
    try:
        pm = pymem.Pymem("csgo.exe")
    except Exception as e:
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)  
        quit(0)
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
    engine_pointer = pm.read_uint(engine + dwClientState)
    cham = False
    oldpunch = Vec3(0, 0, 0)
    newrcs = Vec3(0, 0, 0)
    punch = Vec3(0, 0, 0)
    rcs = Vec3(0, 0, 0)
    First = True
    while True:
        time.sleep(0.0005)
        try:
            if not GetWindowText(GetForegroundWindow()).decode(
                    'cp1252') == "Counter-Strike: Global Offensive - Direct3D 9":
                time.sleep(1)
                continue
            pm.write_uchar(engine + dwbSendPackets, 1)
            player = pm.read_uint(client + dwLocalPlayer)
            if client and engine and pm:
                try:
                    player, engine_pointer, glow_manager, crosshairid, getcrosshairTarget, immunitygunganme,\
                    localTeam, crosshairTeam, y_angle = GetPlayerVars(pm, client, engine, engine_pointer)
                except Exception as e:
                    time.sleep(2)
                    continue
            if is_pressed("space"):
                Bhop(pm, client, player)
            if is_pressed(triggerkey):
                shootTrigger(pm, crosshairid, client, localTeam, crosshairTeam, triggerkey)
            oldpunch = rcse(pm, player, engine_pointer, oldpunch, newrcs, punch, rcs)
            if not args.legit:
                cham = False
                First = True
                flash_value = player + m_flFlashMaxAlpha
                if flash_value:
                    pm.write_float(flash_value, float(0))
                for i in range(0, 64):
                    entity = pm.read_uint(client + dwEntityList + i * 0x10)
                    if entity:
                        entity_glow, entity_team_id, entity_isdefusing, entity_hp, entity_dormant = GetEntityVars(pm, entity)
                        SetEntityGlow(pm, entity_hp, entity_team_id, entity_dormant, localTeam, glow_manager, entity_glow)
                        pm.write_int(entity + m_bSpotted, 1)
                        Chams(pm, engine, entity, entity_team_id, entity_hp, First, player)
                        First = False
                        # if cham:
                        #     ResetChams(pm, engine, entity, entity_team_id, player)
                    cham = True
        except Exception as e:
            continue

if __name__ == "__main__":
    print("""\033[91m
                                ┌─┐╲ ╱┌─┐┌─┐┌─┐
                                ├─  ╳ ├─ │ │└─┐
                                └─┘╱ ╲└─┘└─┘└─┘   
               ┌──────────────────────────────────────────────────┐ 
       ┌───────┤                \033[95mCredits: \033[94mgithub/9xN\033[91m               ├───────┐
       │       └──────────────────────────────────────────────────┘       │
       │      \033[93m$ \033[38;5;147mpython3 exeos.py -l \033[92mor\033[38;5;147m --legit \033[92mto enable stealthy mode\033[91m    │
       └──────────────────────────────────────────────────────────────────┘
        \033[0m""")
    threading.Thread(target=main).start()
else:
    print("Program Is not allowed to be ran, by other programs!")
    quit(0)
