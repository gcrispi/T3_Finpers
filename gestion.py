import csv
from pathlib import Path
from datetime import date
import validacion as v

# ruta de archivos
ruta="T3_Finpers/datos/"
# Funciones del Menu Principal
movimientos = []

def cargar_historico():
    # importar datos de prueba desde archivo CSV
    try:
        campos = ['Id','Tipo','Categoria','Item','Fecha','Monto']
        with open(ruta_datos+"movimientos.csv", "r",encoding="utf-8") as archivo:
            registros = csv.DictReader(archivo,fieldnames=campos)
            for fila in registros:

                id=fila["Id"]
                tipo=fila["Tipo"]
                categoria=fila["Categoria"]
                item=fila["Item"]
                fecha=fila["Fecha"]
                monto=fila["Monto"]

                dic_movimiento = {
                "Id":id,
                "Tipo":tipo,
                "Categoria":categoria,
                "Item":item,
                "Fecha":fecha,
                "Monto":monto
                }
                movimientos.append(dic_movimiento)
            print(movimientos)
            archivo.close()
    except Exception as e:
        print(f"Ocurrio un error : {e}")

def ultimo_id():
    num_reg = 0
    with open("T3_Finpers/datos/datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        ultimo = list(lector)
        #int(ultimo[-1][0]) # obtiene el último elemento de la lista
        num_reg=int(ultimo[-1][0])  if int(ultimo[-1][0]) > 0  else 100
        num_reg += 1
    return (num_reg)

def ingresar_movimiento():
    lista=[]
    dic_movimiento={}
    num_fila=ultimo_id() #Valor inicial en 100 para identificar cada registro
    try:
        while True:
            dic_movimiento=v.valida_movimiento(num_fila)
            lista.append(dic_movimiento)
            num_fila +=1
            opcion=input("desea ingresar otro movimiento S/N:")
            if opcion.upper()=="N":
                break
        #print(lista)
        return lista
    except ValueError:
        print("Entrada inválida. Por favor, opción correcta.")
 
def exportar_movimientos(lista):
    '''
    id = input("Ingrese Id Movimiento: ")
    tipo = input("Ingrese Tipo: ")
    categoria = input("Ingrese Categoria: ")
    item = input("Ingrese Item: ")
    fecha = input("Ingrese Fecha: ")
    monto = input("Ingrese Monto: ")

    dic_movimiento = {
            "Id":id,
            "Tipo":tipo,
            "Categoria":categoria,
            "Item":item,
            "Fecha":fecha,
            "Monto":monto
            }
    '''
    try:
        # importante declarar diccionario previamente
        # Se exporta un diccionario validado al archivo de datos
        # Utilización de libreria PathLib para verificar existencia de archivo
            #dic_movimiento={} 
            #dic_movimiento=v.valida_movimiento()
            #datos=[]
            #datos.append(dic_movimiento)
            #print(datos)
        datos=[]
        datos=lista
        campos = ['Id','Tipo','Categoria','Item','Fecha','Monto']
        ruta_datos = Path(str(ruta) + "/datos.csv")
        if ruta_datos.exists():
            with open(ruta_datos, "a", newline="", encoding="utf-8") as archivo:
            
                archivo=csv.DictWriter(archivo,fieldnames=campos)
                #archivo.writeheader()
                archivo.writerows(datos)
            #archivo.writerow(dic_movimiento)
        #print(f"Se ha registrado un nuevo movimiento {dic_movimiento}")

    except Exception as e:
        print(f"Ocurrio un error {e}")
    finally:
        print("Proceso de exportado se ejecuto.")


def reportes():
    pass
def exportar():
    pass

# Funciones cargar historico desde archivo csv
# Funciones del Menu movimientos
# CRUD Movimientos
# Funciones del Menú Reportes Totales
# Funciones del Menú Exportar Archivos

