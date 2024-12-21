import mysql.connector
from mysql.connector import Error
from ticket import Ticker
server = 'localhost'  # Servidor donde se encuentra SQL Server
database = 'TP_TICKER'  # Nombre de la base de datos
def conexion_base():
    """Establece la conexión a la base de datos."""
    try:
    # Establecer la conexión
        connection = mysql.connector.connect(
        host='localhost',          # Cambia a tu host, por ejemplo, '127.0.0.1' o una IP remota
        database='TP_TICKER',# Nombre de tu base de datos
        user='root',         # Usuario MySQL
        password='')   # Contraseña MySQL

        if connection.is_connected():
        # Información del servidor
            db_info = connection.get_server_info()
            print("Conectado a MySQL Server versión", db_info)

        # Crear un cursor para ejecutar consultas
            # # cursor = connection.cursor()
            # cursor.execute("SELECT DATABASE();")
            # record = cursor.fetchone()
            # print("Conectado a la base de datos:", record)

    except Error as e:
        print("Error al conectar a MySQL:", e)
        # cursor.close()
        connection.close()
 
    return connection        

def insertar_ticker(ticker: Ticker):
    """Inserta un nuevo registro en la tabla ticker y devuelve el ID generado."""
    connection = conexion_base()
    if connection is None:
        return

    try:
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()
        consulta_tipo =  """
          SELECT COUNT(*) FROM ticker  WHERE tipo_ticker = %s ;"""
        datos_consulta = (ticker.tipo)
        cursor.execute(consulta_tipo, datos_consulta)
        contador = cursor.fetchone()[0]
        if contador == 0:
            consulta_insert = """
            INSERT INTO ticker (tipo_ticker, fecha_inicio, fecha_fin)
            VALUES (%s, %s, %s);
        """
            datos = (ticker.tipo, ticker.fecha_inicio, ticker.fecha_fin)
           
        # Ejecutar la consulta
            cursor.execute(consulta_insert, datos)
            

        # Obtener el ID autogenerado
            primary_key = cursor.lastrowid
            print(f"Insertado exitosamente con ID: {primary_key}")

        # Confirmar los cambios
            connection.commit()
            return primary_key
        else :
            # Consulta SQL de actualización
            consulta_update = """
                UPDATE ticker
                SET fecha_inicio = %s, fecha_fin = %s
                WHERE tipo_ticker = %s;
            """
            datos = (ticker.fecha_inicio, ticker.fecha_fin, ticker.tipo)

            # Ejecutar la consulta
            cursor.execute(consulta_update, datos)
            primary_key = cursor.lastrowid
            print(f"Insertado exitosamente con ID: {primary_key}")
            connection.commit()

            return primary_key

    except Error as e:
        print("Error al insertar el ticker:", e)

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")
            
    
