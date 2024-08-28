#Libraries required
import mysql.connector
from mysql.connector import Error
from config import config

# Method that allow connect to MySQL Server
def create_connection(config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("Connection has been successful!")
    except Error as e:
        print(f"This error '{e}'  occured")
    return connection

# Method to read salaries
def read_Bookings(connection):
    cursor = connection.cursor()
    query = "select * from artistas where id <10"
    cursor.execute(query)
    salaries = cursor.fetchall()
    for salary in salaries:
        print("Bookings: "+str(salary))

# Method to insert a new salary registry
def create_salaries(connection, id, nombre, pais, fecha_nacimiento, descripcion):
    cursor = connection.cursor()
    query = "INSERT INTO artistas (id, nombre, pais, fecha_nacimiento, descripcion) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(id, nombre, pais, fecha_nacimiento, descripcion))
    connection.commit()
    print(f"New salary for employee '{id}' has been inserted.")

# Method to update a registry
def update_employee(connection, id,descripcion):
    cursor = connection.cursor()
    query = """
    UPDATE artistas 
    SET descripcion = %s
    WHERE id = %s
    """
    cursor.execute(query, ( descripcion,))
    connection.commit()
    print(f"Employee {id} updated successfully.")

# Method to delete an employee
def delete_employee(connection, id):
    cursor = connection.cursor()
    query = "DELETE FROM artistas WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    print(f"Employee {id} deleted successfully.")

def main():
    connection = create_connection(config)

    # Calling method delete
   # print("Delete employee")
   # delete_employee(connection,8)

     #Calling method create a new salary
    #create_salaries(connection,  8, '2024-08-19', 'nuevo 8')


    # Calling method update
    #print("Update employee data")
    #update_employee(connection,  7, "el 8 fue saltado")
    
    # Calling method read
    #print("Read salaries upper 100000")Bookings
    read_Bookings(connection)


if __name__ == "__main__":
    main()