import pyautogui as pg
from time import sleep, clock
sleep(3)
#tic = clock()
def flatline():
    arr = [[0, 0],[17, 105], [1, 43], [36, 62], [26, 37], [23, 61], [-3, 41], [-6, 22], [-47, 6], [-17, -19], [-10, 13], [-15, 41], [7, 12], [35, 20], [24, -7], [31, -9], [25, 4], [-7, 38], [10, 29], [35, 36], [29, 2], [26, 6], [4, 39], [-17, 11], [-25, 6], [-37, 16], [-27, 12], [-16, -24], [-30, 25], [-11, 28]]
    for i in range(30):
        pg.moveRel(arr[i][0], arr[i][1], duration=0.1)

#toc = clock()
#print(toc - tic)



