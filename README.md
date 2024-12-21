# Proyecto: Gestión y Visualización de Tickers Financieros

## Descripción General
Este proyecto es una aplicación interactiva desarrollada en Python que permite la consulta, almacenamiento, análisis y visualización de datos históricos financieros para diferentes tickers (por ejemplo, `AAPL` o `MSFT`). Los datos son obtenidos a través de la API de [Polygon.io](https://polygon.io/) y se almacenan en una base de datos MySQL para realizar análisis posteriores. 

El proyecto fue realizado para poder observar el movimiento de los tickers a lo largo del tiempo, de una forma automatizada.

---

## **Características**

1. **Consulta de Datos desde la API de Polygon.io**:
   - Permite obtener datos históricos de los tipos de tickers como fechas de inicio y de fin y sus valores en letras.
   - Permite consultas personalizadas por rango de fechas.

2. **Gestión de Datos en MySQL**:
   - **Inserción y Actualización Automática**: Los datos obtenidos son almacenados en una base de datos MySQL. Si un ticker ya existe, se actualizan los registros.
   - **Consultas Internas**: Posibilidad de acceder a tickers almacenados y sus datos históricos para realizar resumenes y gráficos.

3. **Visualización de Datos**:
   - **Gráficos de Líneas**: Representación de los precios de apertura y cierre a lo largo del tiempo.
   - **Gráficos de Barras**: Visualización del volumen de transacciones por fecha.

4. **Interfaz Interactiva**:
   - Menú en consola que permite:
     - Actualizar datos desde la API.
     - Consultar resúmenes de tickers que fueron almacenados.
     - Graficar tickers con las fechas seleccionadas almacenadas.

---

## **Tecnologías Utilizadas**
- **Lenguaje**: Python 3.x
- **Librerías y Herramientas**:
  - `requests`: Para realizar solicitudes HTTP a la API de Polygon.io.
  - `pandas`: Para la manipulación y análisis de datos estructurados.
  - `matplotlib`: Para la generación de gráficos.
  - `mysql-connector-python`: Para conectar Python con MySQL.
  - `visual studio code`: para poder correr codigo de python, fue utilizado por comodidad.
- **Base de Datos**: MySQL tambien por saber utilizarlo mejor, para almacenar y consultar los datos de tickers financieros.

---

### Módulos Principales:
1. **`main.py`**:
   - Controlador principal que permite al usuario interactuar con el sistema mediante un menú en consola.
   - Funcionalidades:
     - Actualización de datos desde la API.
     - Visualización y graficación de datos almacenados.

2. **`conexion_SQLserver.py`**:
   - Maneja la conexión con la base de datos MySQL.
   - Implementa las operaciones CRUD para las tablas `ticker` y `valor_ticker`.

3. **`graficos_resumen.py`**:
   - Contiene las funciones para generar gráficos interactivos y personalizados.

4. **`ticket.py`**:
   - Define la clase `Ticker`, que representa un ticker con sus atributos principales (tipo, fecha de inicio y fecha de fin).

5. **`resultados.py`**:
   - Define la clase `Resultados`, que representa los datos históricos de un ticker.

6. **`ingresar_ticker.py`**:
   - Permite al usuario ingresar un nuevo ticker y el rango de fechas para la consulta.

### Base de Datos:
1. **Tablas**:
   - **`ticker`**:
     - Almacena información general de los tickers: tipo, fecha de inicio y fecha de fin.
   - **`valor_ticker`**:
     - Almacena los datos históricos asociados a cada ticker: volumen, precios de apertura, cierre, máximo y mínimo.

---

## **Flujo del Sistema**
1. **Inicio**:
   - El usuario ejecuta el programa y selecciona una opción del menú interactivo.

2. **Opción 1: Actualizar datos**:
   - El usuario ingresa un ticker y un rango de fechas.
   - Se realiza una solicitud a la API de Polygon.io para obtener los datos históricos del ticker.
   - Los datos son almacenados en la base de datos MySQL.

3. **Opción 2: Visualizar y graficar datos**:
   - **Resumen**: Muestra los tickers almacenados y sus fechas.
   - **Graficar**: Permite seleccionar un ticker para generar gráficos de líneas (precios) y barras (volumen).

---

