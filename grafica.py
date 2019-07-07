#--------------------------------------------------------
# grafica.py
# objetivo: Hacer interfaz grafica python
# Autor: Carlos Vázquez
# Fecha: 5 de julio de 2019
#--------------------------------------------------------

import tkinter as tk 
#Importamos el tipo widget
from tkinter import Label
#Creamos la ventana
root = tk.Tk()
#Modificamos el tamaño de la ventana
root.geometry("800x800")
#Creamos la etiqueta
widget = Label(None, text = "Hola mundo tkinter")
#Agregamos la etiqueta a la ventana
widget.pack()
#Ciclo de espera de eventos
root.mainloop()