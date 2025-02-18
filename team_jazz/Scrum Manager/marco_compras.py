
import tkinter 
from tkinter import tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog




def abrir_modulo_compras():
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Compras")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 1020
    alto_ventana = 570
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 20)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco_buscador = tkinter.Frame(ventana, bg="white")

    marco = tkinter.Frame(ventana, bg="white")

    marco_btn = tkinter.Frame(ventana, bg="white")

    marco_buscador.pack(padx=10, pady=20)
    marco.pack(padx=10, pady=20)
    marco_btn.pack(padx=20)

    marco_menu = tkinter.Frame(ventana, height=600, width=0)
    marco_menu.config(bg="white")
    marco_menu.place(x=0, y=50)

    def desplegar():
        ancho = marco_menu.winfo_width()
        if ancho < 250:
            marco_menu.config(width=250)
            crear_oc = tkinter.Button(marco_menu, image=oc_img, cursor="hand2", bg="white", bd=0, activebackground="white",
                                      text="Crear OC", font="Barlow 11", compound="left")
            crear_oc.place(x=30, y=30)
            reg_proveedor = tkinter.Button(marco_menu, image=reg_proveedor_img, cursor="hand2", bg="white", bd=0, activebackground="white",
                                           text="Reg. proveedor", font="Barlow 11", compound="left")
            reg_proveedor.place(x=30, y=110)

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
    main_btn.place(x=8, y=8)

    oc_img = tkinter.PhotoImage(file="./gestion/oc_img.png")
    reg_proveedor_img = tkinter.PhotoImage(file="./gestion/reg_tecnico_img.png")
   
    buscar_label = tkinter.Label(
        marco_buscador, text="Búsqueda por caso / gestor", font="Barlow 11 ", bg="white")
    buscador_entry = tkinter.Entry(marco_buscador, font="Barlow 11")

