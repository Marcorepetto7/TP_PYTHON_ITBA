import pyodbc
import requests
from conexion_SQLserver import insertar_ticker
from ticket import Ticker
from ingresar_ticker import ingresar_ticker
from datetime import date
ticker1 = None

while True :
     print("1. ingrese ticker a pedir: ")
     print ("2. salir: ")
     opcion = input("opcion: ")
     match opcion:
        case "1" :
            ticker1 = ingresar_ticker()
            insertar_ticker(ticker1)
            print(ticker1)
            r = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker1.tipo}/range/1/day/{ticker1.fecha_inicio}/{ticker1.fecha_fin}?adjusted=true&sort=asc&apiKey=deRqjr7FLt4JA0xlnrd9MMNs38wGq22V")
            #print(r.content)
        case "2":
             break


