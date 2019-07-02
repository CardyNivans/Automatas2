# Nombre: Factorial.py
# Objetivo: Obtener el factorial de un numero
# Math
# Autor: Carlos Vázquez
# Fecha 1 Julio 2019

#Importamos la libreria Math
import math as mat 

#------------------------------------------------
# Función para obtener el factorial de un numero
#------------------------------------------------
def fact(n):
   x =  mat.factorial(n)
   return x





def main():
    n = int(input ("Ingrese el número del que quiere sacar el factorial"))
    print("El factorial es: ",fact(n))

    

if __name__ == "__main__":
    main()
