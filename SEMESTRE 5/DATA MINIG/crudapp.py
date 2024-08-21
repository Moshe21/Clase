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
def read_Bookings(connection,table,id):
    cursor = connection.cursor()
    query = "select * from %s  where %s < 15"
    cursor.execute(query,(table,id))
    salaries = cursor.fetchall()
    for salary in salaries:
        print("Bookings: "+str(salary))

# Method to insert a new salary registry
def create_salaries(connection, BookingID, PassengerID, FlightID, BookingDate, SeatNumber):
    cursor = connection.cursor()
    query = "INSERT INTO Bookings (BookingID, PassengerID, FlightID, BookingDate, SeatNumber) VALUES(%s,%s,%s,%s,%s)"
    cursor.execute(query,(BookingID, PassengerID, FlightID, BookingDate, SeatNumber))
    connection.commit()
    print(f"New salary for employee '{BookingID}' has been inserted.")

# Method to update a registry
def update_employee(connection,  BookingID, BookingDate, SeatNumber):
    cursor = connection.cursor()
    query = """
    UPDATE Bookings 
    SET BookingDate = %s, SeatNumber = %s
    WHERE BookingID = %s
    """
    cursor.execute(query, (BookingDate, SeatNumber,BookingID))
    connection.commit()
    print(f"Employee {BookingID} updated successfully.")

# Method to delete an employee
def delete_employee(connection, BookingID):
    cursor = connection.cursor()
    query = "DELETE FROM Bookings WHERE BookingID = %s"
    cursor.execute(query, (BookingID,))
    connection.commit()
    print(f"Employee {BookingID} deleted successfully.")

def main():
    connection = create_connection(config)

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
    read_Bookings(connection,'Airlines','AirlineID')


if __name__ == "__main__":
    main()