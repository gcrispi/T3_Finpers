import csv

def ultimo_id():
    with open("T3_Finpers/datos/datos.csv", "r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        ultimo = list(lector)
        print(ultimo[-1][0])
    

ultimo_id()