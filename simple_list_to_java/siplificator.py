#Transforma un montón de palabras sueltas en algo que se puede copiar y pegar en un arreglo
#\n automatiza el proceso de pegado haciendo que se puedan pegar 200 palabras de un tirón

def main():
    string = []

    for i in range(int(input("Number of items: "))):
        x = input("object: \n")
        for n in range(len(x.split(" "))):
            string.append(x.split(" ")[n])

    res = []
    for i in range(len(string)):
        try: int(string[i])
        except: res.append('"' + string[i].title() + '"')
    return ', '.join(res)

print(main())