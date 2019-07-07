# Nombre: listas.py
# Objetivo: Muestra el funcionamiento de las listas en python
# Math
# Autor: Carlos Vázquez
# Fecha 2 Julio 2019
lista = []
    

#------------------------------------------------
# Función para agregar items a la lista
#------------------------------------------------

def agregaItem(dato):
    lista.append(dato)
#------------------------------------------------
# Función para agregar items a la lista
#------------------------------------------------
def imprimirLista():
    j=1
    for i in lista:
        print("Item: ",j,",",i)
        j+=1
#------------------------------------------------
# Función para remover items de la lista
#------------------------------------------------
def eliminarItem(dato):
    #Buscamos el item
    if (dato in lista):
        lista.remove(dato)
        print ("Dato eliminado...")
    else:
        print("Elemento no existe en la lista...")


# Parte principal del Script
def main():
    opc=0
    ciclo = True
    while ciclo == True:
        print("--- Script para trabajar con Listas ----")
        print("1.- Agregar elementos a la lista")
        print("2.- Buscar un elemento en la lista")
        print("3.- Modificar un elemento en la lista")
        print("4.- Eliminar un eleento de la lista")
        print("5.- Imprimir los elementos de la lista")
        print("6.- Salir")

        opc = int (input("Elija una opcion entre 1 y 6"))

        if (opc == 1 ):
            item = input ("Introduce valor del elemento")
            agregaItem(item)
    #elif (opc == 2 ):
    
    #elif (opc == 3 ):

    #elif (opc == 4 ):

        elif (opc == 5 ):
            imprimirLista()
        elif (opc == 6 ):
            print("**Fin del programa")
            ciclo = False
        else:
            print("Selecciona un entero entre 1 y 6")

    

if __name__ == "__main__":
    main()