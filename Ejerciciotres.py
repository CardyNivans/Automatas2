# Nombre: Ejerciciotres.py
# Objetivo: Ejercicio 3 de jupyter
# 
# Autor: Carlos Vázquez
# Fecha 4 Julio 2019



def main():
    nomina=0
    ciclo = 0
    while ciclo < 10:
        sueldo = float(input("Introduce sueldo :"))
        nomina = nomina + sueldo
        ciclo = ciclo+1
        
        print ("Total de nómina: ",nomina)



if __name__ == "__main__":
    main()