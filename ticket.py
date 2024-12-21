from datetime import date
class Ticker:
    def __init__(self,tipo,fecha_inicio,fecha_fin):
        self.tipo = tipo
        self.fecha_inicio =  fecha_inicio
        self.fecha_fin = fecha_fin
    def __str__(self):
        return (f"(tipo={self.tipo}, "
                f"fecha_inicio={self.fecha_inicio}, "
                f"fecha_fin={self.fecha_fin})")   






