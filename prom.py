# Realice un programa en Python que permita capturar en una 
# lista las calificaciones de N alumnos y que le permita calcular e imprimir lo siguiente:
# 1.-El promedio general de los alumnos
# 2.-Numero de alumnos aprobados y número de alumnos reprobados (Si el alumno sacó una calificación menor a 70 se considera reprobado)
# 3.-Porcentaje de alumnos aprobados y reprobados.
# 4.-Número de alumnos cuya calificación fue mayor a 80



Alumnos = []

def main():
    cant = 1
    ciclo = True
    

    while ciclo == True:
        nota = int(input ("Introduce la calificación: "))
        Alumnos.append(nota)
        print("\n")
        resp = input ("Desea capturar otra calificación? (S/N)")

        if (resp == "S" or resp == "s"):
            ciclo = True
            cant =cant+1
        elif (resp == "N" or resp == "n"):
            ciclo = False
    ciclod = True
    while ciclod == True: 
        print ("Qué desea saber? ")
        print ("1.- El promedio general de los alumnos ")
        print ("2.- Número de alumnos aprobados y reprobados ")
        print ("3.- Porcentaje de alumnos reprobados y aprobados ")
        print ("4.- Número de alumnos cuya calificación fue mayor a 80 ")
        print ("5.- Salir ")

        opc = int (input ("Introduce tu opcion "))
        
        if (opc == 1):
            suma=0
            for i in Alumnos:
                suma=i+suma
            print ("El promedio es : ",suma/cant)

        elif (opc == 2):
            suma=0
            a = 0
            r = 0
            for i in Alumnos:
                suma=i+suma
                if (i < 70):
                    r = r+1
                else:
                    a = a+1
            print ("Alumnos Reprobados: ",r)
            print ("Alumnos Aprobados: ",a)

        elif (opc == 3):
            suma=0
            a = 0
            r = 0
            for i in Alumnos:
                suma=i+suma
                if (i < 70):
                    r = r+1
                else:
                    a = a+1
            print ("Porcentaje de Alumnos Reprobados: ",r/cant*100)
            print ("Porcentaje de Alumnos Aprobados: ",a/cant*100)
        
        elif (opc == 4):
            suma = 0
            o = 0
            for i in Alumnos:
                suma=i+suma
                if (i > 80):
                    o = o+1
            print("Número de alumnos cuya calificación es mayor a 80: ",o)

        elif (opc == 5):
            ciclod = False

            
                
            



if __name__ == "__main__":
    main()