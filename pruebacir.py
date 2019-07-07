# Nombre: circunferencia.py
# Objetivo: Calcula el área y diámetro de una circunferencia e importar la libreria
# Math
# Autor: Carlos Vázquez
# Fecha 1 Julio 2019

import math as mat

#----------------------------------
# Función para calcular área 
#----------------------------------

def calculaArea(r):
    area = mat.pi*(mat.pow(r, 2))
    return area
    
#----------------------------------
# Función para calcular el diametro 
#----------------------------------
def calculaDiametro(d):
    diam = d * 2
    return diam

def main():
    ciclo = True
    while ciclo == True:
        print("--- Script para calcular área de circunferencia---")
        radio = float(input("Introduce el valor del radio:"))
        # Invocar a un método
        print("El área es: ", calculaArea(radio))
        print("El diámetro es: ", calculaDiametro(radio))

        resp = input ("Desea hacer otro cálculo: (s,n)?")
        if (resp == "S" or resp == "s"):
            ciclo = True
        else: 
            ciclo = False
    else:
        print("*** Fin del programa")

if __name__ == "__main__":
    main()