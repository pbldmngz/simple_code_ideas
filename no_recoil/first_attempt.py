import sys
import pyautogui as pg
from pynput import mouse
from time import sleep, clock
from threading import Thread 

arr = [[0, 0],[17, 105], [1, 43], [36, 62], [26, 37], [23, 61], [-3, 41], [-6, 22], [-47, 6], [-17, -19], [-10, 13], [-15, 41], [7, 12], [35, 20], [24, -7], [31, -9], [25, 4], [-7, 38], [10, 29], [35, 36], [29, 2], [26, 6], [4, 39], [-17, 11], [-25, 6], [-37, 16], [-27, 12], [-16, -24], [-30, 25], [-11, 28]]
active = False
running = True

def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    pass

def on_click(x, y, button, pressed):
    global active
    global running
    running = True
    
    if not pressed:
        running = False
    else:
        #print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
        tic = clock()

        if active == True:
            n = 0
            while n < 30:
                print("Vuelta n° {}".format(n+1))
                #sleep(0.1)
                if running:
                    pg.moveRel(arr[n][0], arr[n][1], 0.1)
                else:
                    print("ya sale")
                n += 1
        toc = clock()
        print(tic - toc)

def on_scroll(x, y, dx, dy):
    global active
    if dy > 0: 
        active = not active
        print('Spectra_flatline {0}'.format('ACTIVADO' if active else 'DESACTIVADO'))

with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
