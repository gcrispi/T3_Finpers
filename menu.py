# modulo encargado de realizar la visualización de opciones y menu del 
# sistema, estos fueron creados en listas para su mantenibilidad y uso
# de diccionarios

import gestion as g

# Funciones de visualización para opciones del Menu del Sistema
# inicializa lista con diccionaro desde archivo guardado

g.cargar_historico() ### Llamada a funcion para cargar datos

def menu_principal():
    menu_dic = {
            "1":"Mantenedor de Finanzas Personales",
            "2":"Borrar Hitorico",
            "3":"Reportes Totales",
            "4":"Exportar XLSX,JSON",
            "5":"Salir"
    }
    while True:
        print("*"*72)
        print("Sistema de Gestion para las Finanzas Personales\n")
        print("*"*72)
        #Recorrido de diccionario con for y diccionario con uso de llave
        for m in menu_dic:
            print(f"{m} : {menu_dic[m]}")        
        
        opcion=input("Ingrese Opción :")
        if not opcion.isdigit():
            print("Debe ingresar sólo números")
            break
        else:
            opcion=int(opcion)
        match opcion:
            case 1:
                menu_crud()
            case 2:
                menu_historico()
            case 3:
                menu_reportes()
            case 4:
                menu_exportar()
            case 5:
                break
            case _:
                print("Opcion Invalida, vuelva a intentar: ")

def menu_historico():
    menu_dic = {
            "1":"Limpiar Base Historico",
            "2":"Menu Anterior"
    }
    while True:
        print("*"*72)
        m="Sistema de Gestion para las Finanzas Personales / Carga Historico"
        print(m)
        print("*"*72)
        #Recorrido de diccionario con for y obteniendo llave e items como valor        
        for km, val_menu in menu_dic.items():
            print(f"{km} : {val_menu}")
        
        opcion=input("Ingrese Opción :")
        if not opcion.isdigit():
            print("Debe ingresar sólo números")
            break
        else:
            opcion=int(opcion)
        match opcion:
            case 1:
                pass
            case 2:
                break
            case _:
                print("Opcion Invalida, vuelva a intentar: ")

def menu_crud():
    # Se genera lista con datos desde el archivo
    lista=[]
    
    menu_dic = {
            "1":"Ingresar Nuevo Movimiento",
            "2":"Buscar Movimiento",
            "3":"Mostrar Movimientos",
            "4":"Eliminar Movimiento",
            "5":"Menu Anterior"
    }    
    while True:
        print("*"*72)
        m="Sistema de Gestion para las Finanzas Personales / CRUD Movimientos"
        print(m)
        print("*"*72)
        #Recorrido de diccionario con for y obteniendo valor e items como arreglo
        for val_menu in menu_dic.items():
            print(f"{val_menu[0]} : {val_menu[1]}")

        opcion=input("Ingrese Opción :")
        if not opcion.isdigit():
            print("Debe ingresar sólo números")
            break
        else:
            opcion=int(opcion)
        match opcion:
            case 1:
                # llamada a funcion que retorna lista de diccionario 
                # una vez que sale del ingreso, se envia lista para la función
                # exportar que escribe la lista de diccionario en un archivo
                lista=g.ingresar_movimiento()
                g.exportar_movimientos(lista)
            case 2:
                g.buscar_movimiento()
            case 3:
                g.mostrar_movimiento()
            case 4:
                g.eliminar_movimiento()
            case 5:
                break
            case _:
                print("Opcion Invalida, vuelva a intentar: ")

def menu_reportes():
    while True:
        print("*"*72)
        m="Sistema de Gestion para las Finanzas Personales / Reportes"
        print(m)
        print("*"*72)
                
        print("1.- Totales Ingresos/Egresos")
        print("2.- Total Categorias")
        print("3.- Total Mensual")
        print("4.- Menu Anterior")
        
        opcion=input("Ingrese Opción :")
        if not opcion.isdigit():
            print("Debe ingresar sólo números")
            break
        else:
            opcion=int(opcion)
        match opcion:
            case 1:
                g.reportes_totales()
            case 2:
                g.reportes_categorias()
            case 3:
                g.reportes_mensual()
            case 4:
                break
            case _:
                print("Opcion Invalida, vuelva a intentar: ")

def menu_exportar():
    while True:
        print("*"*72)
        m="Sistema de Gestion para las Finanzas Personales / Exportar JSON-Excel"
        print(m)
        print("*"*72)
                
        print("1.- Exportar Excel")
        print("2.- Exportar Json")
        print("3.- Menu Anterior")
        
        opcion=input("Ingrese Opción :")
        if not opcion.isdigit():
            print("Debe ingresar sólo números")
            break
        else:
            opcion=int(opcion)
        match opcion:
            case 1:
                g.exportar_excel()
            case 2:
                g.exportar_json()
            case 3:
                break
            case _:
                print("Opcion Invalida, vuelva a intentar: ")    

'''
if __name__ == "__main__":
    menu_principal()
'''