import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import mysql.connector
from reportlab.pdfgen import canvas
from time import strftime
from funciones import *

def abrir_creacion_oc():
    conn = mysql.connector.connect(user="root", password="0000",
                                host = importar_host(),
                                database="RCC",
                                port="3306")
    cursor = conn.cursor()
    instruccion ="INSERT INTO oc_compras (id) VALUES (NULL)"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()
    pdf_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF", "*.pdf")])
    if pdf_file != '':
        doc = canvas.Canvas(pdf_file)

        def registrar_ocMysql():
            oc = entry_oc.get()
            fecha = entry_fecha.get()
            proveedor = combobox_proveedor.get()
            nit = combobox_nit.get()
            ciudad = combobox_ciudad_proveedor.get()
            envio = entry_envio.get()
            subtotal_oc = entry_subtotal_oc.get()

            if fecha and proveedor and nit and ciudad and envio and subtotal_oc:
                conn = mysql.connector.connect(user="root", password="0000",
                                    host = importar_host(),
                                    database="RCC",
                                    port="3306")
                cursor = conn.cursor()
                instruccion =f"""UPDATE oc_compras SET fecha = '{fecha}', proveedor = '{proveedor}', nit = '{nit}',
                                ciudad = '{ciudad}', envio = {envio}, subtotal = {subtotal_oc} WHERE id = {oc}"""
                cursor.execute(instruccion)
                conn.commit()
                conn.close()
                

        def crear_formato():
            doc.line(5,835,5,718)

            doc.drawImage("./RCC LOGO.png", 8, 725, width=450, height=105)

            # doc.line(140,835,140,718)

            doc.setFont("Times-Roman", 30)

            # doc.drawString(148, 790, "FORMATO DE ORDEN")
            # doc.drawString(208, 750, "DE COMPRA")

            doc.line(460,835, 460,718)

            doc.line(590,835, 590,718)

            doc.line(5, 835, 590, 835)

            doc.line(460,815,590,815)
            doc.line(460,790,590,790)
            doc.line(460,765,590,765)

            doc.line(5, 718, 590, 718)

            doc.setFont("Times-Roman", 15)

            doc.drawString(490, 820, "F-COM-005")
            doc.drawString(520, 795, "1")
            doc.drawString(490, 770, "16/06/2023")
            doc.drawString(505, 735, "1 DE 1")

            doc.line(5, 700, 590, 700)

            doc.setFont("Times-Roman", 20)

            doc.drawString(10, 675, "RCC INGENIERIA Y PROYECTOS SAS")
            doc.drawString(10, 650, "NIT: 901133593-5")

            doc.setFont("Times-Roman", 15)

            doc.drawString(10, 630, "Dirección:")
            doc.drawString(10, 610, "Ciudad:")
            doc.drawString(10, 590, "Teléfono:")

            doc.drawString(180, 630, "CRA. 8 F BIS #164A-36")
            doc.drawString(220, 610, "BOGOTA")
            doc.drawString(212, 590, "3142707164")

            doc.setFont("Times-Roman", 20)
            doc.setFillColor("Steelblue")

            doc.drawString(390, 650,"ORDEN DE COMPRA")

            doc.setFont("Times-Roman", 20)
            doc.setFillColor("Black")

            doc.setFont("Times-Roman", 15)

            doc.drawString(420, 630, "No." )
            doc.drawString(420, 610, "Fecha" )

            doc.line(5, 700, 5, 180)

            doc.line(590, 700, 590, 180)

            doc.line(5, 180, 590, 180)

            doc.setFillColor("Steelblue")
            doc.rect(5, 550, 585, 35, fill=True)

            doc.setFont("Times-Roman", 30)
            doc.setFillColor("White")

            doc.drawString(10, 560, "Proveedor")

            doc.drawString(325, 560, "Dirección de entrega")

            doc.setFont("Times-Roman", 15)
            doc.setFillColor("black")

            doc.drawString(10, 535, "Nombre")
            doc.drawString(10, 510, "NIT/CC")
            doc.drawString(10, 485, "Dirección")
            doc.drawString(10, 460, "Ciudad")
            doc.drawString(10, 435, "Teléfono")

            doc.line(320, 585, 320, 410)

            doc.drawString(325, 535, "Nombre")
            doc.drawString(325, 510, "NIT/CC")
            doc.drawString(325, 485, "Dirección")
            doc.drawString(325, 460, "Ciudad")
            doc.drawString(325, 435, "Teléfono")

            doc.setFillColor("Steelblue")
            doc.rect(5, 400, 585, 30, fill=True)

            doc.setFont("Times-Roman", 15)
            doc.setFillColor("White")

            doc.drawString(46, 410, "Código")

            doc.drawString(185, 410, "Descripción")

            doc.drawString(280, 410, "Cant.")

            doc.drawString(385, 410, "Precio unitario")

            doc.drawString(505, 410, "TOTALES")

            doc.setFillColor("Black")

            doc.drawString(5, 160, "Instrucciones")

            doc.line(5, 150, 320, 150)
            doc.line(5, 80, 320, 80)
            doc.line(320, 150, 320, 80)
            doc.line(5, 150, 5, 80)
            
            doc.line(380, 150, 590, 150)
            doc.line(380, 80, 590, 80)
            doc.line(380, 150, 380, 80)
            doc.line(480, 150, 480, 80)
            doc.line(590, 150, 590, 80)
            doc.line(380, 131, 590, 131)
            doc.line(380, 115, 590, 115)
            doc.line(380, 98, 590, 98)

            doc.drawString(385, 135, "Sub-total")
            doc.drawString(385, 118, "IVA")
            doc.drawString(385, 101, "Envío")
            doc.drawString(385, 84, "Total")

            doc.drawString(5, 40, "Autorizado")
            doc.drawString(5, 25, "por")

            doc.line(80, 55, 320, 55)
            doc.line(80, 55, 80, 20)
            doc.line(320, 55, 320, 20)
            doc.line(80, 20, 320, 20)

            doc.drawString(105, 33, "MOISES ZABALETA CRUZ")

            doc.setFont("Times-Roman", 9)

        def fill_oc():
            try:
                registrar_ocMysql()
                crear_formato()

                doc.setFont("Times-Roman", 12)

                fecha = entry_fecha.get()
                oc = entry_oc.get()

                doc.drawString(500,630, oc)
                doc.drawString(475,610, fecha)

                nombre_proveedor = combobox_proveedor.get()
                nit_proveedor = combobox_nit.get()
                direccion_proveedor = combobox_direccion_proveedor.get().upper()
                ciudad_proveedor = combobox_ciudad_proveedor.get().upper()
                telefono_proveedor = combobox_telefono_proveedor.get()
                nombre_destinatario = entry_destinatario.get().upper()
                nit_destinatario = entry_nit_destinatario.get()
                direccion_entrega = entry_direccion_entrega.get().upper()
                ciudad_destinatario = entry_ciudad_destinatario.get().upper()
                telefono_destinatario = entry_telefono_destinatario.get()

                subtotal_oc = int(entry_subtotal_oc.get())
                base_iva = 0.19
                iva = subtotal_oc * base_iva
                iva = int(iva)
                envio = int(entry_envio.get())
                total_oc = subtotal_oc + iva + envio

                #ESCRIBIR MONTOS AL FINAL DEL PDF

                doc.drawString(485, 135, str(subtotal_oc))
                doc.drawString(485, 118, str(iva))
                doc.drawString(485, 101, str(envio))
                doc.drawString(485, 84, str(total_oc))

                #ESCRIBIR INFORMACION DEL PROVEEDOR EN EL PDF

                doc.drawString(75, 535, nombre_proveedor)
                doc.drawString(75, 511, nit_proveedor)
                doc.drawString(75, 485, direccion_proveedor)
                doc.drawString(75, 460, ciudad_proveedor)
                doc.drawString(75, 435, telefono_proveedor)

                #ESCRIBIR INFORMACION DEL DESTINATARIO EN EL PDF

                doc.drawString(390, 535, nombre_destinatario)
                doc.drawString(390, 511, nit_destinatario)
                doc.drawString(390, 485, direccion_entrega)
                doc.drawString(390, 460, ciudad_destinatario)
                doc.drawString(390, 435, telefono_destinatario)


                doc.setFont("Times-Roman", 9)
                
                registros = []

                for item in tabla.get_children():
                    valores = tabla.item(item, "values")
                    registros.append(valores)

                # Definir un límite de página (por ejemplo, 170)
                page_limit = 170
                current_height = 390  # Altura inicial (también puedes cambiarla según tus necesidades)
                current_width = 50
                for fila in registros:
                    # Si la altura actual es menor que el límite de la página, crea una nueva página
                    if current_height <= page_limit:
                        doc.showPage()  # Crea una nueva página
                        crear_formato()
                        doc.setFont("Times-Roman", 12)

                        fecha = entry_fecha.get()
                        oc = entry_oc.get()

                        doc.drawString(500,630, oc)
                        doc.drawString(475,610, fecha)

                        nombre_proveedor = combobox_proveedor.get()
                        nit_proveedor = combobox_nit.get()
                        direccion_proveedor = combobox_direccion_proveedor.get()
                        ciudad_proveedor = combobox_ciudad_proveedor.get()
                        telefono_proveedor = combobox_telefono_proveedor.get()
                        nombre_destinatario = entry_destinatario.get().upper()
                        nit_destinatario = entry_nit_destinatario.get()
                        direccion_entrega = entry_direccion_entrega.get().upper()
                        ciudad_destinatario = entry_ciudad_destinatario.get().upper()
                        telefono_destinatario = entry_telefono_destinatario.get()

                        #ESCRIBIR INFORMACION DEL PROVEEDOR EN EL PDF

                        doc.drawString(75, 535, nombre_proveedor)
                        doc.drawString(75, 511, nit_proveedor)
                        doc.drawString(75, 485, direccion_proveedor)
                        doc.drawString(75, 460, ciudad_proveedor)
                        doc.drawString(75, 435, telefono_proveedor)

                        #ESCRIBIR MONTOS AL FINAL DEL PDF

                        doc.drawString(485, 135, str(subtotal_oc))
                        doc.drawString(485, 118, str(iva))
                        doc.drawString(485, 101, str(envio))
                        doc.drawString(485, 84, str(total_oc))

                        #ESCRIBIR INFORMACION DEL DESTINATARIO EN EL PDF

                        doc.drawString(390, 535, nombre_destinatario)
                        doc.drawString(390, 511, nit_destinatario)
                        doc.drawString(390, 485, direccion_entrega)
                        doc.drawString(390, 460, ciudad_destinatario)
                        doc.drawString(390, 435, telefono_destinatario)


                        doc.setFont("Times-Roman", 9)
                        current_height = 390  # Reinicia la altura
                    for item in fila:
                        doc.drawString(current_width, current_height, str(item))
                        current_width += 120
                    # Ajustar la altura para el siguiente dato. '20' es la altura de la línea. Puedes ajustarla según tus necesidades.
                    current_height -= 20
                    current_width = 50

                doc.save()
                
                messagebox.showinfo("Creación exitosa", "Su orden de compra ha sido creada con éxito.")

                ventana.destroy()
            except Exception as ep:
                messagebox.showerror('',ep)
            
        def agg_item():
            precio_unitario_actual = entry_preciou.get()
            nuevo_precio_unitario = precio_unitario_actual.replace(".","")
            nuevo_precio_unitario = int(nuevo_precio_unitario)
            total_actual = valor_totales.get()
            nuevo_total = total_actual.replace(".","")
            nuevo_total = int(nuevo_total)
            codigo = entry_codigo.get()
            descripcion = entry_descripcion.get().upper()
            cantidad = entry_cantidad.get()

            total_oc = int(entry_subtotal_oc.get())
            nuevo_total_oc = total_oc + nuevo_total
            entry_subtotal_oc.delete(0,'end')
            entry_subtotal_oc.insert(0,nuevo_total_oc)
            entry_codigo.focus_set()
            
            

            if codigo and descripcion and cantidad and nuevo_precio_unitario:

                entry_codigo.delete(0,'end')
                entry_descripcion.delete(0,'end')
                entry_cantidad.delete(0,'end')
                entry_preciou.delete(0,'end')
                valor_totales.delete(0,'end')

                tabla.insert("",'end',values=(codigo, descripcion, cantidad, nuevo_precio_unitario, nuevo_total))
                tabla.pack()

        def datos_proveedor(event):
            proveedor = combobox_proveedor.get()
            conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
            cursor = conn.cursor()
            instruccion_nit = f"SELECT nit FROM proveedores WHERE razon_social = '{proveedor}'"
            instruccion_direccion = f"SELECT direccion FROM proveedores WHERE razon_social = '{proveedor}'"
            instruccion_ciudad = f"SELECT ciudad FROM proveedores WHERE razon_social = '{proveedor}'"
            instruccion_telefono = f"SELECT telefono FROM proveedores WHERE razon_social = '{proveedor}'"
            cursor.execute(instruccion_nit)
            nit = cursor.fetchone()
            cursor.execute(instruccion_direccion)
            direccion = cursor.fetchone()
            cursor.execute(instruccion_ciudad)
            ciudad = cursor.fetchone()
            cursor.execute(instruccion_telefono)
            telefono = cursor.fetchone()
            combobox_nit.set("")
            combobox_nit.config(values=nit)
            combobox_direccion_proveedor.set("")
            combobox_direccion_proveedor.config(values=direccion)
            combobox_ciudad_proveedor.set("")
            combobox_ciudad_proveedor.config(values=ciudad)
            combobox_telefono_proveedor.set("")
            combobox_telefono_proveedor.config(values=telefono)
        
        def permitir_21(event):
            valor = entry_descripcion.get()
            if len(valor) > 21:
                entry_descripcion.delete(21, 'end')
                messagebox.showerror("Error", "Este campo solo admite 21 caracteres")

        def calcular_total():
            try:
                precio_unitario_actual = entry_preciou.get()
                nuevo_precio_unitario =precio_unitario_actual.replace(".","")
                nuevo_precio_unitario = int(nuevo_precio_unitario)
                cantidad = int(entry_cantidad.get())
                resultado = cantidad * nuevo_precio_unitario
                resultado = str(resultado)
                resultado_formateado = ""
                contador = 0
                for numero in resultado[::-1]:
                    if contador == 3:
                        resultado_formateado += "."
                        contador= 0
                    resultado_formateado += numero
                    contador += 1
                resultado_final = resultado_formateado[::-1]
                valor_totales.delete(0, 'end')
                valor_totales.insert(0,resultado_final)
            except:
                messagebox.showerror("Error", "Campos Cantidad y Precio unitario vacíos.")

        def formatear_precio(event):
            precio = str(entry_preciou.get())
            contador = 0
            precio_formateado = ""
            for numero in precio[::-1]:
                if contador == 3:
                    precio_formateado += "."
                    contador = 0
                precio_formateado += numero
                contador += 1
            precio_unitario = precio_formateado[::-1]
            entry_preciou.delete(0, 'end')
            entry_preciou.insert(0, precio_unitario)
            calcular_total()
        
        def descartar_oc():
            oc = entry_oc.get()
            x = messagebox.askquestion("Cerrar ventana", "¿Deseas descartar la creación de la OC?")
            if x == 'yes':
                conn = mysql.connector.connect(user="root", password="0000",
                                    host = importar_host(),
                                    database="RCC",
                                    port="3306")
                cursor = conn.cursor()
                cursor.execute(f"DELETE FROM oc_compras WHERE id ={oc}")
                instruccion = "SELECT id FROM oc_compras ORDER BY id DESC LIMIT 1;"
                cursor.execute(instruccion)
                ultimo_registro = cursor.fetchone()
                if ultimo_registro == None:
                    nuevo_registro = 1
                else:
                    nuevo_registro = (ultimo_registro[0] + 1)
                instruccion_reset = f"ALTER TABLE oc_compras AUTO_INCREMENT = {nuevo_registro}"
                cursor.execute(instruccion_reset)
                conn.commit()
                conn.close()
                ventana.destroy()

        ventana = tkinter.Toplevel()
        ventana.title("Scrum Manager | Creación de OC")
        ancho_pantalla = ventana.winfo_screenwidth()
        alto_pantalla = ventana.winfo_screenheight()
        ancho_ventana = 970
        alto_ventana = 700
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - alto_ventana) // 2
        ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        ventana.config(bg="white")
        ventana.iconbitmap("./icon.ico")

        marco_proveedor = tkinter.Frame(ventana, bg="white")
        marco_proveedor.pack()

        proveedor_label_frame = tkinter.LabelFrame(marco_proveedor, text="Datos del proveedor / Datos de entrega", font="Barlow 15", bg="white", padx=5, pady=5)
        proveedor_label_frame.pack()

        label_fecha = tkinter.Label(proveedor_label_frame, text="Fecha", bg="white", font="Barlow 11 ")
        label_fecha.grid(column=0, row=0)

        entry_fecha = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_fecha.grid(column=1, row=0)
        entry_fecha.bind("<KeyRelease>",lambda event: FormatoFecha("",event,entry_fecha))
        entry_fecha.bind("<Key>", solo_numeros)

        label_proveedor = tkinter.Label(proveedor_label_frame, text="Nombre de proveedor", bg="white", font="Barlow 11 ")
        label_proveedor.grid(column=0, row=1)

        conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database="RCC",
                                    port="3306")
        cursor = conn.cursor()
        instruccion = f"SELECT DISTINCT razon_social FROM proveedores"
        cursor.execute(instruccion)
        datos = cursor.fetchall()
        proveedores_lista = []
        for dato in datos:
            proveedores_lista.append(dato[0])

        combobox_proveedor = ttk.Combobox(proveedor_label_frame, state="readonly", values=proveedores_lista)
        combobox_proveedor.grid(column=1, row=1)
        combobox_proveedor.bind("<<ComboboxSelected>>", datos_proveedor)

        label_nit = tkinter.Label(proveedor_label_frame, text="NIT/CC", bg="white", font="Barlow 11 ")
        label_nit.grid(column=0, row=2)

        combobox_nit = ttk.Combobox(proveedor_label_frame, state="readonly")
        combobox_nit.grid(column=1, row=2)

        label_direccion_proveedor = tkinter.Label(proveedor_label_frame, text="Dirección", bg="white", font="Barlow 11 ")
        label_direccion_proveedor.grid(column=0, row=3)

        combobox_direccion_proveedor = ttk.Combobox(proveedor_label_frame, state="readonly")
        combobox_direccion_proveedor.grid(column=1, row=3)

        label_ciudad_proveedor = tkinter.Label(proveedor_label_frame, text="Ciudad", font="Barlow 11 ", bg="white")
        label_ciudad_proveedor.grid(column=2, row=0)

        combobox_ciudad_proveedor = ttk.Combobox(proveedor_label_frame, state="readonly")
        combobox_ciudad_proveedor.grid(column=3, row=0)

        label_telefono_proveedor = tkinter.Label(proveedor_label_frame, text="Teléfono", font="Barlow 11 ", bg="white")
        label_telefono_proveedor.grid(column=2, row=1)

        combobox_telefono_proveedor = ttk.Combobox(proveedor_label_frame, state="readonly")
        combobox_telefono_proveedor.grid(column=3, row=1)

        label_oc = tkinter.Label(proveedor_label_frame, text="OC Nro", font="Barlow 11 ", bg="white")
        label_oc.grid(column=2, row=2)

        conn = mysql.connector.connect(user="root", password="0000",
                                    host=importar_host(),
                                    database = "RCC",
                                    port="3306")
        cursor = conn.cursor()
        instruccion = "SELECT id FROM oc_compras ORDER BY id DESC LIMIT 1"
        cursor.execute(instruccion)
        oc_nro = cursor.fetchone()
        conn.commit()
        conn.close()

        def block_oc(event):
            if event.keysym == 'Tab':
                pass
            else:
                return "break"

        entry_oc= tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_oc.grid(column=3, row=2)
        entry_oc.delete(0,'end')
        entry_oc.insert(0, oc_nro)
        entry_oc.bind("<Key>", block_oc)

        label_destinatario = tkinter.Label(proveedor_label_frame, text="Nombre destinatario", font="Barlow 11 ", bg="white")
        label_destinatario.grid(column=2, row=3)

        entry_destinatario = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_destinatario.grid(column=3, row=3)

        label_nit_destinatario = tkinter.Label(proveedor_label_frame, text="NIT/CC", bg="white", font="Barlow 11 ")
        label_nit_destinatario.grid(column=4, row=0)

        entry_nit_destinatario = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_nit_destinatario.grid(column=5, row=0)

        label_direccion_entrega = tkinter.Label(proveedor_label_frame, text="Dirección de entrega", font="Barlow 11 ", bg="white")
        label_direccion_entrega.grid(column=4, row=1)

        entry_direccion_entrega = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_direccion_entrega.grid(column=5, row=1)

        label_ciudad_destino = tkinter.Label(proveedor_label_frame, text="Ciudad destino", font="Barlow 11 ", bg="white")
        label_ciudad_destino.grid(column=4, row=2)

        entry_ciudad_destinatario = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_ciudad_destinatario.grid(column=5, row=2)

        label_telefono_destinatario = tkinter.Label(proveedor_label_frame, text="Teléfono destinatario", font="Barlow 11 ", bg="white")
        label_telefono_destinatario.grid(column=4, row=3)

        entry_telefono_destinatario = tkinter.Entry(proveedor_label_frame, font="Barlow 10")
        entry_telefono_destinatario.grid(column=5, row=3)


        for widget in proveedor_label_frame.winfo_children():
            widget.grid_configure(padx=5, pady=5)

        marco_items = tkinter.Frame(ventana, bg="white")
        marco_items.pack()

        items_label_frame = tkinter.LabelFrame(marco_items, text="Información de pedido", font="Barlow 15", bg="white")
        items_label_frame.pack()

        label_codigo = tkinter.Label(items_label_frame, text="Código", bg="white", font="Barlow 11")
        label_codigo.grid(column=0, row=0)

        entry_codigo = tkinter.Entry(items_label_frame, font="Barlow 10")
        entry_codigo.grid(column=1, row=0)

        label_descripcion = tkinter.Label(items_label_frame, text="Descripción",font="Barlow 11", bg="white")
        label_descripcion.grid(column=2, row=0)

        entry_descripcion = tkinter.Entry(items_label_frame, font="Barlow 10")
        entry_descripcion.grid(column=3, row=0)
        entry_descripcion.bind("<KeyRelease>", permitir_21)

        label_envio = tkinter.Label(items_label_frame, text="Envío", font="Barlow 11 ", bg="white")
        label_envio.grid(column=0, row=1)

        entry_envio = tkinter.Entry(items_label_frame, font="Barlow 10")
        entry_envio.grid(column=1, row=1)

        label_cantidad = tkinter.Label(items_label_frame, text="Cantidad", font="Barlow 11 ", bg="white")
        label_cantidad.grid(column=2, row=1)

        entry_cantidad = tkinter.Entry(items_label_frame, font="Barlow 10")
        entry_cantidad.grid(column=3, row=1)

        label_preciou = tkinter.Label(items_label_frame, text="Precio unitario", bg="white", font="Barlow 11 ")
        label_preciou.grid(column=0, row=2)

        entry_preciou = tkinter.Entry(items_label_frame, font="Barlow 10")
        entry_preciou.grid(column=1, row=2)
        entry_preciou.bind('<FocusOut>', formatear_precio)

        label_totales = tkinter.Label(items_label_frame, font="Barlow 11 ", bg="white", text="Total")
        label_totales.grid(column=2, row=2)

        valor_totales = tkinter.Entry(items_label_frame, font="Barlow 10")
        valor_totales.grid(column=3, row=2)
        valor_totales.bind("<Key>", lambda e: "break")

        for widget in items_label_frame.winfo_children():
            widget.grid_configure(padx=19, pady=5)

        marco_tabla = tkinter.Frame(ventana, padx= 5, pady=5, bg="white")
        marco_tabla.pack()

        tabla = ttk.Treeview(marco_tabla, selectmode="browse")
        vertical_bar = ttk.Scrollbar(marco_tabla, orient="vertical")

        tabla.config(yscrollcommand=vertical_bar.set)
        vertical_bar.config(command=tabla.yview)

        vertical_bar.pack(side="right", fill="y")
        tabla.pack()

        tabla["columns"] = ("Codigo", "Descripcion", "Cantidad", "Precio unitario", "Total")

        tabla.column("#0", width=0, stretch=False)
        tabla.column("Codigo", anchor="center" , width=150)
        tabla.column("Descripcion", anchor="center" , width=250)
        tabla.column("Cantidad", anchor="center" , width=150)
        tabla.column("Precio unitario", anchor="center" , width=150)
        tabla.column("Total", anchor="center" , width=150)

        tabla.heading("Codigo", text="Código", anchor="center")
        tabla.heading("Descripcion", text="Descripción", anchor="center")
        tabla.heading("Cantidad", text="Cantidad", anchor="center")
        tabla.heading("Precio unitario", text="Precio unitario", anchor="center")
        tabla.heading("Total", text="Total", anchor="center")

        marco_subtotal_oc = tkinter.Frame(ventana, bg="white")
        marco_subtotal_oc.pack(padx=10 , pady=10)

        label_subtotal_oc = tkinter.Label(marco_subtotal_oc, text="Subtotal OC", bg="white", font="Barlow 20 ")
        label_subtotal_oc.pack(side="left")

        entry_subtotal_oc = tkinter.Entry(marco_subtotal_oc, font="Barlow 20")
        entry_subtotal_oc.pack()
        entry_subtotal_oc.insert(0, 0)
        entry_subtotal_oc.bind("<Key>", lambda e: "break")

        for widget in marco_subtotal_oc.winfo_children():
            widget.pack_configure(padx=10)

        marco_btn = tkinter.Frame(ventana, bg="white")
        marco_btn.pack(padx=10 , pady=5)

        agg_item_btn = tkinter.Button(marco_btn, text="Agregar Item",
                                bd=0, relief="flat",
                                font="Barlow 15 bold",
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width= 32,
                                command=agg_item)
        agg_item_btn.pack(side="left")
        agg_item_btn.bind("<Enter>", lambda event: hover_on(event, agg_item_btn))
        agg_item_btn.bind("<Leave>", lambda event: hover_off(event, agg_item_btn))

        crear_oc_btn = tkinter.Button(marco_btn, text="Crear OC",
                                bd=0, relief="flat",
                                font="Barlow 15 bold",
                                cursor="hand2",
                                bg="#282e35",
                                foreground="#00d2ff",
                                activebackground="#282e35",
                                activeforeground="#00d2ff",
                                width= 32,
                                command=fill_oc)
        crear_oc_btn.pack()
        crear_oc_btn.bind("<Enter>", lambda event: hover_on(event, crear_oc_btn))
        crear_oc_btn.bind("<Leave>", lambda event: hover_off(event, crear_oc_btn))

        for btn in marco_btn.winfo_children():
            btn.pack_configure(padx=5, pady=5)

        ventana.protocol("WM_DELETE_WINDOW", descartar_oc)


        ventana.mainloop()
