import pyautogui as pg
from pynput import mouse
n = 0
b = True
array = []
def on_move(x, y):
    #print('Pointer moved to {0}'.format((x, y)))
    pass

def on_click(x, y, button, pressed):
    global n
    global b
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    b = not b
    if b: 
        array.append(list(pg.position()))
        n += 1
    if not pressed and n == 50:
        # Stop listener
        print(array)
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()

#m.Listener.start()

#on_click()

#results = [[887, 278], [904, 383], [905, 426], [941, 488], [967, 525], [990, 586], [987, 627], [981, 649], [934, 655], [917, 636], [907, 649], [892, 690], [899, 702], [934, 722], [958, 715], [989, 706], [1014, 710], [1007, 748], [1017, 777], [1052, 813], [1081, 815], [1107, 821], [1111, 860], [1094, 871], [1069, 877], [1032, 893], [1005, 905], [989, 881], [959, 906], [948, 934]]