from os import walk, getcwd, listdir, makedirs
def counter(path, dotTypes):
    arr = recSearch(path, dotTypes)

    total = 0
    counter = []
    for p in arr:
        secCounter = 0
        file = open(p, "r+", encoding="utf8")
        #print(f"len = {len(file)}")
        for i in file:
            secCounter += 1
        counter.append((p.split("\\")[-1], secCounter))
        #counter.append((p, secCounter))
        file.close()
    
    for p, x in counter:
        total += x

    print(counter)
    print(f"Total lines of code: {total}")

def recSearch(path, dotTypes):
    pathArr = []

    for (dirpath, dirnames, filenames) in walk(path):
        for f in filenames:
            if "." in f"{dirpath}\{f}":
                if f"{dirpath}\{f}".split(".")[-1] in dotTypes:
                    pathArr.append(f"{dirpath}\{f}")
    return pathArr

#dotTypes = ["py", "pyw", "css", "txt", "js", "xml", "xlst", "html", "md", "ino"]
dotTypes = ["py", "pyw"]
counter(r"C:\Users\coffe\Documents\GitHub\Milwaukee", dotTypes)
#print(recSearch(r"C:\Users\coffe\Documents\GitHub\simple_projects"))