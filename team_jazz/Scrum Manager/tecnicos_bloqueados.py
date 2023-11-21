import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from funciones import *


def abrir_tecnicos_bloqueados():
    
    def bloquear_tecnico():
        x = messagebox.askquestion("Técnicos Bloqueados","¿Deseas desbloquear el técnico?")
        if x == 'yes':
            seleccion = tabla.focus()

            # Verificar si se ha seleccionado una fila
            if seleccion:
                # Obtener los valores de la fila seleccionada
                valores = tabla.item(seleccion, 'values')
                
                # Obtener el valor de la primera columna (índice 0) que contiene el ID
                id = valores[0]

                conn = mysql.connector.connect(user='root', password='0000',
                                                host=importar_host(),
                                                database='RCC',
                                                port='3306')
                cursor = conn.cursor()
                instruccion = f"""INSERT INTO tecnicos (nombre, cc, cuenta, tipo_cuenta, banco, telefono, regimen, pension, eps, caja_compensacion) SELECT nombre, cc, cuenta, tipo_cuenta, banco, telefono, regimen, pension, eps, caja_compensacion FROM tecnicos_bloqueados WHERE id = {id}"""
                cursor.execute(instruccion)
                eliminar_tecnico = f"DELETE FROM tecnicos_bloqueados WHERE id = {id}"
                cursor.execute(eliminar_tecnico)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = "SELECT * FROM tecnicos_bloqueados"
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                messagebox.showinfo("Proceso exitoso","El técnico se ha desbloqueado con éxito.")

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Técnicos bloqueados")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 635
    alto_ventana = 320
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 30)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco = tkinter.Frame(ventana)
    marco.pack(padx=10, pady=10, fill="x")
    marco.config(bg="white")

    marco_btn = tkinter.Frame(ventana, bg="white")
    marco_btn.pack(padx=50, pady=5)

    vertical_bar = ttk.Scrollbar(marco, orient="vertical")
    horizontal_bar = ttk.Scrollbar(marco, orient="horizontal")
    tabla = ttk.Treeview(marco, selectmode="browse")

    tabla.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.configure(command=tabla.yview)
    horizontal_bar.configure(command=tabla.xview)

    tabla["columns"] = ("ID", "Nombre", "Cedula", "Telefono", "Cuenta", "Banco", "Tipo de cuenta",
                        "Regimen", "Pension", "EPS", "Caja de compensacion")

    tabla.column("#0", width=0, stretch=False)
    tabla.column("ID", anchor="center", width=40)
    tabla.column("Nombre", anchor="center", width=140)
    tabla.column("Cedula", anchor="center", width=140)
    tabla.column("Telefono", anchor="center", width=140)
    tabla.column("Cuenta", anchor="center", width=140)
    tabla.column("Banco", anchor="center", width=140)
    tabla.column("Tipo de cuenta", anchor="center", width=140)
    tabla.column("Regimen", anchor="center", width=140)
    tabla.column("Pension", anchor="center", width=140)
    tabla.column("EPS", anchor="center", width=140)
    tabla.column("Caja de compensacion", anchor="center", width=140)

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("ID", text="ID", anchor="center")
    tabla.heading("Nombre", text="Nombre", anchor="center")
    tabla.heading("Cedula", text="Cédula", anchor="center")
    tabla.heading("Telefono", text="Teléfono", anchor="center")
    tabla.heading("Cuenta", text="Cuenta", anchor="center")
    tabla.heading("Banco", text="Banco", anchor="center")
    tabla.heading("Tipo de cuenta", text="Tipo de cuenta", anchor="center")
    tabla.heading("Regimen", text="Régimen", anchor="center")
    tabla.heading("Pension", text="Pensión", anchor="center")
    tabla.heading("EPS", text="EPS", anchor="center")
    tabla.heading("Caja de compensacion",
                    text="Caja de compensación", anchor="center")

    conn = mysql.connector.connect(user='root', password='0000',
                                    host=importar_host(),
                                    database='RCC',
                                    port='3306')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tecnicos_bloqueados")
    datos = cursor.fetchall()
    for dato in datos:
        tabla.insert("", "end", values=dato)
    conn.commit()
    conn.close()

    vertical_bar.pack(fill="y", side="right")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    bloquear_btn = tkinter.Button(marco_btn, text="Desbloquear",
                                    bd=0, relief="flat",
                                    font=("Barlow"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    width=20,
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    state="normal",
                                    command=bloquear_tecnico)
    bloquear_btn.grid(column=0, row=0)
    bloquear_btn.bind("<Enter>", lambda event: hover_on(event, bloquear_btn))
    bloquear_btn.bind("<Leave>", lambda event: hover_off(event, bloquear_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(padx=10)

    ventana.mainloop()
