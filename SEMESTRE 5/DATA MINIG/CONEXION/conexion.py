import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Moshe21",
    database="conexion_py"
)


def crear():

    mycursor =mydb.conexion_py()
    mycursor.execute("create table new_table();")
    myresultado= mycursor.fetchall()

    for x in myresultado:
        print(x)

crear()

def mostar():

    mycursor =mydb.conexion_py()
    mycursor.execute("select * from Bookings;")
    myresultado= mycursor.fetchall()

    for x in myresultado:
        print(x)

mostar()

def eliminar():

    mycursor =mydb.conexion_py()
    mycursor.execute("delete BookingID from Bookings where BookingID= 2;")
    myresultado= mycursor.fetchall()

    for x in myresultado:
        print(x)

eliminar()

def modificar():

    mycursor =mydb.conexion_py()
    mycursor.execute("alter table * from Bookings;")
    myresultado= mycursor.fetchall()

    for x in myresultado:
        print(x)

modificar()




