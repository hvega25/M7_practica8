import delete
import create
import create_table
import insert
import read
import update

print("Creacion de base de datos de vehicles")
print(create.create())

print("Ahora se creara la tabla vehicle")
print(create_table.create_tables())

#tengo el teclado ingles por eso el ny
print("A continuacion se anyadiran datos a la tabla")
print(insert.insert())

print("Ahora como se veria la tabla")
print(read.read())

print("finalmente asi se editaran los elementos")
print(update.updateTable())

print("Ahora como se veria la tabla despues de actualizar")
print(read.read())

print("Ahora se eliminara el vehiculo con id 1")
print(delete.deleteVehicle(1))

print("Ahora como se veria la tabla despues de eliminar")
print(read.read())