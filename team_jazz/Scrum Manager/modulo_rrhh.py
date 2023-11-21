import tkinter
from tkinter import ttk
from tkinter import Menu
from registro_tecnico import abrir_registro_tecnico
from tecnicos_bloqueados import abrir_tecnicos_bloqueados
from REVISION_AFILIACIONES import *


def abrir_modulo_rrhh():
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Recursos Humanos")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 1200
    alto_ventana = 690
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 40)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco_tabla = tkinter.Frame(ventana)
    marco_tabla.config(bg="white")
    marco_tabla.pack(padx=50, pady=70)

    MODULO_RRHH(marco_tabla)

    marco_menu = tkinter.Frame(ventana, height=600, width=0)
    marco_menu.config(bg="white")
    marco_menu.place(x= 0, y=50)

    def desplegar(): 
        ancho = marco_menu.winfo_width()
        if ancho < 250:
            marco_menu.config(width=250)
            reg_tecnico_btn = tkinter.Button(marco_menu, cursor="hand2", bg="white", bd=0, image=reg_tecnico_img, text="Ingresar técnico",
                                       activebackground="white",font="Barlow 11" , compound="left", command=abrir_registro_tecnico)
            reg_tecnico_btn.place(x= 30, y=30)

            tecnicos_bloqueados_btn = tkinter.Button(marco_menu, cursor="hand2", bg="white", bd=0, image=tecnicos_bloqueados_img, text="Técnicos bloqueados",
                                       activebackground="white",font="Barlow 11" , compound="left", command=abrir_tecnicos_bloqueados)
            tecnicos_bloqueados_btn.place(x= 30, y=100)
            


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
    main_btn = tkinter.Button(ventana, image=img_menu, cursor="hand2", bg="white", bd=0, text=" ",activebackground="white", compound="left", command= toggle)
    main_btn.place(x=5, y=5)


    reg_tecnico_img = tkinter.PhotoImage(file="./gestion/reg_tecnico_img.png")
    tecnicos_bloqueados_img = tkinter.PhotoImage(file="./gestion/tecnicos_bloqueados.png")

    
    ventana.mainloop()