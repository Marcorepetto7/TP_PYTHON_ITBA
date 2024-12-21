import mysql.connector
from mysql.connector import Error
from resultados import Resultados
from ticket import Ticker
server = 'localhost'  
database = 'TP_TICKER'  
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
        datos_consulta = (ticker.tipo,)
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
            connection.commit()
            consulta_primaryKEY = """SELECT id_ticker FROM ticker WHERE tipo_ticker = %s ;"""
            datos_primaryKEY = (ticker.tipo,)
            cursor.execute(consulta_primaryKEY,datos_primaryKEY )
            primary_key = cursor.fetchone()[0]
            print(f"Insertado exitosamente con ID: {primary_key}")
            

            return primary_key

    except Error as e:
        print("Error al insertar el ticker:", e)

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def resultados_ticker(resultados_ticker,id_ticker):
    connection = conexion_base()
    try:
        cursor = connection.cursor()
        consulta_tipoAPI =  """
          SELECT COUNT(*) FROM valor_ticker  WHERE id_valor_ticker = %s ;"""
        datos_consultaAPI = (id_ticker,)
        cursor.execute(consulta_tipoAPI, datos_consultaAPI)
        contador = cursor.fetchone()[0]
        if contador == 0:
            consulta_API =  """
                INSERT INTO valor_ticker (id_valor_ticker,v,vw,o,c,h,l,t,n)
                VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s);
            """ 
            for result in resultados_ticker:
                v = result.get('v')
                vw = result.get('vw')
                o = result.get('o')
                c = result.get('c')
                h = result.get('h')
                l = result.get('l')
                t = result.get('t')
                n = result.get('n')
                datos_API = (id_ticker,v,vw,o,c,h,l,t,n)
                cursor.execute(consulta_API, datos_API)
                connection.commit()
        else:
            consulta_delete =  """DELETE FROM valor_ticker WHERE id_valor_ticker = %s ;"""
            datos_consulta_delete = (id_ticker,)
            cursor.execute (consulta_delete,datos_consulta_delete)
            connection.commit()
            consulta_API_again =  """
                INSERT INTO valor_ticker (id_valor_ticker,v,vw,o,c,h,l,t,n)
                VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s);
            """ 
            for result in resultados_ticker:
                v = result.get('v')
                vw = result.get('vw')
                o = result.get('o')
                c = result.get('c')
                h = result.get('h')
                l = result.get('l')
                t = result.get('t')
                n = result.get('n')
                datos_API = (id_ticker,v,vw,o,c,h,l,t,n)
                cursor.execute(consulta_API_again, datos_API)
                connection.commit()    
        
    except Error as e:
        print("Error al insertar resultados:", e)

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")        
    
def traer_tickers():
    connection = conexion_base()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        traer_dato ="""SELECT tipo_ticker,fecha_inicio,fecha_fin FROM ticker """
        cursor.execute (traer_dato,)
        ticker = cursor.fetchall()
        return ticker
    except Error as e:
        print("Error al traer tickers:", e)

    finally:
        # Cerrar la conexión
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

def traer_valores_ticker(tipo_ticker):

    connection = conexion_base()
    if connection is None:
        return

    try:
        cursor = connection.cursor()
        traer_dato2 ="""SELECT v.v,v.vw,v.o,v.c,v.h,v.l,v.t,v.n,t.tipo_ticker,t.fecha_inicio,t.fecha_fin 
        FROM valor_ticker v 
        INNER JOIN ticker t  ON t.id_ticker = v.id_valor_ticker
        WHERE t.tipo_ticker = %s  ;"""
        datos_join = (tipo_ticker,)
        cursor.execute (traer_dato2,datos_join)
        filas = cursor.fetchall()
        resultados_graficar = [
            Resultados(
                v=fila[0],
                vw=fila[1],
                o=fila[2],
                c=fila[3],
                h=fila[4],
                l=fila[5],
                t=fila[6],
                n=fila[7],
                tipo_ticker=fila[8],
                fecha_inicio=fila[9],
                fecha_fin=fila[10]
            )
            for fila in filas
        ]

        return resultados_graficar
        
    except Error as e:
        print("Error al traer datos:", e)

    finally:
        
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")