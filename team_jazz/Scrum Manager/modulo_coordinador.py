import tkinter
from tkinter import ttk
from tkinter import Menu
from pagos_coordinador import abrir_pagos_coordinador
import SEGUIMIENTO_COORDINADOR
from SEGUIMIENTO_COORDINADOR import *


def abrir_modulo_coordinador(user):
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Coordinador")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 1200
    alto_ventana = 720
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 50)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco_tabla = tkinter.Frame(ventana)
    marco_tabla.config(bg="white")
    marco_tabla.pack(padx=50, pady=50)

    marco_menu = tkinter.Frame(ventana, height=600, width=0)
    marco_menu.config(bg="white")
    marco_menu.place(x=0, y=50)

    Coordinador(user, marco_tabla, ventana)

    def desplegar():
        ancho = marco_menu.winfo_width()
        ancho += 20
        if ancho < 270:
            marco_menu.config(width=270)
            rev_pagos = tkinter.Button(marco_menu, image=rev_img_pagos, cursor="hand2", bg="white", bd=0, activebackground="white",
                                       text="Revision de pagos", font="Barlow 14", compound="left", command=abrir_pagos_coordinador)
            rev_pagos.place(x=30, y=30)

    def esconder():
        ancho = marco_menu.winfo_width()
        if ancho > 0:
            marco_menu.config(width=0)

    def toggle():

        ancho = marco_menu.winfo_width()

        if ancho == 1:
            desplegar()
            main_btn.config(image=img_close)
        else:
            esconder()
            main_btn.config(image=img_menu)

    img_menu = tkinter.PhotoImage(file="./menu.png")
    img_close = tkinter.PhotoImage(file="./close.png")
    main_btn = tkinter.Button(ventana, image=img_menu, cursor="hand2", bg="white",
                              bd=0, text=" ", activebackground="white", compound="left", command=toggle)
    main_btn.place(x=5, y=5)

    rev_img_pagos = tkinter.PhotoImage(file="./revision/pagos_img.png")

    ventana.mainloop()
