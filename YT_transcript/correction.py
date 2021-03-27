d = open("original.txt", "r")

arr = []
for id, n in enumerate(d):
    if id%2 != 0:
        arr.append(n[:-1])

print(arr)

file = open("output.txt", "w+")
file.write(" ".join(arr))
