import calc
from tkinter import *
#Ventana
root = Tk()
frame = Frame(root)
root.config(background = "#8F8F97")
root.title("eval calculator")
frame.config(background = "#8F8F97")
frame.pack()
#Variables
labelfont = ('times', 20)
texto = StringVar()
#Funciones
def texto_pantalla(n):
    texto.set(texto.get() + n)
def clear():
    texto.set("")
def resultado():
    try:
        texto.set(calc.calc(texto.get()))
    except: texto.set("Ha ocurrido un error")
#Pantalla
pantalla = Entry(frame, textvariable = texto)
pantalla.grid(row = 1, column = 1, columnspan = 4)
pantalla.config(background = "#8F8F97", fg = "#FFFFFF",  width = 36, font = labelfont)
#Botones #FILA 1
boton7 = Button(frame, text = "7", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("7"))
boton7.grid(row = 2, column = 1)
boton8 = Button(frame, text = "8", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("8"))
boton8.grid(row = 2, column = 2)
boton9 = Button(frame, text = "9", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("9"))
boton9.grid(row = 2, column = 3)
botonCE = Button(frame, text = "CE", width = 8, height = 3, font = labelfont, command = lambda: clear())
botonCE.grid(row = 2, column = 4)

#Botones #FILA 2
boton4 = Button(frame, text = "4", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("4"))
boton4.grid(row = 3, column = 1)
boton5 = Button(frame, text = "5", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("5"))
boton5.grid(row = 3, column = 2)
boton6 = Button(frame, text = "6", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("6"))
boton6.grid(row = 3, column = 3)
botonp1 = Button(frame, text = "(", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla("("))
botonp1.grid(row = 3, column = 4)
#Botones #FILA 3
boton1 = Button(frame, text = "1", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("1"))
boton1.grid(row = 4, column = 1)
boton2 = Button(frame, text = "2", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("2"))
boton2.grid(row = 4, column = 2)
boton3 = Button(frame, text = "3", width = 8, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: texto_pantalla("3"))
boton3.grid(row = 4, column = 3)
botonp2 = Button(frame, text = ")", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla(")"))
botonp2.grid(row = 4, column = 4)
#Botones #FILA 4
botonSum = Button(frame, text = "+", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla("+"))
botonSum.grid(row = 5, column = 1)
botonRes = Button(frame, text = "-", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla("-"))
botonRes.grid(row = 5, column = 2)
botonMult = Button(frame, text = "*", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla("*"))
botonMult.grid(row = 5, column = 3)
botonpDiv = Button(frame, text = "/", width = 8, height = 3, font = labelfont, command = lambda: texto_pantalla("/"))
botonpDiv.grid(row = 5, column = 4)
#Botones #FILA 5
botonEnter = Button(frame, text = "ENTER", width = 34, height = 3, background = "#000", fg = "#FFFFFF", font = labelfont, command = lambda: resultado())
botonEnter.grid(row = 6, column = 1, columnspan = 4)

#End
root.mainloop()