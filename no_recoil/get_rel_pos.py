arr = [[887, 278], [904, 383], [905, 426], [941, 488], [967, 525], [990, 586], [987, 627], [981, 649], [934, 655], [917, 636], [907, 649], [892, 690], [899, 702], [934, 722], [958, 715], [989, 706], [1014, 710], [1007, 748], [1017, 777], [1052, 813], [1081, 815], [1107, 821], [1111, 860], [1094, 871], [1069, 877], [1032, 893], [1005, 905], [989, 881], [959, 906], [948, 934]]
flat = [
        [0, 0],
        [-11, -14],
        [6, -18],
        [-6, -12],
        [-14, -12],
        [-5, -13],
        [-2, -11],
        [2, -11],
        [22, -2],
        [9, 1],
        [4, -14],
        [-3, -7],
        [-9, -6],
        [-9, 3],
        [-12, -1],
        [-11, -2],
        [-9, -7],
        [-1, -9],
        [-1, -13],
        [-9, -5],
        [-9, -5],
        [-6, -8],
        [5, -10],
        [14, 0],
        [16, -2],
        [9, -2],
        [9, -5],
        [8, -6],
        [8, -10],
        [2, -12]
      ]

r99 = [
        [0, 0],
        [1, -9],
        [-1, -8],
        [-5, -8],
        [5, -9],
        [3, -15],
        [7, -8],
        [3, -12],
        [3, -8],
        [-1, -11],
        [0, -8],
        [-7, -7],
        [2, -11],
        [-4, -7],
        [-2, -6],
        [6, -1],
        [3, -5],
        [5, 2]
      ]

r301 = [
        [0, 0],
        [5, -13],
        [2, -12],
        [-3, -9],
        [5, -10],
        [2, -7],
        [3, -10],
        [1, -4],
        [4, -3],
        [3, -6],
        [-1, -1],
        [1, -2],
        [1, -4],
        [-5, -4],
        [-2, -6],
        [-2, -3],
        [-5, -3]
      ]

p45 = [
        [0, 0],
        [0, -7],
        [3, -7],
        [6, -7],
        [0, -10],
        [5, -7],
        [6, -6],
        [6, -5],
        [4, -5],
        [5, -1],
        [6, -5],
        [7, -1],
        [-4, -6],
        [4, -5],
        [5, -5]
      ]

alt = [
        [0, 0],
        [-7, -12],
        [7, -14],
        [-6, -16],
        [9, -13],
        [-7, -16],
        [4, -12],
        [-4, -9],
        [6, -10],
        [-5, -9],
        [9, -6],
        [-6, -6],
        [10, -2],
        [-5, -3],
        [5, -1],
        [-9, -6]
      ]

def presonal_subs(a, b):
    return [b[0] - a[0], b[1] - a[1]]

def multiplier(x):
    m = 9/16
    return [int(x[0]*m), int(x[1])]

def foo(m):
    mult = 1
    return [m[0]*mult, m[1]*mult]

print(list(map(foo, alt)))

#print([presonal_subs(arr[i-1], arr[i]) for i in range (1, 30)])

#print(list(map(multiplier, [presonal_subs(flat[i-1], flat[i]) for i in range (1, 30)])))

#print(list(map(multiplier, flat)))

#res = [[0, 0], [17, 105], [1, 43], [36, 62], [26, 37], [23, 61], [-3, 41], [-6, 22], [-47, 6], [-17, -19], [-10, 13], [-15, 41], [7, 12], [35, 20], [24, -7], [31, -9], [25, 4], [-7, 38], [10, 29], [35, 36], [29, 2], [26, 6], [4, 39], [-17, 11], [-25, 6], [-37, 16], [-27, 12], [-16, -24], [-30, 25], [-11, 28]]

#(a, b) = ([i[0] for i in res], [i[1] for i in res])

# a = [0, 17, 1, 36, 26, 23, -3, -6, -47, -17, -10, -15, 7, 35, 24, 31, 25, -7, 10, 35, 29, 26, 4, -17, -25, -37, -27, -16, -30, -11]
# b = [0, 105, 43, 62, 37, 61, 41, 22, 6, -19, 13, 41, 12, 20, -7, -9, 4, 38, 29, 36, 2, 6, 39, 11, 6, 16, 12, -24, 25, 28]



#Aquí comenzó todo :)