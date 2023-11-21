import tkinter
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from funciones import *


def abrir_pagos_proveedor(fecha, cliente, caso, comercial, oc, proveedor, ciudad, resumen, comentarios):

    def importar_limite():
        conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conexion.cursor()
        sql = f"SELECT monto FROM limite_pagos WHERE destinatario = 'proveedores'"
        cursor.execute(sql)
        datos = cursor.fetchone()
        conexion.commit()
        conexion.close()
        return datos[0]

    def comparacion():
        valor_pago = int(quitar_formato(valor_pago_entry))
        monto_limite = int(importar_limite())
        if valor_pago > monto_limite:
            messagebox.showerror("", "Monto límite excedido")
        else:
            registrar_datos()
            nuevo_limite = monto_limite - valor_pago
            conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
            cursor = conexion.cursor()
            sql = f"UPDATE limite_pagos SET MONTO = {nuevo_limite} WHERE DESTINATARIO = 'proveedores'"
            cursor.execute(sql)
            conexion.commit()
            conexion.close()
                      

    ventana = tkinter.Toplevel()
    ventana.title("Scrum Manager | Pagos a Proveedores")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 885
    alto_ventana = 620
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    # CREACION DEL MARCO DONDE IRÁN CONTENIDOS LOS WIDGETS

    marco = tkinter.Frame(ventana)
    marco.pack(padx=10, pady=10)
    marco.config(bg="white")

    # LABEL FRAME PARA EL INGRESO DE DATOS

    registro_info_frame = tkinter.LabelFrame(
        marco, text="Registra tu pago")
    registro_info_frame.pack(padx=5, pady=5, fill="x")
    registro_info_frame.config(
        bg="white", foreground="black", font="Barlow 13 ")

    # WIDGETS PARA EL INGRESO DE DATOS

    etiqueta_fecha = tkinter.Label(
        registro_info_frame, text="Fecha de solicitud", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_fecha.grid(column=0, row=0)

    fecha_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    fecha_entry.grid(column=1, row=0)
    fecha_entry.insert(0, fecha)
    # fecha_entry.bind("<KeyRelease>", lambda event: FormatoFecha('', event, fecha_entry))

    etiqueta_cliente = tkinter.Label(registro_info_frame, text="Cliente", font="Barlow 11", bg="white", foreground="black")
    etiqueta_cliente.grid(column=0, row=1)

    cliente_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    cliente_combobox.grid(column=1, row=1)
    cliente_combobox.set(cliente)

    etiqueta_ot = tkinter.Label(
        registro_info_frame, text="Caso", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_ot.grid(column=0, row=2)

    ot_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    ot_combobox.grid(column=1, row=2)
    ot_combobox.set(caso)

    etiqueta_comercial = tkinter.Label(
        registro_info_frame, text="Comercial RCC", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_comercial.grid(column=0, row=3)

    comercial_combobox = ttk.Combobox(registro_info_frame, state="readonly")
    comercial_combobox.grid(column=1, row=3)
    comercial_combobox.set(comercial)

    etiqueta_oc = tkinter.Label(
        registro_info_frame, text="OC", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_oc.grid(column=0, row=4)

    oc_combobox = ttk.Combobox(registro_info_frame, state="readonly")
    oc_combobox.grid(column=1, row=4)
    oc_combobox.set(oc)

    etiqueta_proveedor = tkinter.Label(
        registro_info_frame, text="Proveedor", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_proveedor.grid(column=2, row=0)

    def select_datos_principales(event):
        proveedor = proveedor_combobox.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT banco FROM proveedores WHERE razon_social ='{proveedor}'")
        busqueda_banco = cursor.fetchall()
        banco_tecnico = []
        for dato in busqueda_banco:
            banco_tecnico.append(dato[0])
        cursor.execute(
            f"SELECT DISTINCT nit FROM proveedores WHERE razon_social = '{proveedor}'")
        cc_tecnico = cursor.fetchall()
        banco_combobox.set("")
        nit_combobox.set("")
        banco_combobox.config(values=banco_tecnico)
        nit_combobox.config(values=cc_tecnico)
        conn.commit()
        conn.close()

    proveedor_combobox = tkinter.Entry(registro_info_frame, font="Barlow 10")
    proveedor_combobox.grid(column=3, row=0)
    proveedor_combobox.insert(0, proveedor)
    proveedor_combobox.bind("<FocusOut>", select_datos_principales)

    etiqueta_banco = tkinter.Label(
        registro_info_frame, text="Banco", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_banco.grid(column=2, row=1)

    def select_cuenta(event):
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conn.cursor()
        proveedor = proveedor_combobox.get()
        banco = banco_combobox.get()
        cursor.execute(
            f"SELECT cuenta FROM proveedores WHERE razon_social = '{proveedor}' and banco = '{banco}'")
        nro_cuenta = cursor.fetchall()
        cursor.execute(
            f"SELECT tipo_cuenta FROM proveedores WHERE razon_social = '{proveedor}' and banco = '{banco}'")
        tipo_cuenta = cursor.fetchall()
        cuenta_combobox.set("")
        tipo_cuenta_combobox.set("")
        tipo_cuenta_combobox.config(values=tipo_cuenta)
        cuenta_combobox.config(values=nro_cuenta)
        conn.commit()
        conn.close()

    banco_combobox = ttk.Combobox(
        registro_info_frame, values="", state="readonly")
    banco_combobox.grid(column=3, row=1)
    banco_combobox.bind("<<ComboboxSelected>>", select_cuenta)

    etiqueta_nit = tkinter.Label(
        registro_info_frame, text="Nit", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_nit.grid(column=2, row=2)

    nit_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    nit_combobox.grid(column=3, row=2)

    etiqueta_cuenta = tkinter.Label(
        registro_info_frame, text="Cuenta", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_cuenta.grid(column=2, row=3)

    cuenta_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    cuenta_combobox.grid(column=3, row=3)

    etiqueta_tipo_cuenta = tkinter.Label(
        registro_info_frame, text="Tipo de cuenta", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_tipo_cuenta.grid(column=2, row=4)

    tipo_cuenta_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    tipo_cuenta_combobox.grid(column=3, row=4)

    etiqueta_valor_pago = tkinter.Label(
        registro_info_frame, text="Valor del pago", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_valor_pago.grid(column=4, row=2)

    valor_pago_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    valor_pago_entry.grid(column=5, row=2)
    valor_pago_entry.bind("<FocusIn>", lambda event: vaciar_entry(event, valor_pago_entry))
    valor_pago_entry.bind("<FocusOut>", lambda event: formatear_entry(event, valor_pago_entry))

    etiqueta_ciudad = tkinter.Label(
        registro_info_frame, text="Ciudad", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_ciudad.grid(column=4, row=0)

    ciudad_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    ciudad_entry.grid(column=5, row=0)
    ciudad_entry.insert(0, ciudad)

    etiqueta_resumen = tkinter.Label(
        registro_info_frame, text="Resumen del caso", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_resumen.grid(column=4, row=1)

    resumen_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    resumen_entry.grid(column=5, row=1)
    resumen_entry.insert(0, resumen)

    

    etiqueta_comentarios = tkinter.Label(
        registro_info_frame, text="Comentarios", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_comentarios.grid(column=4, row=3)

    comentarios_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    comentarios_entry.grid(column=5, row=3)
    comentarios_entry.insert(0,comentarios)

    # ESPACIO ENTRE WIDGETS CONTENIDOS EN EL LABEL FRAME

    for widget in registro_info_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # CEACION DE SCROLLBAR

    barra_desplazamiento = ttk.Scrollbar(marco, orient="horizontal")

    # TABLA DE VISUALIZACIÓN DE DATOS INGRESADOS

    tabla = ttk.Treeview(marco, selectmode="browse")
    tabla.configure(xscrollcommand=barra_desplazamiento.set)
    tabla.pack(padx=5, fill="x")
    barra_desplazamiento.pack(padx=5, fill="x")

    # CONFIGURACION DE SCROLLBAR

    barra_desplazamiento.configure(command=tabla.xview)

    # DEFINICION DE LAS COLUMNAS DE LA TABLA

    tabla['columns'] = ("Fecha de solicitud", "Cliente", "Caso", "Comercial RCC",
                        "OC", "Proveedor", "Banco", "Nit", "Cuenta", "Tipo de cuenta",
                        "Ciudad", "Resumen del caso", "Valor del pago", "Comentarios")

    # FORMATEAR LAS COLUMNAS

    tabla.column("#0", width=0, stretch=False)
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
    tabla.heading("Fecha de solicitud",
                  text="Fecha de solicitud", anchor="center")
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

    # CREACIÓN DE FUNCIÓN PARA TOMAR LOS DATOS INGRESADOS Y REGISTRARLOS EN LA BD

    def registrar_datos():
        fecha = fecha_entry.get()
        cliente = cliente_combobox.get()
        caso = ot_combobox.get()
        comercial_rcc = comercial_combobox.get()
        oc = oc_combobox.get()
        proveedor = proveedor_combobox.get()
        banco_proveedor = banco_combobox.get()
        nit_proveedor = nit_combobox.get()
        cuenta_proveedor = cuenta_combobox.get()
        tipo_cuenta = tipo_cuenta_combobox.get()
        ciudad = ciudad_entry.get().upper()
        resumen_caso = resumen_entry.get().upper()
        valor_pago = quitar_formato(valor_pago_entry)
        comentarios = comentarios_entry.get().upper()

        if fecha and cliente and comercial_rcc and caso and oc and resumen_caso and proveedor and nit_proveedor and cuenta_proveedor and banco_proveedor and ciudad and valor_pago and comentarios and tipo_cuenta:
            fecha_entry.delete(0, 'end')
            cliente_combobox.set("")
            comercial_combobox.set("")
            ot_combobox.set("")
            resumen_entry.delete(0, 'end')
            proveedor_combobox.delete(0, 'end')
            nit_combobox.set("")
            cuenta_combobox.set("")
            banco_combobox.set("")
            ciudad_entry.delete(0, 'end')
            valor_pago_entry.delete(0, 'end')
            oc_combobox.set("")
            comentarios_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            fecha_entry.focus_set()

            # VIZUALIZACION DE DATOS REGISTRADOS EN LA TABLA

            tabla.insert("", tkinter.END,
                         values=(fecha, cliente, caso, comercial_rcc, oc, proveedor,
                                 banco_proveedor, nit_proveedor, cuenta_proveedor,
                                 tipo_cuenta, ciudad, resumen_caso, valor_pago, comentarios))
            tabla.pack()

            messagebox.showinfo(title="Registro realizado",
                                message="El registro fue realizado con éxito.")

            # CONEXIÓN A LA BASE DE DATOS EN MYSQL

            conn = mysql.connector.connect(user='root', password='0000',
                                           host=importar_host(),
                                           database='RCC',
                                           port='3306')
            cursor = conn.cursor()
            # INSERTAR DATOS INGRESADOS EN LA BASE DE DATOS
            data_insert_query = f'''INSERT INTO pagos_proveedores (fecha_solicitud, cliente, caso, comercial_rcc, oc,
                    proveedor,  banco_proveedor, nit_proveedor, cuenta_proveedor, tipo_cuenta, ciudad, resumen_caso, valor_pago,
                    comentarios) VALUES ('{fecha}', '{cliente}', '{caso}', '{comercial_rcc}', '{oc}', '{proveedor}', '{banco_proveedor}',
                    '{nit_proveedor}', '{cuenta_proveedor}', '{tipo_cuenta}', '{ciudad}', '{resumen_caso}', {valor_pago}, '{comentarios}')'''
            cursor.execute(data_insert_query)
            conn.commit()
            conn.close()
            ventana.destroy()
        else:
            messagebox.showerror(title="Error de registro",
                                 message="Debes llenar los campos obligatorios.")

    # CREACIÓN DE BOTÓN PARA REGISTRAR LOS DATOS INGRESADOS

    boton_registro = tkinter.Button(marco, text="Registrar",
                                    bd=0, relief="flat",
                                    font=("Barlow"),
                                    command=comparacion,
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=75)
    boton_registro.pack(padx=10, pady=10)
    boton_registro.bind(
        "<Enter>", lambda event: hover_on(event, boton_registro))
    boton_registro.bind(
        "<Leave>", lambda event: hover_off(event, boton_registro))

    marco_totales = tkinter.Frame(ventana, bg="white")
    marco_totales.pack()

    etiqueta_monto_limite = tkinter.Label(marco_totales, text="Monto Límite", font="Barlow 30", bg="white", foreground="black")
    etiqueta_monto_limite.grid(column=0, row=0)

    resultado = formatear_monto(str(importar_limite()))

    monto_limite = tkinter.Label(marco_totales, text=str(resultado), font="Barlow 25", bg="white", foreground="black")
    monto_limite.grid(column=1, row=0)

    for widget in marco_totales.winfo_children():
        widget.grid_configure(pady=5, padx=20)


    proveedor_combobox.focus_set()

    ventana.mainloop()
