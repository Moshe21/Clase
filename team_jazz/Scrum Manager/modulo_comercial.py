import tkinter
from tkinter import ttk
from modulo_pagos import validacion_horario_pagos
from modulo_pedidos import validacion_horario_pedidos
from check_pedidos import abrir_check_pedidos
from check_pagos import abrir_check_pagos
from SEGUIMIENTO_GESTOR import *
from MODULO_AFILIACIONES import *
from novedades_afiliaciones import novedades
import datetime


def abrir_modulo_afiliaciones(useri):
    hora_actual = datetime.datetime.now().time()
    hora_limite = datetime.time(16, 0, 0)

    if hora_actual >= hora_limite:
        messagebox.showerror(
            "Tiempo finalizado", "No estás dentro de la hora de afiliaciones permitida")
    else:
        Gestor_Afiliaciones((useri))


def chek_afiliaciones():
    novedades()


def abrir_modulo_comercial(user):
    usuario_ingreso = user
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Modulo Gestor")
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

    Gestor(user, marco_tabla, ventana)

    marco_menu = tkinter.Frame(ventana, height=600, width=0)
    marco_menu.config(bg="white")
    marco_menu.place(x=0, y=50)

    def desplegar():
        ancho = marco_menu.winfo_width()
        if ancho < 270:
            marco_menu.config(width=270)
            btn_pagos = tkinter.Button(marco_menu, cursor="hand2", bg="white", bd=0, image=img_pagos, text="Pagos",
                                       activebackground="white", font="Barlow 11", compound="left", command=lambda: validacion_horario_pagos(user))
            btn_pagos.place(x=35, y=30)
            btn_afiliacion = tkinter.Button(marco_menu, image=img_afiliacion, cursor="hand2", bg="white", bd=0, activebackground="white",
                                            text="Afiliación", font="Barlow 11", compound="left", command=lambda: abrir_modulo_afiliaciones(usuario_ingreso))
            btn_afiliacion.place(x=20, y=90)
            btn_compras = tkinter.Button(marco_menu, image=img_compras, cursor="hand2", bg="white", bd=0, activebackground="white",
                                         text="Compras", font="Barlow 11", compound="left", command=lambda: validacion_horario_pedidos(user))
            btn_compras.place(x=25, y=160)
            rev_pagos = tkinter.Button(marco_menu, image=rev_img_pagos, cursor="hand2", bg="white", bd=0, activebackground="white",
                                       text="Revision de pagos", font="Barlow 11", compound="left", command=abrir_check_pagos)
            rev_pagos.place(x=35, y=230)
            rev_afiliacion = tkinter.Button(marco_menu, image=rev_img_afiliacion, cursor="hand2", bg="white",
                                            bd=0, activebackground="white", text="Revision de afiliación", font="Barlow 11", compound="left", command=chek_afiliaciones)
            rev_afiliacion.place(x=20, y=290)
            rev_compras = tkinter.Button(marco_menu, image=rev_img_compras, cursor="hand2", bg="white", bd=0, activebackground="white",
                                         text="Revisión de compras", font="Barlow 11", compound="left", command=abrir_check_pedidos)
            rev_compras.place(x=26, y=370)

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

    img_pagos = tkinter.PhotoImage(file="./gestion/pagos_img.png")
    img_afiliacion = tkinter.PhotoImage(file="./gestion/arl_img.png")
    img_compras = tkinter.PhotoImage(file="./gestion/compras_img.png")
    rev_img_pagos = tkinter.PhotoImage(file="./revision/pagos_img.png")
    rev_img_afiliacion = tkinter.PhotoImage(file="./revision/arl_img.png")
    rev_img_compras = tkinter.PhotoImage(file="./revision/compras_img.png")

    ventana.mainloop()
