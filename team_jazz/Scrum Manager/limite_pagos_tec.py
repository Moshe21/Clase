import tkinter
from tkinter import messagebox
import mysql.connector
from funciones import *


def abrir_limites_pagos_tec():
    def establecer_limite():
        valor = entry.get()
        conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conexion.cursor()
        sql = f"UPDATE limite_pagos SET MONTO = {valor} WHERE DESTINATARIO = 'tecnicos'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Proceso exitoso","El limite se ha establecido de manera satisfactoria")
        ventana.destroy()

    ventana = tkinter.Toplevel()
    ventana.title("Scrum Manager | Limite de pago a Técnicos")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 390
    alto_ventana = 210
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco = tkinter.Frame(ventana, bg="white")
    marco.pack(padx=10, pady=10)

    label = tkinter.Label(
        marco, text="Establece un monto límite diario", bg="white", font="Barlow 17")
    label.grid(column=0, row=0)

    entry = tkinter.Entry(marco, font="Barlow 11", width=42)
    entry.grid(column=0, row=1)

    button = tkinter.Button(marco, text="Establecer",
                            bd=0, relief="flat",
                            cursor="hand2",
                            bg="#282e35",
                            foreground="#00d2ff",
                            activebackground="#282e35",
                            activeforeground="#00d2ff",
                            font="Barlow 15 bold",
                            command=establecer_limite)
    button.grid(column=0, row=2, columnspan=2, sticky="we")
    button.bind("<Enter>", lambda event: hover_on(event, button))
    button.bind("<Leave>", lambda event: hover_off(event, button))

    for widget in marco.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    entry.focus_set()

    ventana.mainloop()
