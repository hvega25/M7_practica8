import psycopg2 #importa la libreria necesaria para la base de datos


def insert():
    try:
        # la variable coneccion se le asigna el metodo con los parametros
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password=' ',  # tenemos diferentes contraseñas en el pgadmin4
            database='vehicle')
        print("Conexión exitosa")  # imprime si hay conexion es una bandera verde
        cursor = connection.cursor()  # esta variable es la de control sobre la tabla

        #query necesaria para la ejecucion de la base de datos
        postgres_insert_query = """ INSERT INTO vehicle (id, marca, preu,color) VALUES (%s,%s,%s,%s)"""
        record_to_insert = (9, 'Lambo', 60, 'amarillo') #valores
        cursor.execute(postgres_insert_query, record_to_insert)#ejecucion de la query

        connection.commit() # subida
        count = cursor.rowcount # conteo de elementos subidos a la tabla
        print(count, "Insertado correctamente") #
    except Exception as ex:
        print(ex)
    connection.close()  # cierra la conexion
    print("Cerrada correctamente")


insert()