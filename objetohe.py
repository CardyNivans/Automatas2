#--------------------------------------------------------
# objetoshe.py
# objetivo: Muestra el manejo de clases en python
# Autor: Carlos Vázquez
# Fecha: 5 de julio de 2019
#--------------------------------------------------------
import math as mat

class Punto(object):
    
    #Constructor de la clase
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # Metodos GET
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    #Metodos set
    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y
        
    def toString(self):
        return "El punto tiene las siguientes coordenadas: ",self.x,",",self.y


class Circunferencia(Punto):
    def __init__(self, valorRadio):
        self.radio = valorRadio

    def getRadio(self):
        return self.radio
    
    def setRadio(self,valorRadio):
        self.radio = valorRadio

    def getArea(self):
        return mat.pi * mat.pow(self.getRadio(), 2)

    def toString(self):
        return "La circunferencia tiene como centro: ", self.getX(), ", ", self.getY(),",",self.getRadio(),"El área es: ", self.getArea()

#Escriba la clase de cilindro que hereda de circunferencia, crea un objeto p4 y escribir en la clase cilindro 
#un método llamado calcularvolumen

def main():
    
    #Creamos objeto p1
    p1=Punto(2,3)
    print(p1.toString())
    
    #Creamos un objeto p2
    p2=Punto(0,0)
    print(p2.toString())
    #Invocamos al metodo set
    p2.setX(-2)
    p2.setY(-4)
    print(p2.toString())

    p3 = Circunferencia(12.34)
    p3.setX(10)
    p3.setY(12)
    print(p3.toString())


if __name__ == "__main__":
    main()