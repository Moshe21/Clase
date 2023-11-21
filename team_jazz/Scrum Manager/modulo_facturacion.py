import tkinter
from tkinter import ttk
import usuario_facturacion as UF


def abrir_modulo_facturacion():
    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Facturación")
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

    UF.Facturacion(ventana, marco_tabla)

    img_menu = tkinter.PhotoImage(file="./menu.png")
    
    main_label = tkinter.Label(ventana, image=img_menu, bg="white")
    main_label.place(x=9, y=8)

    ventana.mainloop()
