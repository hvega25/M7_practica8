import psycopg2

def create_tables():
    try:
        connection = psycopg2.connect(user="postgres",
                                      password=" ",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="vehicle")

        cursor = connection.cursor()
        #CREAR TABLAS
        command = """
        CREATE TABLE vehicles (
            id INTEGER PRIMARY KEY,
            marca VARCHAR(55) NOT NULL,
            preu INTEGER NOT NULL,
            color VARCHAR(55) NOT NULL
        )
        """
        cursor.execute(command)
        # close communication
        cursor.close()
        # subir cambios
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # tancant connexió
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL s'ha tancat la connexió")
