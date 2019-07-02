#Sumar 2 numeros 

def suma(num1,num2):
    return num1+num2


def multiplica(num1,num2):
    return num1+num2


def divide(num1,num2):
    return num1/num2
#Comparar numeros
def compara(num1,num2):
    if(num1>num2):
        print("El numero mayor es el No1: ",num1)
        
    elif(num2>num1):
        print("El mayor es el num2: ",num2)
        
    else:
        print(" Los numeros son iguales")
        
#Función para hacer un ciclo con for  
def cuenta(num1, num2):
    if (num2>=num1):
        for i in range(num1, num2+1):
            print ("valor de i:", i)

    if (num1>num2):
        for i in range(num1, num2+1)
            print ("valor de i:", i)

#Funcion main 
def main():
    ciclo = True
    while (ciclo == True):
        print ("Operaciones basicas con numeros enteros")
        print("\n")
        n1 = int( input("Introduce el primer numero"))
        n2 = int( input("Introduce el segundo numero"))
 
        print("La suma es: ",str(suma(n1, n2)))
        print("La multiplicacion es:",str(multiplica(n1, n2)))
        print("La division es:", str(divide(n1, n2)))
        compara(n1, n2)
        cuenta(n1, n2)

        cad = input("¿Desea hacer otro cálculo (s/n)? : ")
        if(cad == "S" or cad == "s"):
            ciclo = True
        else:
            ciclo = False

        
if __name__ == "__main__":
    main()




