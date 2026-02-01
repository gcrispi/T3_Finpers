# Modulo con funciones para realizar operación en archivos 
# adicionalmente se importan bibliotecas especificas

# Funciones cargar historico desde archivo csv
# Funciones del Menu movimientos
# CRUD Movimientos
# Funciones del Menú Reportes Totales
# Funciones del Menú Exportar Archivos


import csv
import pandas as pd
import json

from pathlib import Path
from datetime import date

import validacion as v

# Ruta de archivos, que se utilizara con Path
ruta="T3_Finpers/datos/"
# Funciones del Proyecto para gestionar Registros y Movimientos 
movimientos = []


def cargar_historico():
    # importar datos de prueba desde archivo CSV
    try:
        campos = ['Id','Tipo','Categoria','Item','Fecha','Monto']
        ruta_datos = Path(str(ruta) + "/datos.csv")
        with open(ruta_datos, "r",encoding="utf-8") as archivo:
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
            # print(movimientos)
            archivo.close()
    except Exception as e:
        print(f"Ocurrio un error : {e}")
    finally:
        print("Se ha cargado información desde la Base")

# Funciones para el menú de CRUD de movimientos

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

    dic_movimiento={}
    num_fila=ultimo_id() #Valor inicial en 100 para identificar cada registro
    try:
        while True:
            dic_movimiento=v.valida_movimiento(num_fila)
            movimientos.append(dic_movimiento)
            num_fila +=1
            opcion=input("desea ingresar otro movimiento S/N:")
            if opcion.upper()=="N":
                break
        
        return movimientos
    except ValueError:
        print("Entrada inválida. Por favor, opción correcta.")

def buscar_movimiento():
    while True:
        num_id=input("Ingrese código del elementos a buscar: ")
        if num_id.isdigit():
            for valor in movimientos:
                # print(f"{valor["Id"]} {str(num_id)}")
                # Buscar elemento en lista de diccionarios
                if valor["Id"] == str(num_id):
                    print(f"Id:        {valor["Id"]}")
                    print(f"Tipo:      {valor["Tipo"]}")
                    print(f"Categoria: {valor["Categoria"]}")
                    print(f"Item:      {valor["Item"]}")
                    print(f"Fecha:     {valor["Fecha"]}")
                    print(f"Monto:     {valor["Monto"]}") 
        else:
            print("Debe ingresar sólo números punto para salir(.)")
            break

def eliminar_movimiento():
    while True:
        num_id=input("Ingrese código del elementos a eliminar: ")
        if num_id.isdigit():
            for valor in movimientos:
                # print(f"{valor["Id"]} {str(num_id)}")
                # Buscar elemento en lista de diccionarios
                if valor["Id"] == str(num_id):
                    movimientos.remove(valor)
        return False

def mostrar_movimiento():
    print("-"*79)
    print("ID | Categoria | Item | Fecha | Monto ")
    for valor in movimientos:
        print(f"{valor["Id"]}|{valor["Categoria"]}|{valor["Item"]}|{valor["Fecha"]}|{valor["Monto"]}")
    print("-"*79)

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
            with open(ruta_datos, "w", newline="", encoding="utf-8") as archivo:
            
                archivo=csv.DictWriter(archivo,fieldnames=campos)
                if len(datos) < 0:
                    archivo.writeheader()
                archivo.writerows(datos)
            #archivo.writerow(dic_movimiento)
        #print(f"Se ha registrado un nuevo movimiento {dic_movimiento}")

    except Exception as e:
        print(f"Ocurrio un error {e}")
    finally:
        print("Proceso de exportado se ejecuto.")

# Funciones para el menú de Reportes

def reportes_totales():

    lista=[]
    total=0
    
    for valor in movimientos:
        print(f"{valor["Tipo"]} {valor["Monto"]}")
        #monto=int(valor["Monto"])
        if valor["Tipo"] == "Ingreso":
            lista.append(int(valor["Monto"]))
        elif valor["Tipo"] == "Egreso":
            lista.append(int(valor["Monto"])*-1)
    
    total=sum(lista)

    if total<0:
        print(f"Tiene más gastos que ingresos: {total}")
    else:
        print(f"Finanzas Saludables: {total}")
    
def reportes_categorias():
    pass

def reportes_mensual():
    pass        

# Funciones para exportar a otros formatos
def exportar_excel():
    df = pd.DataFrame(movimientos)  
    #ruta del archivo Excel
    ruta_datos = Path(str(ruta) + "/datos.xlsx")

    try:
        dfexcel = pd.read_excel(ruta_datos)
        print(f"El archivo {ruta_datos} ya existe. Leyendo datos existentes.")
        print(dfexcel)
    except FileNotFoundError as e:
        print(f"Error al exportar a Excel: {e}")
        df.to_excel(ruta_datos, index=False)
        # Exportar el DataFrame a un archivo Excel

def exportar_json():
    ruta_datos = Path(str(ruta) + "/datos.json")
    try:
        with open(ruta_datos, "w", encoding="utf-8") as archivo_json:
            json.dump(movimientos, archivo_json, ensure_ascii=False, indent=4)
            print("Datos exportados exitosamente a JsonExportado.json")
    except Exception as e:
        print(f"Ocurrió un error al exportar los datos a JSON: {e}")
    


