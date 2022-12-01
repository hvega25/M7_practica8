import psycopg2 #importa la libreria necesaria para la base de datos


def read():
#usamos try para evitar cierres bruscos
    try:
    #la variable coneccion se le asigna el metodo con los parametros
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password = ' ', #tenemos diferentes contraseñas en el pgadmin4
            database = 'vehicle')
        print("Conexión exitosa") #imprime si hay conexion es una bandera verde
        cursor = connection.cursor() # esta variable es la de control sobre la tabla


        cursor.execute("SELECT * FROM vehicle") #la query que selecciona la tabla
        rows = cursor.fetchall() #guarda los datos
        for row in rows:#metodo para imprimir los datos
            print(rows)
    except Exception as ex:#exception que muestra el error si hubiera
        print(ex)
    finally:
        connection.close()#cierra la conexion
        print("Cerrada correctamente")


read()#llamada de la funcion