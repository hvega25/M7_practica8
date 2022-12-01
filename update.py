import psycopg2


def updateTable(vehicleId, marca, preu, color):
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="localhost",
                                      port="5432",
                                      database="vehicle")

        cursor = connection.cursor()

        # Llamamos a la tabla
        print("Table antes de update")
        sql_select_query = """select * from vehicle where id = %s"""
        cursor.execute(sql_select_query, (vehicleId,))
        record = cursor.fetchone()
        print(record)

        # Actualizamos cada uno de los datos de la tabla
        sql_update_query = """Update vehicle set marca = %s where id = %s"""
        cursor.execute(sql_update_query, (marca, vehicleId))
        sql_update_query = """Update vehicle set preu = %s where id = %s"""
        cursor.execute(sql_update_query, (preu, vehicleId))
        sql_update_query = """Update vehicle set color = %s where id = %s"""
        cursor.execute(sql_update_query, (color, vehicleId))
        connection.commit()
        count = cursor.rowcount
        print(count, "Actualizaste con exito los datos ")

        # Imprimimos los cambios realizados llamando nuevamente a la tabla
        print("Tabla despues de actualizar: ")
        sql_select_query = """select * from vehicle where id = %s"""
        cursor.execute(sql_select_query, (vehicleId,))
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
marca = 'n'
preu= 4
color = 'o'
updateTable(id, marca, preu, color)
