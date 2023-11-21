import tkinter
from tkinter import ttk
import mysql.connector
from funciones import *


def abrir_check_pedidos():
    def buscador(event):
        ot = buscador_entry.get()
        gestor = buscador_entry.get().upper()
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        instruccion = f"SELECT * FROM registro_pedidos WHERE caso LIKE '{ot}%' or gestor_rcc like'{gestor}%'"
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Pedidos pendientes")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 875
    alto_ventana = 385
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco = tkinter.Label(ventana, padx=5, pady=5)
    marco.pack(padx=10, pady=10)
    marco.config(bg="white")

    marco_buscador = tkinter.Frame(marco, padx=5, pady=5)
    marco_buscador.config(bg="white")
    marco_buscador.pack(padx=10, pady=10)

    buscador_label = tkinter.Label(
        marco_buscador, text="Buscar por caso/gestor", font="Barlow 13 ", bg="white")
    buscador_label.pack(side="left", pady=10)

    buscador_entry = tkinter.Entry(
        marco_buscador, font="Barlow 11", width=70)
    buscador_entry.pack(fill="x", pady=10)
    buscador_entry.bind("<Return>", buscador)

    tabla = ttk.Treeview(marco, selectmode="browse", height=12)
    horizontal_bar = ttk.Scrollbar(marco, orient="horizontal")
    vertical_bar = ttk.Scrollbar(marco, orient="vertical")

    tabla.configure(xscrollcommand=horizontal_bar.set,
                    yscrollcommand=vertical_bar.set)
    horizontal_bar.configure(command=tabla.xview)
    vertical_bar.configure(command=tabla.yview)

    vertical_bar.pack(side="right", fill="y")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    tabla['columns'] = ("Fecha de solicitud", "Cliente", "Caso", "Orden de compra", "Sede", "Gestor",
                        "Resumen del caso", "Insumo", "Cantidad", "Tipo", "Valor materiales", "Valor envio",
                        "Direccion cliente", "Ciudad entrega", "Tecnico que recibe", "Cedula tecnico", "Tlf tecnico que recibe", "Comentarios")

    tabla.column("#0", width=0, stretch=False)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
    tabla.column("Caso", anchor="center", width=140)
    tabla.column("Orden de compra", anchor="center", width=140)
    tabla.column("Sede", anchor="center", width=140)
    tabla.column("Gestor", anchor="center", width=140)
    tabla.column("Resumen del caso", anchor="center", width=140)
    tabla.column("Insumo", anchor="center", width=140)
    tabla.column("Cantidad", anchor="center", width=140)
    tabla.column("Tipo", anchor="center", width=140)
    tabla.column("Valor materiales", anchor="center", width=140)
    tabla.column("Valor envio", anchor="center", width=140)
    tabla.column("Direccion cliente", anchor="center", width=140)
    tabla.column("Ciudad entrega", anchor="center", width=140)
    tabla.column("Tecnico que recibe", anchor="center", width=140)
    tabla.column("Cedula tecnico", anchor="center", width=140)
    tabla.column("Tlf tecnico que recibe", anchor="center", width=140)
    tabla.column("Comentarios", anchor="center", width=140)

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("Fecha de solicitud",
                  text="Fecha de solicitud", anchor="center")
    tabla.heading("Cliente", text="Cliente", anchor="center")
    tabla.heading("Caso", text="Caso", anchor="center")
    tabla.heading("Orden de compra", text="Orden de compra", anchor="center")
    tabla.heading("Sede", text="Sede", anchor="center")
    tabla.heading("Gestor", text="Gestor", anchor="center")
    tabla.heading("Resumen del caso", text="Resumen del caso", anchor="center")
    tabla.heading("Insumo", text="Insumo solicitado", anchor="center")
    tabla.heading("Cantidad", text="Cantidad", anchor="center")
    tabla.heading("Tipo", text="Tipo", anchor="center")
    tabla.heading("Valor materiales",
                  text="Valor de materiales", anchor="center")
    tabla.heading("Valor envio", text="Valor de envío", anchor="center")
    tabla.heading("Direccion cliente",
                  text="Dirección cliente", anchor="center")
    tabla.heading("Ciudad entrega", text="Ciudad de entrega", anchor="center")
    tabla.heading("Tecnico que recibe",
                  text="Técnico que recibe", anchor="center")
    tabla.heading("Cedula tecnico", text="Cédula de técnico", anchor="center")
    tabla.heading("Tlf tecnico que recibe",
                  text="Tlf técnico que recibe", anchor="center")
    tabla.heading("Comentarios", text="Comentarios", anchor="center")

    conn = mysql.connector.connect(user="root", password="0000",
                                   host=importar_host(),
                                   database="RCC",
                                   port="3306")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM registro_pedidos"
    cursor.execute(instruccion)
    registros = cursor.fetchall()
    for registro in registros:
        tabla.insert('', 'end', values=registro)
    tabla.pack()

    ventana.mainloop()


if __name__ == '__main__':
    ventana = tkinter.Tk()
    ventana.mainloop()
