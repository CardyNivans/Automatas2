# Nombre: Ejerciciodos.py
# Objetivo: Ejercicio 2 de jupyter
# Realice un programa en Python que dado como datos la categoría y el sueldo de un trabajor, 
# calcule el aumento correspondiente teniendo en cuenta la siguiente información e imprima el nuevo sueldo del trabajador:
#Categoría 1 : Aumento 15%
#Categoría 2 : Aumento 10%
#Categoría 3 : Aumento 8%
#Categoría 4 : Aumento 7%
# Autor: Carlos Vázquez
# Fecha 4 Julio 2019


def main():
    print ("--Calcula Incremento de sueldo --")
    print("\n")
    sueldo = float (input ("Introduce sueldo: "))
    cat = int (input ("Introduce categoría (1, 2, 3, 4)"))

    if (cat == 1):
        sueldo = sueldo*.15 + sueldo
    elif (cat == 2):
        sueldo = sueldo*.10 + sueldo
    elif (cat == 3):
        sueldo = sueldo*.8 + sueldo
    elif (cat == 4):
        sueldo = sueldo*.7 + sueldo
    print ("El sueldo del trabajador es : ",sueldo)
        


if __name__ == "__main__":
    main()