# Necesita una cantidad considerable de correcciones para que devuelva EXACTAMENTE la longitud de lína que quiero
import csv, sys

def menu_item_separator(nombres, precios, desc):
    sep = int(sys.argv[1]) - 2*len(str(max(list(map(int, precios))))) - 4
    res = []
    f = ""
    aux = 0
    for i in range(len(nombres)):
        aux = 5 - len(str(precios[i]))
        if nombres[i] == "" or nombres[i] == "Nombre": 
            #sep = int(50) - 2*len(str(max(list(map(int, precios))))) - 4
            res.append("")
            continue
        if nombres[i][0] == "-": nombres[i] = nombres[i][1:].strip()
        f = nombres[i][0].upper() + nombres[i][1:].casefold() + "."*(sep - len(nombres[i])+len(precios[i])+aux) + "$" + precios[i] + ".00"
        res.append(f)
        if desc[i] != "": 
            if len(desc[i])+2 > sep-10:
                x = desc[i][sep-5:].find(" " or ")")
                res.append("(" + desc[i][:sep-5+x] + (")" if len(desc[i][sep-4+x:]) == 0 else ""))
                if len(desc[i][sep-4+x:]) > 0: res.append(desc[i][sep-4+x:] + ")")
            else: res.append("(" + desc[i] + ")")
    print("|||||||||||||||||||||||||||||||||||||||||") # Y quiero que esto se ajuste a la longitud máxima sep
    return "\n".join(res)

def start():
    name = []
    price = []
    desc = []

    with open('formato_menu_automatizado - Sheet1.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name.append(row[0])
            if row[1] == "" or row[1] == "Precio": price.append(0)
            else: price.append(row[1])
            desc.append(row[2])

    print(menu_item_separator(name, price, desc))
    
start()