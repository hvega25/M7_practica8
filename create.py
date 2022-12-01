import psycopg2

def create():
   #estableciendo connexion
   conn = psycopg2.connect(
      database="postgres", user='postgres', password=' ', host='127.0.0.1', port='5432'
   )
   conn.autocommit = True;

   #Creando un cursor
   cursor = conn.cursor()

   #Preparing query to create a database
   sql = '''CREATE database vehicle''';

   #Creating a database
   cursor.execute(sql)
   print("Base de datos creada")

   #Closing the connection
   conn.close()

create()