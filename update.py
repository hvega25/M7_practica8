import psycopg2


def updateTable(VehicleId, marca, precio, producto):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="localhost",
                                      port="5432",
                                      database="Vehicles")

        cursor = connection.cursor()

        # Llamamos a la tabla
        print("Table antes de update")
        sql_select_query = """select * from vehicle where id = %s"""
        cursor.execute(sql_select_query, (VehicleId,))
        record = cursor.fetchone()
        print(record)

        # Actualizamos cada uno de los datos de la tabla
        sql_update_query = """Update Vehicle set marca = %s where id = %s"""
        cursor.execute(sql_update_query, (marca, VehicleId))
        sql_update_query = """Update Vehicle set precio = %s where id = %s"""
        cursor.execute(sql_update_query, (precio, VehicleId))
        sql_update_query = """Update Vehicle set producto = %s where id = %s"""
        cursor.execute(sql_update_query, (producto, VehicleId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Actualizaste con exito los datos ")

        # Imprimimos los cambios realizados llamando nuevamente a la tabla
        print("Tabla despues de actualizar: ")
        sql_select_query = """select * from Vehicle where id = %s"""
        cursor.execute(sql_select_query, (VehicleId,))
        record = cursor.fetchone()
        print(record)

    except (Exception, psycopg2.Error) as error:
        print("Error a la hora de actualizar la tabla")

    finally:
        # Cerramos la base de datos.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


# Ponemos las modificaciones que queramos hacer

id = 2
marca = 't'
precio = 2
producto = 'g'
updateTable(id, marca, precio, producto)
