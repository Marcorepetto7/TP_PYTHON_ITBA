from dateutil import parser
from datetime import date
from datetime import datetime
class Resultados:
    def __init__(self, v, vw, o, c, h, l, t, n, tipo_ticker, fecha_inicio, fecha_fin):
        self.v = v
        self.vw = vw
        self.o = o
        self.c = c
        self.h = h
        self.l = l
        self.t = t
        self.n = n
        self.tipo_ticker = tipo_ticker

        if isinstance(fecha_inicio, datetime):
            self.fecha_inicio = fecha_inicio.date()
        else:
            self.fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()

        if isinstance(fecha_fin, datetime):
            self.fecha_fin = fecha_fin.date()
        else:
            self.fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()
