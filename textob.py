# Script para simular una calculador básica
#Escribir u nscript python con la librera
#Una caja de texto
#Un boton para imprimir un mensaje en la caja de texto
#Un boton para borrar el texto
#Un boton para salir

import tkinter as tk
from tkinter import *





#Funcion para imprimir
def Texto():
    texto = txtC1.get()
    print(": ",texto)


def Borrar():
    txtC1.delete(0,tk.END)


# Funcion para salir de la app
def salir():
    wv.destroy()


# Programa principal 

# Creamos las ventana
wv = tk.Tk()
# Modificamos el tamaño de la ventana
wv.geometry("500x400")
# Titulo de la ventana
wv.title("Tkinter con Texto")

# Creamos la etiqueta
l1 = Label(None, text="Ingrese el texto que quiere: ")

#Creamos los botones
bt = Button(None, text= 'Imprimir', command=Texto)
bq = Button(None, text= 'Salir', command=salir)
bb = Button(None, text= 'Borrar', command=Borrar)


# creamos los campos de texto
txtC1 = Entry(wv)

# Alineamos los widgets
l1.grid(row=1, column=10)

# campos de texto
txtC1.grid(row = 1, column=15)
# Botones
bt.grid(row = 4, column=10)
bq.grid(row = 4, column=35)
bb.grid(row = 4, column = 55 )

# Ciclo de espera de eventos
wv.mainloop()