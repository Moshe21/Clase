import tkinter
from tkinter import ttk
import datetime
import mysql.connector
from tkinter import messagebox
from funciones import *


def validacion_horario_pagos(usuario_ingreso):
    hora_actual = datetime.datetime.now().time()
    hora_limite = datetime.time(11, 0, 0)

    if hora_actual >= hora_limite:
        messagebox.showerror(
            "Tiempo finalizado", "No estás dentro de la hora de pagos permitida")
    else:
        abrir_modulo_pagos(usuario_ingreso)


def abrir_modulo_pagos(usuario_ingresado):
    def select_datos_caso(event):
        caso = caso_entry.get()
        cliente = cliente_combobox.get()
        usuario = comercial_combobox.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        cursor = conn.cursor()
        instruccion_uno = f"SELECT caso FROM casos_rcc WHERE CASO = '{caso}' and CLIENTE ='{cliente}' and GESTOR = '{usuario}'"
        cursor.execute(instruccion_uno)
        validacion = cursor.fetchall()
        if validacion:
            instruccion_dos = f"SELECT OC FROM casos_rcc WHERE CASO ='{caso}'"
            cursor.execute(instruccion_dos)
            oc = cursor.fetchall()
            conn.commit()
            conn.close()
            oc_combobox.set("")
                
            if cliente == 'BDB':
                oc_combobox.config(values="#N/A")
            else:
                oc_combobox.config(values=oc[0])
        else:
            oc_combobox.set("")
            caso_entry.delete(0,'end')
            messagebox.showerror('Caso Incorrecto',f'El caso seleccionado no existe en la base de datos de {usuario.capitalize()}')
            

    def select_datos_principales(event):
        tecnico = tecnico_combobox.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
        cursor = conn.cursor()
        cursor.execute(f"SELECT banco FROM tecnicos WHERE nombre ='{tecnico}'")
        busqueda_banco = cursor.fetchall()
        banco_tecnico = []
        for dato in busqueda_banco:
            banco_tecnico.append(dato[0])
        cursor.execute(f"SELECT DISTINCT cc FROM tecnicos WHERE nombre = '{tecnico}'")
        cc_tecnico = cursor.fetchall()
        banco_combobox.set("")
        cedula_combobox.set("")
        banco_combobox.config(values=banco_tecnico)
        cedula_combobox.config(values=cc_tecnico)
        conn.commit()
        conn.close()

    def select_cuenta(event):
        conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
        cursor = conn.cursor()
        tecnico = tecnico_combobox.get()
        banco = banco_combobox.get()
        cursor.execute(f"SELECT cuenta FROM tecnicos WHERE nombre = '{tecnico}' and banco = '{banco}'")
        nro_cuenta = cursor.fetchall()
        cursor.execute(f"SELECT tipo_cuenta FROM tecnicos WHERE nombre = '{tecnico}' and banco = '{banco}'")
        tipo_cuenta = cursor.fetchall()
        cuenta_combobox.set("")
        tipo_cuenta_combobox.set("")
        tipo_cuenta_combobox.config(values=tipo_cuenta)
        cuenta_combobox.config(values=nro_cuenta)
        conn.commit()
        conn.close()

    # CREACIÓN DE FUNCIÓN PARA TOMAR LOS DATOS INGRESADOS Y REGISTRARLOS EN LA BD

    def registrar_datos():
        fecha = fecha_entry.get()
        comercial_rcc = comercial_combobox.get().upper()
        cliente = cliente_combobox.get()
        caso = caso_entry.get()
        resumen_caso = resumen_entry.get().upper()
        tecnico = tecnico_combobox.get()
        cc_tecnico = cedula_combobox.get()
        cuenta_tecnico = cuenta_combobox.get()
        banco_tecnico = banco_combobox.get()
        ciudad = ciudad_entry.get().upper()
        mano_obra = quitar_formato(mano_obra_entry)
        materiales = quitar_formato(materiales_entry)
        viaticos = quitar_formato(viaticos_entry)
        anticipo = anticipo_combobox.get()
        valor_pago = quitar_formato(valor_pago_entry)
        oc = oc_combobox.get()
        comentarios = comentarios_entry.get().upper()
        tipo_cuenta = tipo_cuenta_combobox.get()

        if fecha and cliente and comercial_rcc and caso and resumen_caso and tecnico and cc_tecnico and cuenta_tecnico and banco_tecnico and ciudad and mano_obra and anticipo and valor_pago and oc and comentarios and tipo_cuenta:
            fecha_entry.delete(0, 'end')
            cliente_combobox.set("")
            comercial_combobox.set("")
            caso_entry.delete(0, 'end')
            resumen_entry.delete(0, 'end')
            tecnico_combobox.set("")
            cedula_combobox.set("")
            cuenta_combobox.set("")
            banco_combobox.set("")
            ciudad_entry.delete(0, 'end')
            mano_obra_entry.delete(0, 'end')
            materiales_entry.delete(0, 'end')
            viaticos_entry.delete(0, 'end')
            anticipo_combobox.set("")
            valor_pago_entry.delete(0, 'end')
            oc_combobox.set("")
            comentarios_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            fecha_entry.focus_set()

            # VIZUALIZACION DE DATOS REGISTRADOS EN LA TABLA

            tabla.insert("", tkinter.END,
                            values=(fecha, comercial_rcc, cliente, caso, resumen_caso,
                                    tecnico, banco_tecnico, cc_tecnico, cuenta_tecnico,
                                    tipo_cuenta, ciudad, mano_obra,materiales, viaticos, 
                                    anticipo, valor_pago, oc, comentarios))
            tabla.pack()

            messagebox.showinfo(title="Registro realizado",
                                message="El registro fue realizado con éxito.")
            # CREACIÓN DE BASE DE DATOS EN MYSQL

            conn = mysql.connector.connect(user='root', password='0000',
                                            host=importar_host(),
                                            database='RCC',
                                            port='3306')
            cursor = conn.cursor()
            # INSERTAR DATOS INGRESADOS EN LA BASE DE DATOS
            data_insert_query = f'''INSERT INTO registro_pagos VALUES (null,'{fecha}', '{comercial_rcc}', '{cliente}', '{caso}', '{resumen_caso}', '{tecnico}', '{banco_tecnico}', '{cc_tecnico}', '{cuenta_tecnico}', 
                                            '{tipo_cuenta}', '{ciudad}', {mano_obra}, {materiales}, {viaticos}, '{anticipo}', {valor_pago}, '{oc}', '{comentarios}')'''
            cursor.execute(data_insert_query)
            conn.commit()
            conn.close()
        else:
            messagebox.showerror(title="Error de registro",
                                    message="Debes llenar los campos obligatorios.")


    ventana = tkinter.Toplevel()
    ventana.title("Scrum Manager | Registro de pagos diarios")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 910
    alto_ventana = 580
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    # CREACION DEL MARCO DONDE IRÁN CONTENIDOS LOS WIDGETS

    marco = tkinter.Frame(ventana)
    marco.pack(padx=11, pady=11)
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
    fecha_entry.bind("<Key>",solo_numeros)
    fecha_entry.bind("<KeyRelease>", lambda event: FormatoFecha("",event, fecha_entry))

    etiqueta_comercial = tkinter.Label(
        registro_info_frame, text="Comercial RCC", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_comercial.grid(column=0, row=1)

    comercial_combobox = ttk.Combobox(registro_info_frame, state="readonly", values=usuario_ingresado)
    comercial_combobox.grid(column=1, row=1)

    etiqueta_cliente = tkinter.Label(
        registro_info_frame, text="Cliente", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_cliente.grid(column=0, row=2)

    conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
    cursor = conn.cursor()
    instruccion = f"SELECT DISTINCT CLIENTE FROM casos_rcc WHERE GESTOR = '{usuario_ingresado}'"
    cursor.execute(instruccion)
    resultados = cursor.fetchall()
    lista_clientes = []
    for resultado in resultados:
        lista_clientes.append(resultado[0])
    conn.commit()
    conn.close()

    cliente_combobox = ttk.Combobox(
        registro_info_frame, state="readonly", values=lista_clientes)
    cliente_combobox.grid(column=1, row=2)

    etiqueta_caso = tkinter.Label(
        registro_info_frame, text="Caso", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_caso.grid(column=0, row=3)

    caso_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    caso_entry.grid(column=1, row=3)
    caso_entry.bind("<FocusOut>", select_datos_caso)

    etiqueta_oc = tkinter.Label(
        registro_info_frame, text="OC", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_oc.grid(column=0, row=4)

    oc_combobox = ttk.Combobox(registro_info_frame, state="readonly")
    oc_combobox.grid(column=1, row=4)

    etiqueta_resumen = tkinter.Label(
        registro_info_frame, text="Resumen del caso", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_resumen.grid(column=0, row=5)

    resumen_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    resumen_entry.grid(column=1, row=5)

    etiqueta_tecnico = tkinter.Label(
        registro_info_frame, text="Técnico", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_tecnico.grid(column=2, row=0)

    conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
    cursor = conn.cursor()
    instruccion = "SELECT DISTINCT nombre FROM tecnicos ORDER BY nombre ASC"
    cursor.execute(instruccion)
    resultados = cursor.fetchall()
    lista_tecnicos = []
    for resultado in resultados:
        lista_tecnicos.append(resultado[0])
    conn.commit()
    conn.close()

    tecnico_combobox = ttk.Combobox(
        registro_info_frame, state="readonly", values=lista_tecnicos)
    tecnico_combobox.grid(column=3, row=0)
    tecnico_combobox.bind("<<ComboboxSelected>>", select_datos_principales)

    etiqueta_banco = tkinter.Label(
        registro_info_frame, text="Banco", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_banco.grid(column=2, row=1)

    banco_combobox = ttk.Combobox(
        registro_info_frame, values="", state="readonly")
    banco_combobox.grid(column=3, row=1)
    banco_combobox.bind("<<ComboboxSelected>>", select_cuenta)

    etiqueta_cedula = tkinter.Label(
        registro_info_frame, text="CC", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_cedula.grid(column=2, row=2)

    cedula_combobox = ttk.Combobox(
        registro_info_frame, state="readonly")
    cedula_combobox.grid(column=3, row=2)

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

    etiqueta_ciudad = tkinter.Label(
        registro_info_frame, text="Ciudad", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_ciudad.grid(column=2, row=5)

    ciudad_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    ciudad_entry.grid(column=3, row=5)

    etiqueta_mano_obra = tkinter.Label(
        registro_info_frame, text="Mano de obra", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_mano_obra.grid(column=4, row=0)

    mano_obra_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    mano_obra_entry.grid(column=5, row=0)
    mano_obra_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event, mano_obra_entry))
    mano_obra_entry.bind("<Key>", lambda event: solo_numeros(event))
    mano_obra_entry.bind("<FocusOut>", lambda event: formatear_entry(event, mano_obra_entry))

    etiqueta_materiales = tkinter.Label(
        registro_info_frame, text="Materiales", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_materiales.grid(column=4, row=1)

    materiales_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    materiales_entry.grid(column=5, row=1)
    materiales_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event, materiales_entry))
    materiales_entry.bind("<Key>", lambda event: solo_numeros(event))
    materiales_entry.bind("<FocusOut>", lambda event: formatear_entry(event, materiales_entry))

    etiqueta_viaticos = tkinter.Label(
        registro_info_frame, text="Viáticos", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_viaticos.grid(column=4, row=2)

    viaticos_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    viaticos_entry.grid(column=5, row=2)
    viaticos_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event, viaticos_entry))
    viaticos_entry.bind("<Key>", lambda event: solo_numeros(event))
    viaticos_entry.bind("<FocusOut>", lambda event: formatear_entry(event, viaticos_entry))

    etiqueta_anticipo = tkinter.Label(
        registro_info_frame, text="Anticipo", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_anticipo.grid(column=4, row=3)

    anticipo_combobox = ttk.Combobox(registro_info_frame, state="readonly", values=["SI", "NO"])
    anticipo_combobox.grid(column=5, row=3)

    etiqueta_valor_pago = tkinter.Label(
        registro_info_frame, text="Valor del pago", font="Barlow 11", bg="white", foreground="black")
    etiqueta_valor_pago.grid(column=4, row=4)

    valor_pago_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    valor_pago_entry.grid(column=5, row=4)
    valor_pago_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event, valor_pago_entry))
    valor_pago_entry.bind("<Key>", lambda event: solo_numeros(event))
    valor_pago_entry.bind("<FocusOut>", lambda event: formatear_entry(event, valor_pago_entry))

    etiqueta_comentarios = tkinter.Label(
        registro_info_frame, text="Comentarios", font="Barlow 11 ", bg="white", foreground="black")
    etiqueta_comentarios.grid(column=4, row=5)

    comentarios_entry = tkinter.Entry(registro_info_frame, font="Barlow 10")
    comentarios_entry.grid(column=5, row=5)

    # ESPACIO ENTRE WIDGETS CONTENIDOS EN EL LABEL FRAME

    for widget in registro_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

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

    tabla['columns'] = ("Fecha de solicitud", "Comercial RCC",
                        "Cliente", "Caso",
                        "Resumen del caso", "Técnico", "Banco", "CC",
                        "Cuenta", "Tipo de cuenta", "Ciudad", "Mano de obra",
                        "Materiales", "Viaticos", "Anticipo", "Valor del pago",
                        "OC", "Comentarios")

    # FORMATEAR LAS COLUMNAS

    tabla.column("#0", width=0, stretch=False)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Comercial RCC", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
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
    tabla.heading("Fecha de solicitud",
                    text="Fecha de solicitud", anchor="center")
    tabla.heading("Comercial RCC", text="Comercial RCC", anchor="center")
    tabla.heading("Cliente", text="Cliente", anchor="center")
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

    boton_registro = tkinter.Button(marco, text="Registrar",
                                    bd=0, relief="flat",
                                    font=("Barlow 15 bold"),
                                    command=registrar_datos,
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=80)
    boton_registro.pack(padx=5, pady=10)
    boton_registro.bind("<Enter>", lambda event: hover_on(event, boton_registro))
    boton_registro.bind("<Leave>", lambda event: hover_off(event, boton_registro))

    ventana.mainloop()