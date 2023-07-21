
def validar_rut(run, listado_rut):

    if len(str(run)) == 8:
        estado = f"Run {run} es correcto\n"
        return True, estado   
    else:
        estado = "El largo del run debe ser de 8 digitos\n"
        return False, estado
    
    
#Esta función valida la compra de un departamento y asigna un RUN a un departamento en una matriz llamada departamento, representada por las variables filas y columnas. También se utiliza una letra  para identificar el tipo de departamento (A, B, C o D). Si el piso (piso) está entre 1 y 10, verifica si el departamento está disponible (no vendido), y si es así, asigna el RUT al departamento y lo agrega a la lista de RUTs vendidos (listado_rut). Devuelve un valor booleano True junto con un mensaje de estado si se pudo realizar la compra correctamente, y en caso contrario, devuelve False junto con un mensaje de estado que indica el problema.  
def validar_departamento(piso, letra, departamento, filas, columnas, run, listado_rut):
    
    tipo= 0
    if letra.upper() == "A":
        tipo = 0
    elif letra.upper()== "B":
        tipo = 1
    elif letra.upper() == "C":
        tipo = 2
    elif letra.upper() == "D":
        tipo = 3
    else:
        estado = "Letra Inválida"
        return False, estado
   
    if piso > 0 and piso < 11: 

        for f in range(filas):        
            for c in range(columnas):

                if len(str(departamento[piso-1,tipo])) > 2: 
                    estado = "No está disponible"
                    return False, estado
                
                else:
                   departamento[piso-1,tipo] = run 
                   
                   estado = f"Piso {piso}{letra.upper()} asignado correctamente al run: {run}\n"
                   listado_rut.append(run)
                   return  True, estado

    else:
        estado= "Rango Incorrecto: Ingrese un piso entre 1 y 10"
        return  False, estado



def listado_comprador(listado_rut):

    listado_rut.sort() #Ordenar RUTs de menor a mayor
    return listado_rut


def salir(flag):
    
    estado = "Alonso Miranda 13/07/2023"
    return False, estado




#La función ganancias_totales calcula y resume las ganancias obtenidas por la venta de departamentos, clasificándolas en cuatro tipos: A, B, C y D. Devuelve la cantidad vendida y la ganancia total por cada tipo, así como la ganancia total general.
def ganancias_totales(departamento):  

    count_tipo_A = 0
    count_tipo_B = 0
    count_tipo_C = 0
    count_tipo_D = 0

    for f in range(10):
        for c in range(4):
            if len(str(departamento[f,c])) > 2:

                if c == 0:
                    count_tipo_A+=1
                elif c == 1:
                    count_tipo_B+=1
                elif c == 2:
                    count_tipo_C+=1
                elif c == 3:
                    count_tipo_D+=1

    suma_tipo_A = count_tipo_A * 3800
    suma_tipo_B = count_tipo_B * 3000
    suma_tipo_C = count_tipo_C * 2800
    suma_tipo_D = count_tipo_D * 3500

    total = suma_tipo_A + suma_tipo_B + suma_tipo_C + suma_tipo_D
    
    estado_A = f"Tipo A 3.800 UF Cantidad Vendidos: {count_tipo_A} Total: {suma_tipo_A} UF"
    estado_B = f"Tipo B 3.000 UF Cantidad Vendidos: {count_tipo_B} Total: {suma_tipo_B} UF"
    estado_C = f"Tipo C 2.800 UF Cantidad Vendidos: {count_tipo_C} Total: {suma_tipo_C} UF"
    estado_D = f"Tipo D 3.500 UF Cantidad Vendidos: {count_tipo_D} Total: {suma_tipo_D} UF"
    estado_total = f"\nTOTAL VENTAS {total} UF"

    return estado_A, estado_B, estado_C, estado_D, estado_total
            
    
    
           