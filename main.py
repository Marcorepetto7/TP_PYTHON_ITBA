import os
import pyodbc
import requests
from conexion_SQLserver import insertar_ticker,resultados_ticker,traer_tickers,traer_valores_ticker
from graficos_resumen import grafico1
from ticket import Ticker
from ingresar_ticker import ingresar_ticker
from datetime import date
ticker1 = None

while True :
     print("1. Actualizar datos ")
     print ("2. Visualizar y graficar ticker ")
     opcion = input("opcion: ")
     match opcion:
        case "1" :
            os.system('cls')
            ticker1 = ingresar_ticker()
            os.system('cls')
            r = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker1.tipo}/range/1/day/{ticker1.fecha_inicio}/{ticker1.fecha_fin}?adjusted=true&sort=asc&apiKey=deRqjr7FLt4JA0xlnrd9MMNs38wGq22V")
            data = r.json()
            results = data.get('results', [])
            id = insertar_ticker(ticker1)
            resultados_ticker(results,id)
        case "2":
            os.system('cls')
            print("1. Resumen ticker ")
            print ("2. Graficar ticker ")
            opcion_ = input ("ingrese una opcion :")
            os.system('cls')
            if opcion_ == "1":
                tickers_resumen = traer_tickers()
                for ticker in tickers_resumen:
                    print(f"{ticker[0]} - {ticker[1].date()} <-> {ticker[2].date()}")
            elif opcion_ == "2":
                ticker = input ("ingrese un tipo de ticker a graficar :") 
                valores = traer_valores_ticker(ticker)
                grafico_1= grafico1(valores)
                
        case _:
            break


