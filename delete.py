import psycopg2

#Funcion delete para eliminar por id
def deleteVehicle(id):
    #Connexion con un try
    #cambiar contraseña en caso de ser diferente
    try:
        connection = psycopg2.connect(user="postgres",
                                      password="12345678",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="vehicles")
        #Delete method
        cursor = connection.cursor()
        sql_delete_query = """Delete vehicle on l'id = %s"""
        cursor.execute(sql_delete_query, (id,))
        connection.commit()
        count = cursor.rowcount
        print(count, "Eliminat correctament ")
    #En caso de no hacer connexion salta este error
    except (Exception, psycopg2.Error) as error:
        print("Error eliminando", error)
    finally:
        # tancant connexió
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL s'ha tancat la connexió")

#llamada a la funcion
deleteVehicle(1)