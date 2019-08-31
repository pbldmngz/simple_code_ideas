# Necesita una cantidad considerable de correcciones para que devuelva EXACTAMENTE la longitud de lína que quiero
def menu_item_separator(nombres, precios, sep):
    sep = int(sep) - 2*len(str(max(list(map(int, precios))))) - 4
    res = []
    f = ""
    aux = 0
    for i in range(len(nombres)):
        aux = 5 - len(precios[i])
        if nombres[i][0] == "-": nombres[i] = nombres[i][1:].strip()
        f = nombres[i][0].upper() + nombres[i][1:].casefold() + "."*(sep - len(nombres[i])+len(precios[i])+aux) + "$" + precios[i] + ".00"
        res.append(f)
    print("|||||||||||||||||||||||||||||||||||||||||") # Y quiero que esto se ajuste a la longitud máxima sep
    return "\n".join(res)

def start():
    cantidad = input("Cantidad de productos: ")
    cantidad = int(cantidad)
    name = []
    price = []

    while True:
        while(cantidad > 0):
            name.append(input("nombre: ").strip())
            price.append(input("precio: "))
            cantidad -= 1
            print("_._._._._._._._._._._._._._._._._._._._._")
        print(menu_item_separator(name, price, sep = input("¿Cuánta separación quieres? ")))
        print("|||||||||||||||||||||||||||||||||||||||||")
        if input("¿Desea cambiar la separación? (Y/N) ").casefold() != "y":
            break
    
start()