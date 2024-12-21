from conexion_SQLserver import traer_valores_ticker
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def grafico1 (valores):
    data = pd.DataFrame([vars(valor) for valor in valores])


    data['t'] = pd.to_datetime(data['t'], unit='ms')  

    
    plt.figure(figsize=(12, 6))


    plt.plot(data['t'], data['o'], label='Precio de Apertura', marker='o')
    plt.plot(data['t'], data['c'], label='Precio de Cierre', marker='x')

    plt.title("Evolución del Precio de Apertura y Cierre")
    plt.xlabel("Fecha")
    plt.ylabel("Precio ($)")
    plt.legend()
    plt.grid(True)

    
    plt.show()

    
    plt.figure(figsize=(12, 6))
    plt.bar(data['t'], data['v'], color='blue', alpha=0.6)

    
    plt.title("Volumen de Transacciones por Fecha")
    plt.xlabel("Fecha")
    plt.ylabel("Volumen")
    plt.grid(axis='y')

    plt.show()

