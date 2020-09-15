import pyautogui as pg
from time import sleep
import math
pi = math.pi

def circle_rel(r,n=90):
    arr = [[r, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    cir =  [[int(math.cos(2*pi/n*x)*r),int(math.sin(2*pi/n*x)*r)] for x in range(0, n+1)]
    for i in range(len(cir)-1):
        arr.append([cir[i+1][0] - cir[i][0], cir[i+1][1] - cir[i][1]])
    for i in range(len(cir)-n//2):
        arr.append([cir[i+1][0] - cir[i][0], cir[i+1][1] - cir[i][1]])
    return arr

def circle(r):
    arr = circle_rel(r)
    for i in range(len(arr)):
        pg.moveRel(arr[i][0], arr[i][1], duration=0.1)

sleep(10)
circle(250)
