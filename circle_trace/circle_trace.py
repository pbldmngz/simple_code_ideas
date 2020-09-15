import math, sys, pyautogui as pg
from time import sleep

pi = math.pi

def circle_rel(r, n):
    arr = [[r, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    cir =  [[int(math.cos(2*pi/n*x)*r),int(math.sin(2*pi/n*x)*r)] for x in range(0, n+1)]
    for i in range(len(cir)-1):
        arr.append([cir[i+1][0] - cir[i][0], cir[i+1][1] - cir[i][1]])
    for i in range(len(cir)-n//2):
        arr.append([cir[i+1][0] - cir[i][0], cir[i+1][1] - cir[i][1]])
    return arr

def circle(r, t=10, n=90):
    sleep(float(t))
    arr = circle_rel(int(r), int(n))
    for i in range(len(arr)):
        pg.moveRel(arr[i][0], arr[i][1], duration=0.1)

if __name__ == '__main__':
    if len(sys.argv) == 3: globals()[sys.argv[1]](sys.argv[2])
    if len(sys.argv) == 4: globals()[sys.argv[1]](sys.argv[2], sys.argv[3])
    if len(sys.argv) == 5: globals()[sys.argv[1]](sys.argv[2], sys.argv[3], sys.argv[4])
