from dateutil import parser
from ticket import Ticker
from datetime import date
def ingresar_ticker():
    tipo = input("ingrese un ticker a pedir: ")
    inicio = (input("ingrese un fecha de inicio a pedir: "))
    fin = input("ingrese un fecha de fin a pedir: ")
    fecha_inicio = parser.parse(inicio)
    fecha_fin = parser.parse(fin)
    ticker1 = Ticker(tipo,fecha_inicio.date(),fecha_fin.date())
    return ticker1 