import tkinter
from tkinter import ttk, filedialog
from tkinter import messagebox
import mysql.connector
import pandas as pd
from funciones import *



def abrir_pagos_administrador2():
    def exportar_datos():
        try:
            conn = mysql.connector.connect(user='root', password='0000',
                                            host=importar_host(),
                                            database='RCC',
                                            port='3306')
            instruccion = 'SELECT * FROM pagos_proveedores'
            data_frame = pd.read_sql(instruccion, con=conn)

            conn.close()

            # Exportar el DataFrame a un archivo de Excel
            excel_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])
            data_frame.to_excel(excel_file, index=False)

            
            messagebox.showinfo(title="Proceso exitoso",
                                message="Exportación de pagos realizada con éxito.")
        except:
            messagebox.showerror(title="Cancelación",
                            message="Exportación de pagos cancelada.")
    
    def exportar_historial():
        try:
            conn = mysql.connector.connect(user='root', password='0000',
                                            host=importar_host(),
                                            database='RCC',
                                            port='3306')
            instruccion = 'SELECT * FROM pagos_realizados_proveedores'
            data_frame = pd.read_sql(instruccion, con=conn)

            conn.close()

            # Exportar el DataFrame a un archivo de Excel
            excel_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])
            data_frame.to_excel(excel_file, index=False)

            
            messagebox.showinfo(title="Proceso exitoso",
                                message="Exportación de pagos realizada con éxito.")
        except:
            messagebox.showinfo(title="Cancelación",
                            message="Exportación de historial cancelada.")

    def buscador(event):
        caso = buscador_entry.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        instruccion = f"SELECT * FROM pagos_proveedores WHERE caso LIKE '{caso}%'"
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)
    
    def realizar_pago():
            x = messagebox.askquestion(
                title="Priorizar pago", message="¿Deseas cambiar el estado del registro?")
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
                    transferencia_pago = f'''INSERT INTO pagos_realizados_proveedores(fecha_solicitud, cliente, caso, comercial_rcc, oc, proveedor, banco_proveedor, nit_proveedor,
                    cuenta_proveedor, tipo_cuenta, ciudad, resumen_caso, valor_pago, comentarios) SELECT fecha_solicitud, cliente, caso, comercial_rcc, oc, proveedor, banco_proveedor,
                    nit_proveedor, cuenta_proveedor, tipo_cuenta, ciudad, resumen_caso, valor_pago, comentarios FROM pagos_proveedores WHERE id = "{id}"'''
                    cursor.execute(transferencia_pago)
                    eliminar_pago = f"DELETE FROM pagos_proveedores WHERE id = '{id}'"
                    cursor.execute(eliminar_pago)
                    filas = tabla.get_children()
                    for fila in filas:
                        tabla.delete(fila)
                    instruccion_refresh = "SELECT * FROM pagos_proveedores"
                    cursor.execute(instruccion_refresh)
                    registros = cursor.fetchall()
                    for registro in registros:
                        tabla.insert('', 'end', values=registro)
                    tabla.pack()
                    conn.commit()
                    conn.close()

                    messagebox.showinfo("Cambio de estado", "Pago realizado con éxito.")
                else:
                    messagebox.showerror("Error", "No has seleccionado ningún registro.")

    def mostrar_priorizados():
        tabla.delete(*tabla.get_children())
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        cursor = conn.cursor()
        instruccion = 'SELECT * FROM pagos_proveedores'
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        for dato in datos:
            tabla.insert("", "end", values=dato)
        conn.commit()
        conn.close()

        pagar_btn.config(state="active")
        exportar_btn.config(state="active")
        conn = mysql.connector.connect(user="root", password="0000",
                                host=importar_host(),
                                database="RCC",
                                port="3306")
        cursor = conn.cursor()
        instruccion = "SELECT SUM(valor_pago) FROM pagos_proveedores"
        cursor.execute(instruccion)
        suma_pagos = cursor.fetchone()
        conn.commit()
        conn.close()

        resultado_mysql = formatear_monto(str(suma_pagos[0]))

        total_label.config(text="Total pago proveedores")
        monto_label.config(text=resultado_mysql)
        
        buscar_label.pack(side="left")
        buscador_entry.pack()

    def mostrar_realizados():
        tabla.delete(*tabla.get_children())
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        cursor = conn.cursor()
        instruccion = 'SELECT * FROM pagos_realizados_proveedores'
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        for dato in datos:
            tabla.insert("", "end", values=dato)
        conn.commit()
        conn.close()
        
        # exportar_btn.config(state="disabled")
        pagar_btn.config(state="disabled")
        conn = mysql.connector.connect(user="root", password="0000",
                                host=importar_host(),
                                database="RCC",
                                port="3306")
        cursor = conn.cursor()
        instruccion = "SELECT SUM(valor_pago) FROM pagos_realizados_proveedores"
        cursor.execute(instruccion)
        suma_pagos = cursor.fetchone()
        conn.commit()
        conn.close()

        resultado_mysql = formatear_monto(str(suma_pagos[0]))

        total_label.config(text="Total pagos realizados")
        monto_label.config(text=resultado_mysql)

        buscar_label.pack_forget()
        buscador_entry.pack_forget()

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Revisión de pagos a proveedores")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 875
    alto_ventana = 560
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
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
    buscador_entry = tkinter.Entry(marco_buscador, font="Barlow 11")

    buscar_label.pack(side="left")
    buscador_entry.pack(fill="x")
    buscador_entry.config(width=95)
    buscador_entry.bind('<Return>', buscador)

    marco_btn = tkinter.Frame(ventana)
    marco_btn.pack(padx=5)
    marco_btn.config(bg="white")

    frame_btn = tkinter.Frame(marco_btn, bg="white", padx=5, pady=5)

    bienvenido_label_frame = tkinter.LabelFrame(
        marco, text="Revisión y envío de pagos", font=("Barlow ", 15), bg="white", padx=5, pady=5)
    bienvenido_label_frame.pack(pady=5, padx=5)
    # CREACION DE LA TABLA DE VISUALIZACIÓN Y SCROLLBAR

    hscrollbar = ttk.Scrollbar(bienvenido_label_frame, orient="horizontal")
    vscrollbar = ttk.Scrollbar(bienvenido_label_frame, orient="vertical")
    tabla = ttk.Treeview(bienvenido_label_frame, selectmode="extended")

    # DEFINICION DE LAS COLUMNAS DE LA TABLA

    tabla['columns'] = ("ID","Fecha de solicitud", "Cliente", "Caso", "Comercial RCC",
                            "OC", "Proveedor", "Banco", "Nit", "Cuenta", "Tipo de cuenta", 
                            "Ciudad", "Resumen del caso", "Valor del pago", "Comentarios")

    # FORMATEAR LAS COLUMNAS

    tabla.column("#0", width=0, stretch=False)
    tabla.column("ID", anchor="center", width=40)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
    tabla.column("Caso", anchor="center", width=140)
    tabla.column("Comercial RCC", anchor="center", width=140)
    tabla.column("OC", anchor="center", width=140)
    tabla.column("Proveedor", anchor="center", width=140)
    tabla.column("Banco", anchor="center", width=140)
    tabla.column("Nit", anchor="center", width=140)
    tabla.column("Cuenta", anchor="center", width=140)
    tabla.column("Tipo de cuenta", anchor="center", width=140)
    tabla.column("Ciudad", anchor="center", width=140)
    tabla.column("Resumen del caso", anchor="center", width=140)
    tabla.column("Valor del pago", anchor="center", width=140)
    tabla.column("Comentarios", anchor="center", width=140)

    # CREACION DE LOS ENCABEZADOS

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("ID", text="ID", anchor="center")
    tabla.heading("Fecha de solicitud", text="Fecha de solicitud", anchor="center")
    tabla.heading("Cliente", text="Cliente", anchor="center")
    tabla.heading("Caso", text="Caso", anchor="center")
    tabla.heading("Comercial RCC", text="Comercial RCC", anchor="center")
    tabla.heading("OC", text="OC", anchor="center")
    tabla.heading("Proveedor", text="Proveedor", anchor="center")
    tabla.heading("Banco", text="Banco", anchor="center")
    tabla.heading("Nit", text="Nit", anchor="center")
    tabla.heading("Cuenta", text="Cuenta", anchor="center")
    tabla.heading("Tipo de cuenta", text="Tipo de cuenta", anchor="center")
    tabla.heading("Ciudad", text="Ciudad", anchor="center")
    tabla.heading("Resumen del caso", text="Resumen del caso", anchor="center")
    tabla.heading("Valor del pago", text="Valor del pago", anchor="center")
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
    cursor.execute("SELECT * FROM pagos_proveedores")
    fetch = cursor.fetchall()
    for datos in fetch:
        tabla.insert("", "end", values=datos)
    conn.commit()
    conn.close()
    # CREACION DE BOTONES PARA ENVIAR Y EXPORTAR REGISTROS


    exportar_btn = tkinter.Button(marco_btn, text="Exportar",
                                bd=0, relief="flat",
                                font=("Barlow 15"),
                                cursor="hand2",
                                width=33,
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                command=exportar_datos)
    exportar_btn.grid(column=0, row=1, columnspan=2)
    exportar_btn.bind('<Enter>', lambda event: hover_on(event, exportar_btn))
    exportar_btn.bind('<Leave>', lambda event: hover_off(event, exportar_btn))

    pagar_btn = tkinter.Button(marco_btn, text="Pagar",
                                bd=0, relief="flat",
                                font=("Barlow 15"),
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width=33,
                                command=realizar_pago)
    pagar_btn.grid(column=2, row=1)
    pagar_btn.bind("<Enter>", lambda event: hover_on(event, pagar_btn))
    pagar_btn.bind("<Leave>", lambda event: hover_off(event, pagar_btn))

    priorizados_btn = tkinter.Button(marco_btn, text="Priorizados",
                                        bd=0, relief="flat",
                                        font=("Barlow 11"),
                                        cursor="hand2",
                                        width=45,
                                        bg="#282e35",
                                        foreground="#00d2ff",
                                        activebackground="#282e35",
                                        activeforeground="#00d2ff",
                                        command=mostrar_priorizados)
    priorizados_btn.grid(column=0, row=2, columnspan=2)
    priorizados_btn.bind("<Enter>", lambda event: hover_on(event, priorizados_btn))
    priorizados_btn.bind("<Leave>", lambda event: hover_off(event, priorizados_btn))

    pagados_btn = tkinter.Button(marco_btn, text="Pagos realizados",
                                    bd=0, relief="flat",
                                    font=("Barlow 11"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=45,
                                    command=mostrar_realizados)
    pagados_btn.grid(column=2, row=2)
    pagados_btn.bind("<Enter>", lambda event: hover_on(event, pagados_btn))
    pagados_btn.bind("<Leave>", lambda event: hover_off(event, pagados_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    marco_totales = tkinter.Frame(ventana, bg="white")
    marco_totales.pack()

    total_label = tkinter.Label(marco_totales, text="Total pago proveedores", bg="white", font="Barlow 30")
    total_label.grid(column= 0, row= 4, columnspan=2)

    monto_label = tkinter.Label(marco_totales, bg="white", font="Barlow 30")
    monto_label.grid(column= 2, row= 4)

    conn = mysql.connector.connect(user="root", password="0000",
                                host=importar_host(),
                                database="RCC",
                                port="3306")
    cursor = conn.cursor()
    instruccion = "SELECT SUM(valor_pago) FROM pagos_proveedores"
    cursor.execute(instruccion)
    suma_pagos = cursor.fetchone()
    conn.commit()
    conn.close()

    resultado_mysql = formatear_monto(str(suma_pagos[0]))

    monto_label.config(text=resultado_mysql)



    for widget in marco_totales.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    ventana.mainloop()


