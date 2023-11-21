import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from creacion_oc import abrir_creacion_oc
from registro_proveedor import abrir_registro_proveedor
from pagos_proveedor import abrir_pagos_proveedor
from funciones import *


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
                                      text="Crear OC", font="Barlow 11", compound="left", command=abrir_creacion_oc)
            crear_oc.place(x=30, y=30)
            reg_proveedor = tkinter.Button(marco_menu, image=reg_proveedor_img, cursor="hand2", bg="white", bd=0, activebackground="white",
                                           text="Reg. proveedor", font="Barlow 11", compound="left", command=abrir_registro_proveedor)
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
    pago_proveedor_img = tkinter.PhotoImage(file="./gestion/pagos_img.png")

    buscar_label = tkinter.Label(
        marco_buscador, text="Búsqueda por caso / gestor", font="Barlow 11 ", bg="white")
    buscador_entry = tkinter.Entry(marco_buscador, font="Barlow 11")

    def buscador_pendientes(event):
        ot = buscador_entry.get()
        gestor = buscador_entry.get().upper()
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        instruccion = f"""SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                    valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                    tecnico, cc, tlf, comentarios FROM registro_pedidos WHERE caso LIKE '{ot}%' or gestor_rcc like'{gestor}%'"""
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)

    def buscador_realizados(event):
        ot = buscador_entry.get()
        gestor = buscador_entry.get().upper()
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        instruccion = f"""SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                    valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                    tecnico, cc, tlf, comentarios FROM pedidos_realizados WHERE caso LIKE '{ot}%' or gestor_rcc like'{gestor}%'"""
        cursor = conn.cursor()
        cursor.execute(instruccion)
        busquedas = cursor.fetchall()
        conn.commit()
        conn.close()
        tabla.delete(*tabla.get_children())
        for busqueda in busquedas:
            tabla.insert('', 'end', values=busqueda)

    buscar_label = tkinter.Label(
        marco_buscador, text="Búsqueda por caso / gestor", font="Barlow 11 ", bg="white")
    buscador_entry = tkinter.Entry(marco_buscador, font="Barlow 11")

    buscar_label.pack(side="left", padx=5)
    buscador_entry.pack(fill="x", padx=5)
    buscador_entry.config(width=75)
    buscador_entry.bind('<Return>', buscador_pendientes)

    tabla = ttk.Treeview(marco, selectmode="browse", height=15)
    vertical_bar = ttk.Scrollbar(marco, orient="vertical")
    horizontal_bar = ttk.Scrollbar(marco, orient="horizontal")

    def ver_lista(event):
        seleccion = tabla.focus()

        # Verificar si se ha seleccionado una fila
        if seleccion:
            # Obtener los valores de la fila seleccionada
            valores = tabla.item(seleccion, 'values')

            # Obtener el valor de las columnas
            fecha = valores[0]
            cliente = valores[1]
            caso = valores[2]
            comercial = valores[5]
            oc = valores[3]
            proveedor = valores[12]
            ciudad = valores[14]
            resumen = valores[6]
            comentarios = valores[18]

            abrir_pagos_proveedor(fecha, cliente, caso, comercial, oc, proveedor, ciudad, resumen, comentarios)

    tabla.configure(yscrollcommand=vertical_bar.set)
    tabla.configure(xscrollcommand=horizontal_bar.set)
    vertical_bar.configure(command=tabla.yview)
    horizontal_bar.configure(command=tabla.xview)
    tabla.bind("<Double-1>", ver_lista)

    vertical_bar.pack(side="right", fill="y")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    tabla['columns'] = ("Fecha de solicitud", "Cliente", "Caso", "Orden de compra", "Sede", "Gestor",
                        "Resumen del caso", "Insumo", "Cantidad", "Unidad de medida","Valor materiales", "Valor envio", "Proveedor",
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
    tabla.column("Unidad de medida", anchor="center", width=140)
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
    tabla.heading("Unidad de medida", text="Unidad de medida", anchor="center")
    tabla.heading("Valor materiales",text="Valor de materiales", anchor="center")
    tabla.heading("Valor envio", text="Valor de envío", anchor="center")
    tabla.heading("Proveedor", text="Proveedor", anchor="center")
    tabla.heading("Direccion cliente",text="Dirección cliente", anchor="center")
    tabla.heading("Ciudad entrega", text="Ciudad de entrega", anchor="center")
    tabla.heading("Tecnico que recibe",text="Técnico que recibe", anchor="center")
    tabla.heading("Cedula tecnico", text="Cédula de técnico", anchor="center")
    tabla.heading("Tlf tecnico que recibe",text="Tlf técnico que recibe", anchor="center")
    tabla.heading("Comentarios", text="Comentarios", anchor="center")

    conn = mysql.connector.connect(user="root", password="0000",
                                   host=importar_host(),
                                   database="RCC",
                                   port="3306")
    instruccion = """SELECT  fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                    valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                    tecnico, cc, tlf, comentarios FROM registro_pedidos"""
    cursor = conn.cursor()
    cursor.execute(instruccion)
    registros = cursor.fetchall()
    for registro in registros:
        tabla.insert('', 'end', values=registro)
    tabla.pack()

    def eliminar_pedido():
        x = messagebox.askquestion("Eliminar pedido", "¿Deseas eliminar el pedido seleccionado?")
        if x == "yes":
            # Obtener la fila seleccionada en el Treeview
            seleccion = tabla.focus()

            # Verificar si se ha seleccionado una fila
            if seleccion:
                # Obtener los valores de la fila seleccionada
                valores = tabla.item(seleccion, 'values')

                # Obtener el valor de la tercera columna (índice 2) que contiene el caso
                fecha = valores[0]
                caso = valores[2]
                conn = mysql.connector.connect(user="root", password="0000",
                                               host=importar_host(),
                                               database="RCC",
                                               port="3306")
                cursor = conn.cursor()
                eliminar_pago = f"DELETE FROM registro_pedidos WHERE caso = '{caso}' and fecha = '{fecha}'"
                cursor.execute(eliminar_pago)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = """SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                        valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                        tecnico, cc, tlf, comentarios FROM registro_pedidos"""
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                messagebox.showinfo("Eliminación de pedidos",
                                    "El pedido ha sido eliminado")

    btn_eliminar = tkinter.Button(marco_btn, text="Eliminar",
                                  bd=0, relief="flat",
                                  font=("Barlow 17"),
                                  cursor="hand2",
                                  bg="#282e35",
                                  foreground="#00d2ff",
                                  activebackground="#282e35",
                                  activeforeground="#00d2ff",
                                  width=33,
                                  command=eliminar_pedido)
    btn_eliminar.grid(column=0, row=0)
    btn_eliminar.bind("<Enter>", lambda event: hover_on(event, btn_eliminar))
    btn_eliminar.bind("<Leave>", lambda event: hover_off(event, btn_eliminar))

    def cambiar_estado():
        x = messagebox.askquestion(
            title="Cambio de estado", message="¿Deseas cambiar el estado del pedido a realizado?")
        if x == 'yes':
            # Obtener la fila seleccionada en el Treeview
            seleccion = tabla.focus()

            # Verificar si se ha seleccionado una fila
            if seleccion:
                # Obtener los valores de la fila seleccionada
                valores = tabla.item(seleccion, 'values')

                # Obtener el valor de la primera columna (índice 0) que contiene el ID
                caso = valores[2]
                fecha = valores[0]
                conn = mysql.connector.connect(user='root', password='0000',
                                               host=importar_host(),
                                               database='RCC',
                                               port='3306')
                cursor = conn.cursor()
                transferencia_pedido = f'''INSERT INTO pedidos_realizados(fecha, cliente, caso, oc, sede,
                                                            gestor_rcc, resumen_caso, insumo, cantidad, unidad_medida, valor_materiales, valor_envio, proveedor, direccion_cliente, 
                                                            ciudad_entrega, tecnico, cc, tlf, comentarios) SELECT fecha, cliente, caso, oc, sede,
                                                            gestor_rcc, resumen_caso, insumo, cantidad, unidad_medida, valor_materiales, valor_envio, proveedor, direccion_cliente, 
                                                            ciudad_entrega, tecnico, cc, tlf, comentarios FROM registro_pedidos WHERE caso = "{caso}"'''
                cursor.execute(transferencia_pedido)
                eliminar_pago = f"DELETE FROM registro_pedidos WHERE caso = '{caso}' and fecha = '{fecha}'"
                cursor.execute(eliminar_pago)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = """SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                        valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                        tecnico, cc, tlf, comentarios FROM registro_pedidos"""
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                messagebox.showinfo("Envío de pedidos",
                                    "Pedido realizado con éxito.")

    btn_enviar = tkinter.Button(marco_btn, text="Realizado",
                                bd=0, relief="flat",
                                font=("Barlow 17"),
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width=33,
                                command=cambiar_estado)
    btn_enviar.grid(column=1, row=0)
    btn_enviar.bind("<Enter>", lambda event: hover_on(event, btn_enviar))
    btn_enviar.bind("<Leave>", lambda event: hover_off(event, btn_enviar))

    def mostrar_pendientes():
        tabla.delete(*tabla.get_children())
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conn.cursor()
        instruccion = '''SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                    valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                    tecnico, cc, tlf, comentarios FROM registro_pedidos'''
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        for dato in datos:
            tabla.insert("", "end", values=dato)
        conn.commit()
        conn.close()
        btn_eliminar.config(state="active")
        btn_enviar.config(state="active")
        buscador_entry.bind('<Return>', buscador_pendientes)

    pendientes_btn = tkinter.Button(marco_btn, text="Pedidos pendientes",
                                    bd=0, relief="flat",
                                    font=("Barlow 11 "),
                                    cursor="hand2",
                                    width=50,
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    command=mostrar_pendientes)
    pendientes_btn.grid(column=0, row=1)
    pendientes_btn.bind("<Enter>", lambda event: hover_on(event, pendientes_btn))
    pendientes_btn.bind("<Leave>", lambda event: hover_off(event, pendientes_btn))

    def mostrar_realizados():
        tabla.delete(*tabla.get_children())
        conn = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
        cursor = conn.cursor()
        instruccion = '''SELECT fecha, cliente, caso, oc, sede, gestor_rcc,resumen_caso, insumo, cantidad, unidad_medida,
                    valor_materiales, valor_envio, proveedor, direccion_cliente, ciudad_entrega, 
                    tecnico, cc, tlf, comentarios FROM pedidos_realizados'''
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        for dato in datos:
            tabla.insert("", "end", values=dato)
        conn.commit()
        conn.close()
        btn_eliminar.config(state="disabled")
        btn_enviar.config(state="disabled")
        buscador_entry.bind('<Return>', buscador_realizados)

    realizados_btn = tkinter.Button(marco_btn, text="Pedidos realizados",
                                    bd=0, relief="flat",
                                    font=("Barlow 11 "),
                                    cursor="hand2",
                                    width=50,
                                    bg="#282e35",
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    command=mostrar_realizados)
    realizados_btn.grid(column=1, row=1)
    realizados_btn.bind("<Enter>", lambda event: hover_on(event, realizados_btn))
    realizados_btn.bind("<Leave>", lambda event: hover_off(event, realizados_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    ventana.mainloop()

    