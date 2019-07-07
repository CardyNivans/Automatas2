# Realice un programa en Python que permita capturar en una 
# lista las calificaciones de N alumnos y que le permita calcular e imprimir lo siguiente:
# 1.-El promedio general de los alumnos
# 2.-Numero de alumnos aprobados y número de alumnos reprobados (Si el alumno sacó una calificación menor a 70 se considera reprobado)
# 3.-Porcentaje de alumnos aprobados y reprobados.
# 4.-Número de alumnos cuya calificación fue mayor a 80



Alumnos = []

def main():
    ciclo = True
    while ciclo == True:
        nota = input ("Introduce la calificación: ")
        Alumnos.append(nota)
        print("\n")
        resp = input ("Desea capturar otra calificación? (S/N)")

        if (resp == "S" or resp == "s"):
            ciclo = True
        elif (resp == "N" or resp == "n"):
            ciclo = False
    ciclo = True
    while ciclo == True: 
        print ("Qué desea saber? ")
        print ("1.- El promedio general de los alumnos ")
        print ("2.- Número de alumnos aprobados y reprobados ")
        print ("3.- Porcentaje de alumnos reprobados y aprobados ")
        print ("4.- Número de alumnos cuya calificación fue mayor a 80 ")
        print ("5.- Salir ")

        opc = int (input ("Introduce tu opcion "))
        if (opc == 1):
            fProm(Alumnos)
            

def fProm(Alumnos):
    sSuma = 0
    if len(Alumnos)>0:
    	for i in Alumnos:
	       sSuma += i
    	return sSuma / len(Alumnos)
    else:
	    return 0

if __name__ == "__main__":
    
    main()