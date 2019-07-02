# Nombre: Triangulo.py
# Objetivo: Identificar el tipo de triangulo de acuerdo al valor de sus lados
# Math
# Autor: Carlos Vázquez
# Fecha 1 Julio 2019

#------------------------------------------------
# Función para identificar el tipo de triángulo
#------------------------------------------------

def identificaT(l1,l2,l3):
    #Equilátero
    if (l1 == l2 and l1 == l3):
        print ("El triangulo es equilatero ",l1,",",l2,",",l3)
        print ("El perímetro es : ",l1+l2+l3)
    elif(l1 == l2 and l1 != l3 or l1 == l3 and l2 != l1):
        print ("El triangulo es isóseles ",l1,",",l2,",",l3)
        print ("El perímetro es : ",l1+l2+l3)
    elif(l1 != l2 and l1 != l3 and l3 != l2):
        print ("El triángulo es escaleno ",l1,",",l2,",",l3)
        print ("El perímetro es : ",l1+l2+l3)

def main():
    print("--- Script para identificar triangulos ---")
    lado1 = float(input ("Introduce el valor del lado número 1 "))
    lado2 = float(input ("Introduce el valor del lado número 2 "))
    lado3 = float(input ("Introduce el valor del lado número 3 "))
    
    identificaT(lado1,lado2,lado3)

if __name__ == "__main__":
    main()