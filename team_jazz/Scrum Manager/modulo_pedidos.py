import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import datetime
from funciones import *

def validacion_horario_pedidos(usuario_ingreso):
    hora_actual = datetime.datetime.now().time()
    hora_limite = datetime.time(11, 0, 0)

    if hora_actual >= hora_limite:
        messagebox.showerror(
            "Tiempo finalizado", "No estás dentro de la hora de pedidos permitida")
    else:
        abrir_modulo_pedidos(usuario_ingreso)

def abrir_modulo_pedidos(usuario_ingresado):
    
    def select_datos_caso(event):
        caso = caso_entry.get()
        cliente = cliente_combobox.get()
        usuario = gestor_combobox.get()
        conn = mysql.connector.connect(user="root", password="0000",
                                        host=importar_host(),
                                        database="RCC",
                                        port="3306")
        cursor = conn.cursor()
        instruccion_uno = f"SELECT caso FROM casos_rcc WHERE CASO = '{caso}' and CLIENTE ='{cliente}' and GESTOR = '{usuario}'"
        cursor.execute(instruccion_uno)
        validacion = cursor.fetchall()
        if validacion:
            instruccion_dos = f"SELECT oc FROM casos_rcc WHERE caso = '{caso}'"
            instruccion_tres = f"SELECT ciudad_sede FROM casos_rcc WHERE caso = '{caso}'"
            cursor = conn.cursor()
            cursor.execute(instruccion_dos)
            oc = cursor.fetchall()
            cursor.execute(instruccion_tres)
            sede = cursor.fetchall()
            conn.commit()
            conn.close()
            oc_combobox.set("")
            sede_combobox.set("")
            if cliente == 'BDB':
                oc_combobox.config(values="#N/A")
                sede_combobox.config(values=sede[0])
            else:
                oc_combobox.config(values=oc[0])
                sede_combobox.config(values=sede[0])
        else:
            oc_combobox.set("")
            sede_combobox.set("")
            caso_entry.delete(0,'end')
            messagebox.showerror('Caso Incorrecto',f'El caso seleccionado no existe en la base de datos de {usuario.capitalize()}')
        
    
    def select_cc(event):
        try:
            tecnico = tecnico_combobox.get()
            conn = mysql.connector.connect(user="root", password="0000",
                                            host=importar_host(),
                                            database="RCC",
                                            port="3306")
            instruccion_uno = f"SELECT cc FROM tecnicos WHERE nombre = '{tecnico}'"
            instruccion_dos = f"SELECT telefono FROM tecnicos WHERE nombre = '{tecnico}'"
            cursor = conn.cursor()
            cursor.execute(instruccion_uno)
            cc = cursor.fetchall()
            cursor.execute(instruccion_dos)
            tlf = cursor.fetchall()
            conn.commit()
            conn.close()
            cc_tecnico_combobox.set("")
            tlf_tecnico_combobox.set("")
            cc_tecnico_combobox.config(values=cc[0])
            tlf_tecnico_combobox.config(values=tlf[0])
        except:
            messagebox.showerror(
                "Error", "El técnico que ingresaste no existe, valida la información ingresada")
        
    def registrar_pedido():
        fecha = fecha_entry.get()
        cliente = cliente_combobox.get()
        caso = caso_entry.get()
        oc = oc_combobox.get()
        sede = sede_combobox.get()
        gestor = gestor_combobox.get().upper()
        resumen_caso = resumen_entry.get().upper()
        insumo = insumo_entry.get().upper()
        cantidad = cantidad_entry.get()
        unidad_medida = unidad_combobox.get()
        valor_materiales = quitar_formato(valor_material_entry)
        valor_envio = quitar_formato(valor_envio_entry)
        proveedor = proveedor_combobox.get()
        direccion_cliente = direccion_entry.get().upper()
        ciudad_entrega = ciudad_entry.get().upper()
        tecnico = tecnico_combobox.get()
        cc = cc_tecnico_combobox.get()
        telefono = tlf_tecnico_combobox.get()
        comentarios = comentarios_entry.get().upper()

        if fecha and cliente and caso and oc and sede and gestor and resumen_caso and insumo and cantidad and unidad_medida and proveedor and direccion_cliente and ciudad_entrega and tecnico and cc and telefono and comentarios:

            tabla.insert("", tkinter.END,
                            values=(fecha, cliente, caso, oc, sede, gestor, resumen_caso, insumo, cantidad, unidad_medida, valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega,tecnico, cc, telefono, comentarios))
            tabla.pack()

            insumo_entry.delete(0, 'end')
            cantidad_entry.delete(0, 'end')
            unidad_combobox.set("")
            insumo_entry.focus_set()

        else:
            messagebox.showerror(title="Error de registro",
                                    message="Debes llenar los campos obligatorios.")

    def enviar_pedido():
        pedidos = tabla.get_children()
        for pedido in pedidos:
            fecha = tabla.item(pedido)['values'][0]
            cliente = tabla.item(pedido)['values'][1]
            caso = tabla.item(pedido)['values'][2]
            oc = tabla.item(pedido)['values'][3]
            sede = tabla.item(pedido)['values'][4]
            gestor = tabla.item(pedido)['values'][5]
            resumen = tabla.item(pedido)['values'][6]
            insumo = tabla.item(pedido)['values'][7]
            cantidad = tabla.item(pedido)['values'][8]
            unidad = tabla.item(pedido)['values'][9]
            valor_materiales = tabla.item(pedido)['values'][10]
            valor_envio = tabla.item(pedido)['values'][11]
            proveedor = tabla.item(pedido)['values'][12]
            direccion_oficina = tabla.item(pedido)['values'][13]
            ciudad_entrega = tabla.item(pedido)['values'][14]
            tecnico = tabla.item(pedido)['values'][15]
            cc = tabla.item(pedido)['values'][16]
            tlf = tabla.item(pedido)['values'][17]
            comentarios = tabla.item(pedido)['values'][18]

            conn = mysql.connector.connect(user="root", password="0000",
                                            host=importar_host(),
                                            database="RCC",
                                            port="3306")
            data_insert_query = f'''INSERT INTO registro_pedidos (fecha, cliente, caso, oc, sede , gestor_rcc,
                        resumen_caso, insumo, cantidad, unidad_medida, valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega,
                        tecnico, cc, tlf, comentarios) VALUES ('{fecha}','{cliente}', '{caso}','{oc}', '{sede}', '{gestor}', '{resumen}',
                        '{insumo}', {cantidad}, '{unidad}', {valor_materiales}, {valor_envio}, '{proveedor}', '{direccion_oficina}', '{ciudad_entrega}',
                        '{tecnico}','{cc}', '{tlf}', '{comentarios}')'''
            cursor = conn.cursor()
            cursor.execute(data_insert_query)
            conn.commit()
            conn.close()

        tabla.delete(*tabla.get_children())

        fecha_entry.delete(0, 'end')
        cliente_combobox.set("")
        caso_entry.delete(0, 'end')
        oc_combobox.set("")
        sede_combobox.set("")
        gestor_combobox.set("")
        resumen_entry.delete(0, 'end')
        insumo_entry.delete(0, 'end')
        cantidad_entry.delete(0, 'end')
        unidad_combobox.set("")
        valor_material_entry.delete(0, 'end')
        valor_envio_entry.delete(0, 'end')
        direccion_entry.delete(0, 'end')
        ciudad_entry.delete(0, 'end')
        tecnico_combobox.set("")
        cc_tecnico_combobox.set("")
        tlf_tecnico_combobox.set("")
        comentarios_entry.delete(0, 'end')
        proveedor_combobox.set("")
        fecha_entry.focus_set()

        messagebox.showinfo('Registro exitoso',
                            'El pedido de su caso ha sido enviado con éxito.')

    def eliminar_item():
        seleccion = tabla.focus()
        tabla.delete(seleccion)

    ventana = tkinter.Toplevel()
    ventana.title("Scrum Manager | Registro de pedidos")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 990
    alto_ventana = 660
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana+20)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco = tkinter.Frame(ventana)
    marco.config(bg="white")
    marco.pack(padx=5, pady=5)

    widget_label_frame = tkinter.LabelFrame(marco, text="Registra tu pedido")
    widget_label_frame.config(
        bg="white", foreground="black", font="Barlow 13 ")
    widget_label_frame.pack(padx=5, pady=5)

    fecha_label = tkinter.Label(
        widget_label_frame, text="Fecha de solicitud", font="Barlow 11 ", bg="white")
    fecha_label.grid(column=0, row=0)

    fecha_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    fecha_entry.grid(column=1, row=0)
    fecha_entry.bind("<Key>", solo_numeros)
    fecha_entry.bind("<KeyRelease>", lambda event: FormatoFecha("",event, fecha_entry))

    gestor_label = tkinter.Label(
        widget_label_frame, text="Gestor RCC", font="Barlow 11 ", bg="white")
    gestor_label.grid(column=0, row=1)

    gestor_combobox = ttk.Combobox(widget_label_frame, state="readonly", values=usuario_ingresado)
    gestor_combobox.grid(column=1, row=1)

    cliente_label = tkinter.Label(
        widget_label_frame, text="Cliente", bg="white", font="Barlow 11 ")
    cliente_label.grid(column=0, row=2)

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

    cliente_combobox = ttk.Combobox(widget_label_frame, state="readonly", values=lista_clientes)
    cliente_combobox.grid(column=1, row=2)

    caso_label = tkinter.Label(
        widget_label_frame, text="Caso", font="Barlow 11 ", bg="white")
    caso_label.grid(column=0, row=3)

    caso_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    caso_entry.grid(column=1, row=3)
    caso_entry.bind('<FocusOut>', select_datos_caso)

    oc_label = tkinter.Label(
        widget_label_frame, text="OC", bg="white", font="Barlow 11 ")
    oc_label.grid(column=0, row=4)

    oc_combobox = ttk.Combobox(widget_label_frame, state="readonly")
    oc_combobox.grid(column=1, row=4)

    sede_label = tkinter.Label(
        widget_label_frame, text="Sede", bg="white", font="Barlow 11 ")
    sede_label.grid(column=0, row=5)

    sede_combobox = ttk.Combobox(widget_label_frame, state="readonly")
    sede_combobox.grid(column=1, row=5)

    resumen_label = tkinter.Label(
        widget_label_frame, text="Resumen del caso", font="Barlow 11 ", bg="white")
    resumen_label.grid(column=2, row=0)

    resumen_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    resumen_entry.grid(column=3, row=0)

    insumo_label = tkinter.Label(
        widget_label_frame, text="Insumo", bg="white", font="Barlow 11 ")
    insumo_label.grid(column=2, row=1)

    insumo_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    insumo_entry.grid(column=3, row=1)

    cantidad_label = tkinter.Label(
        widget_label_frame, text="Cantidad", bg="white", font="Barlow 11 ")
    cantidad_label.grid(column=2, row=2)

    cantidad_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    cantidad_entry.grid(column=3, row=2)
    cantidad_entry.bind("<Key>", lambda event: solo_numeros(event))

    unidad_label = tkinter.Label(
        widget_label_frame, text="Unidad de medida", bg="white", font="Barlow 11 ")
    unidad_label.grid(column=2, row=3)

    unidad_combobox = ttk.Combobox(widget_label_frame, state="readonly", values=["UNIDAD", "KG", "GALON", "METRO", "CUÑETE"])
    unidad_combobox.grid(column=3, row=3)

    valor_material_label = tkinter.Label(
        widget_label_frame, text="Valor de materiales", font="Barlow 11 ", bg="white")
    valor_material_label.grid(column=2, row=4)

    valor_material_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    valor_material_entry.grid(column=3, row=4)
    valor_material_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event,valor_material_entry))
    valor_material_entry.bind("<Key>", lambda event: solo_numeros(event))
    valor_material_entry.bind("<FocusOut>", lambda event: formatear_entry(event, valor_material_entry))

    valor_envio_label = tkinter.Label(
        widget_label_frame, text="Valor de envío", font="Barlow 11 ", bg="white")
    valor_envio_label.grid(column=2, row=5)

    valor_envio_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    valor_envio_entry.grid(column=3, row=5)
    valor_envio_entry.bind("<FocusIn>", lambda event: quitar_puntos_entry(event, valor_envio_entry))
    valor_envio_entry.bind("<Key>", lambda event: solo_numeros(event))
    valor_envio_entry.bind("<FocusOut>", lambda event: formatear_entry(event, valor_envio_entry))

    direccion_label = tkinter.Label(
        widget_label_frame, text="Dirección de ofic. cliente", bg="white", font="Barlow 11 ")
    direccion_label.grid(column=4, row=0)

    direccion_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    direccion_entry.grid(column=5, row=0)

    ciudad_label = tkinter.Label(
        widget_label_frame, text="Ciudad de entrega", font="Barlow 11 ", bg="white")
    ciudad_label.grid(column=4, row=1)

    ciudad_entry = tkinter.Entry(widget_label_frame, font="Barlow 10")
    ciudad_entry.grid(column=5, row=1)

    proveedor_label = tkinter.Label(
        widget_label_frame, text="Proveedor", font="Barlow 11 ", bg="white")
    proveedor_label.grid(column=4, row=2)

    conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
    cursor = conn.cursor()
    instruccion = "SELECT DISTINCT razon_social FROM proveedores ORDER BY razon_social ASC"
    cursor.execute(instruccion)
    resultados_proveedor = cursor.fetchall()
    lista_tecnicos = []
    for proveedor in resultados_proveedor:
        lista_tecnicos.append(proveedor[0])

    proveedor_combobox = ttk.Combobox(widget_label_frame, state="readonly", values=lista_tecnicos)
    proveedor_combobox.grid(column=5, row=2)

    tecnico_label = tkinter.Label(
        widget_label_frame, text="Técnico que recibe", font="Barlow 11 ", bg="white")
    tecnico_label.grid(column=4, row=3)

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

    tecnico_combobox = ttk.Combobox(widget_label_frame, state="readonly", values=lista_tecnicos)
    tecnico_combobox.grid(column=5, row=3)
    tecnico_combobox.bind('<<ComboboxSelected>>', select_cc)

    cc_tecnico_label = tkinter.Label(
        widget_label_frame, text="Cédula de técnico", font="Barlow 11 ", bg="white")
    cc_tecnico_label.grid(column=4, row=4)

    cc_tecnico_combobox = ttk.Combobox(widget_label_frame, state="readonly")
    cc_tecnico_combobox.grid(column=5, row=4)

    tlf_tecnico_label = tkinter.Label(
        widget_label_frame, text="Tlf. técnico que recibe", bg="white", font="Barlow 11 ")
    tlf_tecnico_label.grid(column=4, row=5)

    tlf_tecnico_combobox = ttk.Combobox(widget_label_frame, state="readonly")
    tlf_tecnico_combobox.grid(column=5, row=5)

    comentarios_label = tkinter.Label(
        widget_label_frame, text="Comentarios", font="Barlow 11 ", bg="white")
    comentarios_label.grid(column=0, row=6)

    comentarios_entry = tkinter.Entry(widget_label_frame, font="Barlow 10", width=110)
    comentarios_entry.grid(column=1, row=6, columnspan=5)

    for widget in widget_label_frame.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    tabla = ttk.Treeview(marco, selectmode="browse")
    vertical_bar = ttk.Scrollbar(marco, orient="vertical")
    horizontal_bar = ttk.Scrollbar(marco, orient="horizontal")

    tabla.configure(yscrollcommand=vertical_bar.set)
    tabla.configure(xscrollcommand=horizontal_bar.set)
    vertical_bar.configure(command=tabla.yview)
    horizontal_bar.configure(command=tabla.xview)

    vertical_bar.pack(side="right", fill="y")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    tabla['columns'] = ("Fecha de solicitud", "Cliente", "Caso", "Orden de compra", "Sede", "Gestor",
                        "Resumen del caso", "Insumo","Cantidad", "Unidad", "Valor materiales", "Valor envio","Proveedor",
                        "Direccion cliente", "Ciudad entrega", "Tecnico que recibe", "Cedula tecnico", "Tlf tecnico que recibe", "Comentarios")

    tabla.column("#0", width=0, stretch=False)
    tabla.column("Fecha de solicitud", anchor="center", width=140)
    tabla.column("Cliente", anchor="center", width=140)
    tabla.column("Caso", anchor="center", width=140)
    tabla.column("Orden de compra", anchor="center", width=140)
    tabla.column("Sede", anchor="center", width=140)
    tabla.column("Gestor", anchor="center", width=140)
    tabla.column("Resumen del caso", anchor="center", width=140)
    tabla.column("Insumo", anchor="center", width=140)
    tabla.column("Cantidad", anchor="center", width=140)
    tabla.column("Unidad", anchor="center", width=140)
    tabla.column("Valor materiales", anchor="center", width=140)
    tabla.column("Valor envio", anchor="center", width=140)
    tabla.column("Proveedor", anchor="center", width=140)
    tabla.column("Direccion cliente", anchor="center", width=140)
    tabla.column("Ciudad entrega", anchor="center", width=140)
    tabla.column("Tecnico que recibe", anchor="center", width=140)
    tabla.column("Cedula tecnico", anchor="center", width=140)
    tabla.column("Tlf tecnico que recibe", anchor="center", width=140)
    tabla.column("Comentarios", anchor="center", width=140)

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("Fecha de solicitud",text="Fecha de solicitud", anchor="center")
    tabla.heading("Cliente", text="Cliente", anchor="center")
    tabla.heading("Caso", text="Caso", anchor="center")
    tabla.heading("Orden de compra", text="Orden de compra", anchor="center")
    tabla.heading("Sede", text="Sede", anchor="center")
    tabla.heading("Gestor", text="Gestor", anchor="center")
    tabla.heading("Resumen del caso", text="Resumen del caso", anchor="center")
    tabla.heading("Insumo", text="Insumo", anchor="center")
    tabla.heading("Cantidad", text="Cantidad", anchor="center")
    tabla.heading("Unidad", text="Unidad de medida", anchor="center")
    tabla.heading("Valor materiales",text="Valor de materiales", anchor="center")
    tabla.heading("Valor envio", text="Valor de envío", anchor="center")
    tabla.heading("Proveedor", text="Proveedor", anchor="center")
    tabla.heading("Direccion cliente",text="Dirección cliente", anchor="center")
    tabla.heading("Ciudad entrega", text="Ciudad de entrega", anchor="center")
    tabla.heading("Tecnico que recibe",text="Técnico que recibe", anchor="center")
    tabla.heading("Cedula tecnico", text="Cédula de técnico", anchor="center")
    tabla.heading("Tlf tecnico que recibe",text="Tlf técnico que recibe", anchor="center")
    tabla.heading("Comentarios", text="Comentarios", anchor="center")

    marco_btn = tkinter.Frame(ventana, bg="white")
    marco_btn.pack(padx=5)

    registrar_btn = tkinter.Button(marco_btn, text="Registrar",
                                    bd=0, relief="flat",
                                    font=("Barlow 15"),
                                    command=registrar_pedido,
                                    cursor="hand2",
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    width=39)
    registrar_btn.grid(column=0, row=0)
    registrar_btn.bind('<Enter>', lambda event: hover_on(event, registrar_btn))
    registrar_btn.bind('<Leave>', lambda event: hover_off(event, registrar_btn))

    enviar_btn = tkinter.Button(marco_btn, text="Enviar",
                                bd=0, relief="flat",
                                font=("Barlow 15"),
                                command=enviar_pedido,
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width=39)
    enviar_btn.grid(column=1, row=0)
    enviar_btn.bind('<Enter>', lambda event: hover_on(event, enviar_btn))
    enviar_btn.bind('<Leave>', lambda event: hover_off(event, enviar_btn))

    eliminar_btn = tkinter.Button(marco_btn, text="Eliminar",
                                bd=0, relief="flat",
                                font=("Barlow 15"),
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width=39,
                                command=eliminar_item)
    eliminar_btn.grid(column=0, row=1, columnspan=2)
    eliminar_btn.bind('<Enter>', lambda event: hover_on(event, eliminar_btn))
    eliminar_btn.bind('<Leave>', lambda event: hover_off(event, eliminar_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(pady=5, padx=5)

    fecha_entry.focus_set()

    ventana.mainloop()