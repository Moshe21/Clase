# Lista para almacenar la información de empleados
info1 = []

# Método para crear un nuevo registro
def create(info1):
    ing_id = int(input("Ingrese ID: "))
    ing_nombre = input("Ingrese Nombre: ")
    ing_cargo = input("Ingrese Cargo: ")
    ing_salario = float(input("Ingrese Salario: "))

    # Agregar a la lista sin sobrescribirla
    info1.append([ing_id, ing_nombre, ing_cargo, ing_salario])

    print("✅ Se creó un nuevo registro.")

# Método para leer todos los registros
def read(info1):
    if not info1:
        print("⚠️ No hay registros.")
        return

    print("\n📋 Lista de empleados:")
    for empleado in info1:
        print(f"ID: {empleado[0]}, Nombre: {empleado[1]}, Cargo: {empleado[2]}, Salario: {empleado[3]}")
        
# Método para actualizar un registro
def update(info1):
    ing_id = int(input("Ingrese el ID del empleado a actualizar: "))
    
    for empleado in info1:
        if empleado[0] == ing_id:
            print(f"🔄 Actualizando datos de {empleado[1]}...")
            empleado[1] = input("Nuevo Nombre: ") or empleado[1]
            empleado[2] = input("Nuevo Cargo: ") or empleado[2]
            empleado[3] = float(input("Nuevo Salario: ") or empleado[3])
            print("✅ Registro actualizado.")
            return
    
    print("⚠️ No se encontró un empleado con ese ID.")

# Método para eliminar un registro
def delete(info1):
    ing_id = int(input("Ingrese el ID del empleado a eliminar: "))
    
    for empleado in info1:
        if empleado[0] == ing_id:
            info1.remove(empleado)
            print("🗑️ Registro eliminado correctamente.")
            return
    
    print("⚠️ No se encontró un empleado con ese ID.")

# Menú para interactuar con el CRUD
def menu():
    while True:
        print("\n📌 MENÚ CRUD:")
        print("1️⃣ - Crear Registro")
        print("2️⃣ - Leer Registros")
        print("3️⃣ - Actualizar Registro")
        print("4️⃣ - Eliminar Registro")
        print("5️⃣ - Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            create(info1)
        elif opcion == "2":
            read(info1)
        elif opcion == "3":
            update(info1)
        elif opcion == "4":
            delete(info1)
        elif opcion == "5":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()

        

# Method to insert a new salary registry
# def create(connection, BookingID, PassengerID, FlightID, BookingDate, SeatNumber):
    
#     info[][]


#     print("se creo nuevo dato")

# # Method to update a registry
# def update_employee(connection,  BookingID, BookingDate, SeatNumber):
#     cursor = connection.cursor()
#     query = """
#     UPDATE Bookings 
#     SET BookingDate = %s, SeatNumber = %s
#     WHERE BookingID = %s
#     """
#     cursor.execute(query, (BookingDate, SeatNumber,BookingID))
#     connection.commit()
#     print(f"Employee {BookingID} updated successfully.")

# # Method to delete an employee
# def delete_employee(connection, BookingID):
#     cursor = connection.cursor()
#     query = "DELETE FROM Bookings WHERE BookingID = %s"
#     cursor.execute(query, (BookingID,))
#     connection.commit()
#     print(f"Employee {BookingID} deleted successfully.")

# def main():
   
    # Calling method delete
    #print("Delete employee")
    #delete_employee(connection,7)

     #Calling method create a new salary
   # create_salaries(connection,11, 9, 10, '2024-08-19 14:00:00', 'Creado')


    # Calling method update
    #print("Update employee data")
    #update_employee(connection,8, '2024-08-19 21:00:00', 'Salta_7')
    
    # Calling method read
    #print("Read salaries upper 100000")Bookings
create(info)
read(info)




# [1,2,3,4,5]
#            [maria,fernadnda,juan,julia,moshe]
#            [cocinero,mensajero,mesero,lavadero,admin]
#            [1300000,1100000,1500000,1700000,2500000]