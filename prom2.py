# Nombre: Ejerciciotres.py
# Objetivo: Ejercicio 5 de jupyter
# Ejercicio # 5: Realice un programa en python que permita almacenar en un diccionario los datos generales de un alumno del ITC.
# Deberá poder imprimir cada uno de éstos datos a través de la clave del diccinario y modificar al 
# menos uno de los datos (ej. número telefónico).
# Autor: Carlos Vázquez
# Fecha 4 Julio 2019


def main():
    
    datos_Alumno = {
        "Nombre":"Carlos",
        "Apellidos":"Vázquez, González",
        "Fecha_nacimiento":"29/01/2019",
        "Lugar_nacimiento":"Colima",
        "Nacionalidad":"Mexicana",
        "Telefono":"3121312377",
        "Semestre":"6",
    }

    print("\n.::: Elementos del diccionario: ::.")
    for clave, valor in datos_Alumno.items():
        print(clave + ": " + valor)

    print("\n.::: Llaves del diccionario: ::.")
    for clave in datos_Alumno.keys():
        print(clave)

    print("\n.::: Valores del diccionario: ::.")  
    for valores in datos_Alumno.values():
        print(valores)
    
    print("\n.::: Modificamos el nombre de Carlos por Miguel: ::.") 
    print("\n.::: Modificamos el Semestre de 6 a 7: ::.")  
    datos_Alumno["Nombre"] = 'Miguel'
    datos_Alumno["Semestre"] = '7'
    for clave, valor in datos_Alumno.items():
        print(clave + ": " + valor)

if __name__ == "__main__":
    main()