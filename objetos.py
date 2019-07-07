# Nombre: Ejerciciotres.py
# Objetivo: Ejercicio 5 de jupyter
# Ejercicio # 5: Realice un programa en python que permita almacenar en un diccionario los datos generales de un alumno del ITC.
# Deberá poder imprimir cada uno de éstos datos a través de la clave del diccinario y modificar al 
# menos uno de los datos (ej. número telefónico).
# Autor: Carlos Vázquez
# Fecha 4 Julio 2019

class Punto(object):
    # Constructor de la clase
    def __init__(self,valorX,ValorY):
        self.x= valorX
        self.y= ValorY
    
    #Métodos Get
    def getX(self):
        return self.x 

    def getY(self):
        return self.y


    #Métodos Set
    def SetX(self,valorX):
        self.x = valorX

    def SetY(self,valorY):
        self.x = valorY

    def toString(self):
        return "El punto tiene las siguientes coordenadas: ",self.x,",",self.y
    
def main():
    #Programa principal
    p1 = Punto(2,3)
    print(p1.toString())

    #Creamos el objeto p2
    p2 = Punto(0,0)
    #Invocamos a los métodos set
    p2.SetX(-2)
    p2.SetY(-4)
    print(p2.toString())

if __name__ == "__main__":
    main()

    