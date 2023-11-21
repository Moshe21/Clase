import tkinter
from tkinter import ttk
import mysql.connector
from funciones import *


def abrir_check_pagos():
    def buscador(event):
        ot = buscador_entry.get()
        gestor = buscador_entry.get().upper()
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        instruccion = f"SELECT * FROM registro_pagos WHERE ot LIKE '{ot}%' or comercial_rcc like'{gestor}%'"
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Pagos pendientes")
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

    tabla["columns"] = ("ID", "Fecha de solicitud",
                        "Comercial RCC", "Cliente", "OT - Aviso",
                        "Resumen del caso", "Técnico", "Banco", "CC",
                        "Cuenta", "Tipo de cuenta", "Ciudad", "Mano de obra",
                        "Materiales", "Viaticos", "Anticipo", "Valor del pago",
                        "OC", "Comentarios")

    # FORMATEAR LAS COLUMNAS

    tabla.column("#0", width=0, stretch=False)
    tabla.column("ID", anchor="center", width=40)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Comercial RCC", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
    tabla.column("OT - Aviso", anchor="center", width=140)
    tabla.column("Resumen del caso", anchor="center", width=140)
    tabla.column("Técnico", anchor="center", width=140)
    tabla.column("Banco", anchor="center", width=140)
    tabla.column("CC", anchor="center", width=140)
    tabla.column("Cuenta", anchor="center", width=140)
    tabla.column("Tipo de cuenta", anchor="center", width=140)
    tabla.column("Ciudad", anchor="center", width=140)
    tabla.column("Mano de obra", anchor="center", width=140)
    tabla.column("Materiales", anchor="center", width=140)
    tabla.column("Viaticos", anchor="center", width=140)
    tabla.column("Anticipo", anchor="center", width=140)
    tabla.column("Valor del pago", anchor="center", width=140)
    tabla.column("OC", anchor="center", width=140)
    tabla.column("Comentarios", anchor="center", width=140)

    # CREACION DE LOS ENCABEZADOS

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("ID", text="ID", anchor="center")
    tabla.heading("Fecha de solicitud", text="Fecha de solicitud", anchor="center")
    tabla.heading("Comercial RCC", text="Comercial RCC", anchor="center")
    tabla.heading("Cliente", text="Cliente", anchor="center")
    tabla.heading("OT - Aviso", text="OT - Aviso", anchor="center")
    tabla.heading("Resumen del caso", text="Resumen del caso", anchor="center")
    tabla.heading("Técnico", text="Técnico", anchor="center")
    tabla.heading("Banco", text="Banco", anchor="center")
    tabla.heading("CC", text="Cédula", anchor="center")
    tabla.heading("Cuenta", text="Cuenta", anchor="center")
    tabla.heading("Tipo de cuenta", text="Tipo de cuenta", anchor="center")
    tabla.heading("Ciudad", text="Ciudad", anchor="center")
    tabla.heading("Mano de obra", text="Mano de obra", anchor="center")
    tabla.heading("Materiales", text="Materiales", anchor="center")
    tabla.heading("Viaticos", text="Viáticos", anchor="center")
    tabla.heading("Anticipo", text="Anticipo", anchor="center")
    tabla.heading("Valor del pago", text="Valor del pago", anchor="center")
    tabla.heading("OC", text="OC", anchor="center")
    tabla.heading("Comentarios", text="Comentarios", anchor="center")

    conn = mysql.connector.connect(user="root", password="0000",
                                   host=importar_host(),
                                   database="RCC",
                                   port="3306")
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM registro_pagos"
    cursor.execute(instruccion)
    registros = cursor.fetchall()
    for registro in registros:
        tabla.insert('', 'end', values=registro)
    tabla.pack()

    ventana.mainloop()
