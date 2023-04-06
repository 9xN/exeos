import ctypes
import keyboard, mouse
from Utils.get_netvars import *

keylist = ["space", "tab", "capslock"]

def GetWindowText(handle, length=100):
    user32 = ctypes.windll.user32
    window_text = ctypes.create_string_buffer(length)
    user32.GetWindowTextA(
        handle,
        ctypes.byref(window_text),
        length
    )
    return window_text.value

def GetForegroundWindow():
    user32 = ctypes.windll.user32
    return user32.GetForegroundWindow()

def strtobool(string):
    return string.lower() in ("true", 1)

def is_key(string):
    if keyboard.is_modifier(string) or (string.isalpha() and len(string) == 1) or string in keylist:
        return True
    else:
        return False

def is_mouse(string):
    list = ["left", "right", "middle", "wheel", "mouse4", "mouse5"]
    if string in list:
        return True
    else:
        return False

def is_pressed(key):
    if is_key(key):
        return keyboard.is_pressed(key)
    elif is_mouse(key):
        if key == "mouse4":
            return mouse.is_pressed("x")
        elif key == "mouse5":
            return mouse.is_pressed("x2")
        else:
            return mouse.is_pressed(key)
    else:
        return False
