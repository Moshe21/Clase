import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from funciones import *


def abrir_pagos_coordinador():
    def buscador(event):
        ot = buscador_entry.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        instruccion = f"SELECT * FROM registro_pagos WHERE caso LIKE '{ot}%'"
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)

    def importar_limite():
        conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conexion.cursor()
        sql = f"SELECT monto FROM limite_pagos WHERE destinatario = 'tecnicos'"
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return datos[0]


    def comparacion():
            seleccion = tabla.focus()
            # Verificar si se ha seleccionado una fila
            if seleccion:
                # Obtener los valores de la fila seleccionada
                valores = tabla.item(seleccion, 'values')
                valor_pago = int(valores[16])
                monto_limite = int(importar_limite())
                if valor_pago > monto_limite:
                    messagebox.showerror("Error", "Monto límite excedido")
                else:
                    priorizar_pago()
                    nuevo_limite = monto_limite - valor_pago
                    conexion = mysql.connector.connect(user="root", password="0000",
                                            host=importar_host(),
                                            database="RCC",
                                            port="3306")
                    cursor = conexion.cursor()
                    sql = f"UPDATE limite_pagos SET MONTO = {nuevo_limite} WHERE DESTINATARIO = 'tecnicos'"
                    cursor.execute(sql)
                    conexion.commit()
                    conexion.close()

    def priorizar_pago():
        x = messagebox.askquestion(
                title="Priorizar pago", message="¿Deseas priorizar el registro?")
        if x == 'yes':
            # Obtener la fila seleccionada en el Treeview
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
                transferencia_pago = f'''INSERT INTO pagos_priorizados(fecha_solicitud, comercial_rcc, cliente, caso, resumen_caso, tecnico, banco_tecnico,
                                                            cedula_tecnico, cuenta_tecnico, tipo_cuenta, ciudad, mano_obra, materiales, viaticos, anticipo, valor_pago, oc,
                                                            comentarios) SELECT fecha_solicitud, comercial_rcc, cliente, caso, resumen_caso, tecnico, banco_tecnico,
                                                            cedula_tecnico, cuenta_tecnico, tipo_cuenta, ciudad, mano_obra, materiales, viaticos, anticipo, valor_pago, oc,
                                                            comentarios FROM registro_pagos WHERE id = {id}'''
                cursor.execute(transferencia_pago)
                eliminar_pago = f"DELETE FROM registro_pagos WHERE id = {id}"
                cursor.execute(eliminar_pago)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = "SELECT * FROM registro_pagos"
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                
                messagebox.showinfo("Priorización de registro", "Pago priorizado con éxito.")
            else:
                messagebox.showerror("Error", "No has seleccionado ningún registro.")

    def eliminar_pago():
        x = messagebox.askquestion("Eliminar pago", "¿Deseas eliminar el pago seleccionado?")
        if x == 'yes':
            # Obtener la fila seleccionada en el Treeview
            seleccion = tabla.focus()

            # Verificar si se ha seleccionado una fila
            if seleccion:
                # Obtener los valores de la fila seleccionada
                valores = tabla.item(seleccion, 'values')
                
                # Obtener el valor de la primera columna (índice 0) que contiene el ID
                id = valores[0]
                conn = mysql.connector.connect(user="root", password="0000",
                                            host=importar_host(),
                                            database="RCC",
                                            port="3306")
                cursor = conn.cursor()
                instruccion_delete = f"DELETE FROM registro_pagos WHERE id = {id}"
                cursor.execute(instruccion_delete)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = "SELECT * FROM registro_pagos"
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                messagebox.showinfo("Eliminación de registro", "Pago eliminado con éxito.")

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Revisión de pagos")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 875
    alto_ventana = 460
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.resizable(False, False)
    ventana.iconbitmap("./icon.ico")

    # CREACION DEL MARCO DONDE IRAN LOS WIDGETS CONTENIDOS

    marco_buscador = tkinter.Frame(ventana)
    marco = tkinter.Frame(ventana, padx=5, pady=5)
    marco_buscador.pack(padx=5, pady=5)
    marco_buscador.config(bg="white")
    marco.pack(padx=5, pady=5)
    marco.config(bg="white")

    buscar_label = tkinter.Label(
        marco_buscador, text="Búsqueda por caso", font="Barlow 13 ", bg="white")
    buscador_entry = tkinter.Entry(marco_buscador, font="Barlow 10")

    buscar_label.pack(side="left")
    buscador_entry.pack(fill="x")
    buscador_entry.config(width=95)
    buscador_entry.bind('<Return>', buscador)

    marco_btn = tkinter.Frame(ventana)
    marco_btn.pack(padx=5)
    marco_btn.config(bg="white")

    bienvenido_label_frame = tkinter.LabelFrame(
        marco, text="Revisión y envío de pagos", font=("Barlow ", 15), bg="white", padx=5, pady=5)
    bienvenido_label_frame.pack(pady=5, padx=5)
    # CREACION DE LA TABLA DE VISUALIZACIÓN Y SCROLLBAR

    hscrollbar = ttk.Scrollbar(bienvenido_label_frame, orient="horizontal")
    vscrollbar = ttk.Scrollbar(bienvenido_label_frame, orient="vertical")
    tabla = ttk.Treeview(bienvenido_label_frame, selectmode="extended")

    # DEFINICION DE LAS COLUMNAS DE LA TABLA

    tabla["columns"] = ("ID", "Fecha de solicitud", "Cliente",
                        "Comercial RCC", "Caso",
                        "Resumen del caso", "Técnico", "Banco", "CC",
                        "Cuenta", "Tipo de cuenta", "Ciudad", "Mano de obra",
                        "Materiales", "Viaticos", "Anticipo", "Valor del pago",
                        "OC", "Comentarios")

    # FORMATEAR LAS COLUMNAS

    tabla.column("#0", width=0, stretch=False)
    tabla.column("ID", anchor="center", width=40)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
    tabla.column("Comercial RCC", anchor="center", width=140)
    tabla.column("Caso", anchor="center", width=140)
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
    tabla.heading("Cliente", text="Cliente", anchor="center")
    tabla.heading("Comercial RCC", text="Comercial RCC", anchor="center")
    tabla.heading("Caso", text="Caso", anchor="center")
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

    # CONFIGURACION DE LA TABLA EN EL MARCO

    tabla.configure(xscrollcommand=hscrollbar.set,
                    yscrollcommand=vscrollbar.set)
    hscrollbar.configure(command=tabla.xview)
    vscrollbar.configure(command=tabla.yview)

    # EMPAQUETADO DE TABLA Y SRCOLLBARS EN EL MARCO

    vscrollbar.pack(fill="y", side="right")
    tabla.pack()
    hscrollbar.pack(fill="x", side="bottom")

    # CONEXION DE LA BD CON LA TABLA

    conn = mysql.connector.connect(user='root', password='0000',
                                    host=importar_host(),
                                    database='RCC',
                                    port='3306')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM registro_pagos")
    fetch = cursor.fetchall()
    for datos in fetch:
        tabla.insert("", "end", values=datos)
    conn.commit()
    conn.close()
    # CREACION DE BOTONES PARA ENVIAR Y EXPORTAR REGISTROS

    priorizar_btn = tkinter.Button(marco_btn, text="Priorizar",
                                    bd=0, relief="flat",
                                    font=("Barlow 15"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=33,
                                    command=comparacion)
    priorizar_btn.grid(column=0, row=0, columnspan=2)
    priorizar_btn.bind("<Enter>", lambda event: hover_on(event, priorizar_btn))
    priorizar_btn.bind("<Leave>", lambda event: hover_off(event, priorizar_btn))

    eliminar_btn = tkinter.Button(marco_btn, text="Eliminar",
                                    bd=0, relief="flat",
                                    font=("Barlow 15"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=33,
                                    command=eliminar_pago)
    eliminar_btn.grid(column=2, row=0)
    eliminar_btn.bind("<Enter>", lambda event: hover_on(event, eliminar_btn))
    eliminar_btn.bind("<Leave>", lambda event: hover_off(event, eliminar_btn))

    total_label = tkinter.Label(marco_btn, text="Monto Límite de Pago", bg="white", font="Barlow 30 ")
    total_label.grid(column= 0, row= 1, columnspan=2)

    monto_label = tkinter.Label(marco_btn, bg="white", font="Barlow 30 ")
    monto_label.grid(column= 2, row= 1)

    valor_limite = str(importar_limite())
    resultado_formateado = formatear_monto(valor_limite)   

    monto_label.config(text=resultado_formateado)

    for widget in marco_btn.winfo_children():
        widget.grid_configure(padx= 10)

    ventana.mainloop()