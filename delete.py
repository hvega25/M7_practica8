import psycopg2

#
def deleteVehicle(id):
    try:
        connection = psycopg2.connect(user="postrges",
                                      password="12345678",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="vehicles")

        cursor = connection.cursor()
        sql_delete_query = """Delete vehicle on l'id = %s"""
        cursor.execute(sql_delete_query, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Eliminat correctament ")

    except (Exception, psycopg2.Error) as error:
        print("Error eliminando", error)

    finally:
        # tancant connexió
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL s'ha tancat la connexió")


deleteVehicle(1)