from datetime import date

def valida_movimiento(num_fila):
    dic_movimiento={}
    try:
        id = num_fila #input("Ingrese Id Movimiento: ")
        # Valida Tipo de Movimiento
        # Uso de if abreviado, para definir tipo de ingreso
        while True:
            tipo = input("Ingrese Tipo (I) Ingreso/ (E) Egreso: ")
            tipo.strip()
            print(tipo.strip())
            if tipo.upper()=="I" or tipo.upper()=="E":
                tipo = "Ingreso" if tipo.upper() == "I" else "Egreso" 
                #tipo=tipo.strip()
                break
            else:
                print("Error vuevla a ingresar Tipo")
        #Valida Categoria
        while True:
            categoria = input("Ingrese Categoria: ")
            if categoria.isalpha():
                categoria=categoria.upper()
                break
            else:
                print("Error vuevla a ingresar Categoria")
        #Valida Item
        while True:
            Item = input("Ingrese Item: ")
            if Item.isalpha():
                Item=Item.upper()
                break
            else:
                print("Error vuevla a ingresar Item")
        #Valida Fecha con libreria date y formato
        while True:
            Fecha = input("Ingrese Fecha: dd-mm-aaaa :")
            #datetime.strftime(Fecha,"%d-m-%Y")
            if validar_fecha(Fecha):
                #print("Fecha formateada")
                break
            else:
                print("Error vuevla a ingresar Fecha")
        #Valida Monto
        while True:
            Monto = input("Ingrese Monto: ")
            if Monto.isnumeric():
                Monto=Monto
                break
            else:
                print("Error vuevla a ingresar Monto")     
        
        dic_movimiento = {
            "Id":str(id),
            "Tipo":tipo,
            "Categoria":categoria,
            "Item":Item,
            "Fecha":Fecha,
            "Monto":Monto
            }
        
        return dic_movimiento
    except ValueError:
        print("ha ocurrido un error")

def validar_fecha(fecha_str, formato="%d-%m-%Y"):
    try:
        date.strptime(fecha_str, formato)
        return True
    except ValueError:
        return False
    finally:
        print(fecha_str)

#d=valida_movimiento()
#print(d["Fecha"])
#print(d["Categoria"])


