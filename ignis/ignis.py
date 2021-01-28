import sounddevice as sd
import numpy as np
import keyboard

bal = 0
temp = -1

def press_hotkey(b):
    if b == 0:
        keyboard.press_and_release('alt+1')
    elif b == 1:
        keyboard.press_and_release('alt+2')
    elif b == 2:
        keyboard.press_and_release('alt+3')
    elif b == 3:
        keyboard.press_and_release('alt+4')

def apply(vn, max, min, b):
    global bal
    global temp
    if (vn < max) and (vn >= min):
        if bal != b:
            if temp == b:
                bal = b
                temp = -1
                print(b)
                press_hotkey(b)
            else: temp = b

def effect(vn):
    global bal
    #print(vn)
    apply(vn, 0.5, 0, 0)
    apply(vn, 20, 0.5, 1)
    apply(vn, 45, 20, 2)
    apply(vn, 200, 45, 3)

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    #print(volume_norm)
    effect(volume_norm)
    #print ("|" * int(volume_norm))

with sd.Stream(callback=print_sound):
    sd.sleep(100000)