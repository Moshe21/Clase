import tkinter
from tkinter import ttk
from pagos_administrador_tec import abrir_pagos_administrador1
from pagos_administrador_prov import abrir_pagos_administrador2
from modulo_pagos import abrir_modulo_pagos
from modulo_pedidos import abrir_modulo_pedidos
from limite_pagos_tec import abrir_limites_pagos_tec
from limite_pagos_prov import abrir_limites_pagos_prov
from SEGUIMIENTO_COORDINADOR import *
from MODULO_AFILIACIONES import *
from novedades_afiliaciones import novedades

# from revision_pedidos import abrir_revision_pedidos


def abrir_modulo_afiliaciones(useri):
    Gestor_Afiliaciones((useri))


def chek_afiliaciones():
    novedades()


def abrir_modulo_superusuario(user):
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Gerencia")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 1200
    alto_ventana = 720
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 20)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco_tabla = tkinter.Frame(ventana)
    marco_tabla.config(bg="white")
    marco_tabla.pack(padx=50, pady=50)

    Coordinador(user, marco_tabla, ventana)

    marco_menu = tkinter.Frame(ventana, height=700, width=0)
    marco_menu.config(bg="white")
    marco_menu.place(x=0, y=50)

    def desplegar():
        ancho = marco_menu.winfo_width()
        if ancho < 270:
            marco_menu.config(width=270)
            rev_pagos = tkinter.Button(marco_menu, image=rev_img_pagos, cursor="hand2", bg="white", bd=0, activebackground="white",
                                       text="Pagos a técnicos", font="Barlow 11", compound="left", command=abrir_pagos_administrador1)
            rev_pagos.place(x=35, y=10)
            # rev_pagos.place(x=35, y=220)
            rev_afiliacion = tkinter.Button(marco_menu, image=rev_img_afiliacion, cursor="hand2", bg="white", bd=0,
                                            activebackground="white", text="Revision de afiliación", font="Barlow 11", compound="left", command=chek_afiliaciones)
            rev_afiliacion.place(x=20, y=70)
            # rev_afiliacion.place(x=20, y=280)
            rev_compras = tkinter.Button(marco_menu, image=rev_img_compras, cursor="hand2", bg="white", bd=0, activebackground="white",
                                         text="Pagos a proveedores", font="Barlow 11", compound="left", command=abrir_pagos_administrador2)
            rev_compras.place(x=25, y=150)
            # rev_compras.place(x=27, y=360)
            limite_pagos_tec = tkinter.Button(marco_menu, image=img_limite_pagos, cursor="hand2", bg="white", bd=0, activebackground="white",
                                              text="Límite $ Técnicos", font="Barlow 11", compound="left", command=abrir_limites_pagos_tec)
            limite_pagos_tec.place(x=32, y=220)

            limite_pagos_prov = tkinter.Button(marco_menu, image=img_limite_pagos, cursor="hand2", bg="white", bd=0, activebackground="white",
                                               text="Límite $ Proveedores", font="Barlow 11", compound="left", command=abrir_limites_pagos_prov)
            limite_pagos_prov.place(x=32, y=290)
            dashborad = tkinter.Button(marco_menu, image=img_dashboard, cursor="hand2", bg="white", bd=0, activebackground="white",
                                       text="Estadísticas", font="Barlow 11", compound="left")
            dashborad.place(x=40, y=360)

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
    img_limite_pagos = tkinter.PhotoImage(file="./gestion/limit.png")
    img_dashboard = tkinter.PhotoImage(file="./gestion/informes.png")

    ventana.mainloop()
