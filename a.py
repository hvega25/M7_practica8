import psycopg2

def updateTable(marca, precio, producto):
    # conexion con la base de datos
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="1234",
                                      host="localhost",
                                      port="5432",
                                      database="Vehicles"
                                      )
        print("conexion exitosa")
        cursor = connection.cursor()

        print("Table antes de update")
        sql_select_query = """select * from Vehicles where Vehicle = %s"""
        cursor.execute(sql_select_query, (marca, precio, producto))
        record = cursor.fetchone()
        print(record)

        #Modificación de las columnas
        sql_update_query = """Update Vehicle set marca = %s where marca = %s"""
        sql_update_query = """Update Vehicle set precio = %s where precio = %s"""
        sql_update_query = """Update Vehicle set producto = %s where precio = %s"""
        cursor.execute(sql_update_query, (marca, precio, producto))
        connection.commit()
        count = cursor.rowcount
        print(count, "Actualizado con exito ")


        print("Table After updating record ")
        sql_select_query = """select * from Vehicle where id = %s"""
        cursor.execute(sql_select_query, (marca, precio, producto))
        record = cursor.fetchone()
        print(record)
    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

marca = "a"
precio = 2
producto = "b"
updateTable(marca, precio, producto)




