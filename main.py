
import funciones as fn
import numpy as np 

filas = 10   
columnas= 4   

departamento = np.zeros((filas,columnas), dtype= object) # Array bidimensional que representará el departamento con sus 10 pisos y 4 tipos de departamento por piso.

listado_rut = []  # Listado para guardar los RUT de los compradores

flag = True

while flag == True:

    print("\n===== MENÚ =====")
    print("1. Comprar departamento")
    print("2. Mostrar departamentos disponibles")
    print("3. Ver listado de compradores")
    print("4. Mostrar ganancias totales")
    print("5. Salir\n")

    try:

        option= int(input("Ingrese la opción que desea : "))

        if option == 1:
            print( "Comprar departamento")
            
            flag_run = False
            while flag_run == False:
                run= int(input("Ingrese su run sin puntos ni digito verificador: "))
                flag_run, estado = fn.validar_rut(run, listado_rut)
                print(estado)

            flag_compra = False
            while flag_compra == False:
                print(departamento)
                piso= int(input("\nIngrese el N° del piso del departamento que desea :"))
                letra = input("Ingrese la letra del piso que desea (A - B - C - D) :")
                flag_compra, estado = fn.validar_departamento(piso, letra, departamento, filas, columnas, run, listado_rut)
                print(estado)   

        elif option ==2:
            print("Mostrar departamentos disponibles")
            print(departamento)

        elif option ==3:
            print("Ver listado de compradores")

            print(fn.listado_comprador(listado_rut))
            print()

        elif option ==4:
            print("Mostrar ganancias totales")
            estado_A, estado_B, estado_C, estado_D, estado_total = fn.ganancias_totales(departamento)
            print(f"\n{estado_A}\n{estado_B}\n{estado_C}\n{estado_D}\n{estado_total}\n")

        elif option == 5:      
            flag, estado = fn.salir(flag)
            print(estado)

        else:
            print("Ingrese un número entre 1 y 5\n")              

    except :     
        print("Ingrese un dato válido")

