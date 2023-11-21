import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from funciones import *
from tkinter import PhotoImage, Label

def abrir_registro_proveedor():
    def registrar_proveedor():
        nombre = razon_social_entry.get().upper()
        nit_cc = nit_entry.get()
        cuenta = cuenta_entry.get().upper()
        banco = banco_entry.get().upper()
        telefono = telefono_entry.get()
        tipo_cuenta = tipo_cuenta_combobox.get()
        direccion = direccion_entry.get().upper()
        ciudad = ciudad_entry.get().upper()

        if nombre and nit_cc and cuenta and banco and telefono and tipo_cuenta:

            conn = mysql.connector.connect(user='root', password='0000',
                                           host=importar_host(),
                                           database='RCC',
                                           port='3306')

            data_insert_query = f'''INSERT INTO proveedores (razon_social, nit, direccion, ciudad, telefono, banco, cuenta, tipo_cuenta) VALUES 
                                    ('{nombre}', {nit_cc},'{direccion}', '{ciudad}', '{telefono}', '{banco}', '{cuenta}', '{tipo_cuenta}')'''
            cursor = conn.cursor()
            cursor.execute(data_insert_query)
            cursor.execute("SELECT * FROM proveedores")
            tabla.delete(*tabla.get_children())
            datos = cursor.fetchall()
            for dato in datos:
                tabla.insert("", "end", values=dato)
                tabla.pack()
            conn.commit()
            conn.close()
            razon_social_entry.delete(0, 'end')
            nit_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            direccion_entry.delete(0, 'end')
            ciudad_entry.delete(0, 'end')
            razon_social_entry.focus_set()

            messagebox.showinfo(title="Registro realizado",
                                message="El registro fue realizado con éxito.")
        else:
            messagebox.showerror(title="Error de registro",
                                 message="Debes llenar los campos obligatorios.")

    def limpiar_widgets(event):
        if event.keysym == 'Escape':
            razon_social_entry.delete(0, 'end')
            nit_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            direccion_entry.delete(0, 'end')
            ciudad_entry.delete(0, 'end')
            actualizar_btn.config(state="disabled")
            registro_btn.config(state="normal")
            

    def actualizar_datos():
        elementos = tabla.item(tabla.focus())
        id = elementos["values"][0]
        nombre = razon_social_entry.get().upper()
        nit_cc = nit_entry.get()
        cuenta = cuenta_entry.get().upper()
        banco = banco_entry.get().upper()
        telefono = telefono_entry.get()
        tipo_cuenta = tipo_cuenta_combobox.get()
        direccion = direccion_entry.get().upper()
        ciudad = ciudad_entry.get().upper()

        if nombre and nit_cc and cuenta and banco and telefono and tipo_cuenta:

            tabla.delete(*tabla.get_children())

            conn = mysql.connector.connect(user='root', password='0000',
                                           host=importar_host(),
                                           database='RCC',
                                           port='3306')
            cursor = conn.cursor()
            query = f'''UPDATE proveedores SET razon_social = %s, nit = %s, direccion = %s, ciudad = %s, telefono = %s, banco = %s, cuenta = %s, tipo_cuenta = %s WHERE id = {id}'''
            info = (nombre, nit_cc, direccion, ciudad,
                    telefono, banco, cuenta, tipo_cuenta)
            cursor.execute(query, info)
            cursor.execute("SELECT * FROM proveedores")
            tabla.delete(*tabla.get_children())
            datos = cursor.fetchall()
            for dato in datos:
                tabla.insert("", "end", values=dato)
                tabla.pack()
            conn.commit()
            conn.close()
            razon_social_entry.delete(0, 'end')
            nit_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            direccion_entry.delete(0, 'end')
            ciudad_entry.delete(0, 'end')
            razon_social_entry.focus_set()

            messagebox.showinfo(title="Proceso exitoso",
                                message="La actualización de datos fue realizada con éxito.")
        else:
            messagebox.showerror(title="Error",
                                 message="Estás eliminando un dato obligatorio.")

    def seleccionar_fila(event):
        try:
            elementos = tabla.item(tabla.focus())
            if elementos:
                actualizar_btn.config(state="normal")
                registro_btn.config(state="disabled")
                razon_social_entry.delete(0, 'end')
                nit_entry.delete(0, 'end')
                cuenta_entry.delete(0, 'end')
                banco_entry.delete(0, 'end')
                telefono_entry.delete(0, 'end')
                tipo_cuenta_combobox.set("")
                direccion_entry.delete(0, 'end')
                ciudad_entry.delete(0, 'end')

                razon_social_entry.insert(0, elementos["values"][1])
                nit_entry.insert(0, elementos["values"][2])
                direccion_entry.insert(0, elementos["values"][3])
                ciudad_entry.insert(0, elementos["values"][4])
                telefono_entry.insert(0, elementos["values"][5])
                banco_entry.insert(0, elementos["values"][6])
                cuenta_entry.insert(0, str(elementos["values"][7]))
                tipo_cuenta_combobox.set(elementos["values"][8])
        except:
            messagebox.showerror("Error", "Seleciona un registro válido.")

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Registro de proveedor")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 650
    alto_ventana = 555
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="black")
    ventana.iconbitmap("./icon.ico")
    ruta_imagen_fondo="C:\Users\Admin\Documents\fondo_compras_rccOK.gif"  
    imagen_fondo= PhotoImage(file=ruta_imagen_fondo)
    fondo_label=label(ventana,image=imagen_fondo)
    fondo_label.placa(x=0,y=0,relwidth=1,relheight=1)

    marco = tkinter.Frame(ventana)
    marco.pack(padx=10, pady=10, fill="x")
    marco.config(bg="white")

    registro_tec_frame = tkinter.LabelFrame(
        marco, text="Registro de proveedor")
    registro_tec_frame.pack(padx=10, pady=10, fill="x")
    registro_tec_frame.config(
        bg="white", foreground="black", font="Barlow 13 ")

    marco_btn = tkinter.Frame(ventana, bg="black")
    marco_btn.pack(padx=70, pady=5, fill="x")

    razon_social_label = tkinter.Label(
        registro_tec_frame, text="Razón social", font="Barlow 11 ", bg="white")
    razon_social_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    razon_social_label.grid(column=0, row=0)
    razon_social_entry.grid(column=1, row=0)

    nit_label = tkinter.Label(
        registro_tec_frame, text="NIT/CC", font="Barlow 11 ", bg="white")
    nit_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    nit_label.grid(column=0, row=1)
    nit_entry.grid(column=1, row=1)

    direccion_label = tkinter.Label(
        registro_tec_frame, text="Dirección", font="Barlow 11 ", bg="white")
    direccion_label.grid(column=0, row=2)
    direccion_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    direccion_entry.grid(column=1, row=2)

    ciudad_label = tkinter.Label(
        registro_tec_frame, text="Ciudad", font="Barlow 11 ", bg="white")
    ciudad_label.grid(column=0, row=3)
    ciudad_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    ciudad_entry.grid(column=1, row=3)

    telefono_label = tkinter.Label(
        registro_tec_frame, text="Teléfono", font="Barlow 11 ", bg="white")
    telefono_label.grid(column=2, row=0)
    telefono_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    telefono_entry.grid(column=3, row=0)

    banco_label = tkinter.Label(
        registro_tec_frame, text="Banco", font="Barlow 11 ", bg="white")
    banco_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    banco_label.grid(column=2, row=1)
    banco_entry.grid(column=3, row=1)

    cuenta_label = tkinter.Label(
        registro_tec_frame, text="Cuenta", font="Barlow 11 ", bg="white")
    cuenta_entry = tkinter.Entry(registro_tec_frame, font="Barlow 11")
    cuenta_label.grid(column=2, row=2)
    cuenta_entry.grid(column=3, row=2)

    tipo_cuenta_label = tkinter.Label(
        registro_tec_frame, text="Tipo de cuenta", font="Barlow 11 ", bg="white")
    tipo_cuenta_label.grid(column=2, row=3)
    tipo_cuenta_combobox = ttk.Combobox(
        registro_tec_frame, state="readonly", values=["AHORROS", "CORRIENTE"])
    tipo_cuenta_combobox.grid(column=3, row=3)

    for widget in registro_tec_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)

    vertical_bar = ttk.Scrollbar(marco, orient="vertical")
    horizontal_bar = ttk.Scrollbar(marco, orient="horizontal")
    tabla = ttk.Treeview(marco, selectmode="browse")

    tabla.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.configure(command=tabla.yview)
    horizontal_bar.configure(command=tabla.xview)

    vertical_bar.pack(fill="y", side="right")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    tabla.bind("<ButtonRelease-1>", seleccionar_fila)

    tabla["columns"] = ("ID", "Razon Social", "NIT/CC", "Direccion", "Ciudad",
                        "Telefono", "Banco", "Cuenta", "Tipo de cuenta")

    tabla.column("#0", width=0, stretch=False)
    tabla.column("ID", anchor="center", width=40)
    tabla.column("Razon Social", anchor="center", width=150)
    tabla.column("NIT/CC", anchor="center", width=150)
    tabla.column("Direccion", anchor="center", width=150)
    tabla.column("Ciudad", anchor="center", width=150)
    tabla.column("Telefono", anchor="center", width=150)
    tabla.column("Banco", anchor="center", width=150)
    tabla.column("Cuenta", anchor="center", width=150)
    tabla.column("Tipo de cuenta", anchor="center", width=150)

    tabla.heading("#0", text="", anchor="w")
    tabla.heading("ID", text="ID", anchor="center")
    tabla.heading("Razon Social", text="Razón Social", anchor="center")
    tabla.heading("NIT/CC", text="NIT/CC", anchor="center")
    tabla.heading("Direccion", text="Dirección", anchor="center")
    tabla.heading("Ciudad", text="Ciudad", anchor="center")
    tabla.heading("Telefono", text="Teléfono", anchor="center")
    tabla.heading("Banco", text="Banco", anchor="center")
    tabla.heading("Cuenta", text="Cuenta", anchor="center")
    tabla.heading("Tipo de cuenta", text="Tipo de cuenta", anchor="center")

    conn = mysql.connector.connect(user='root', password='0000',
                                   host=importar_host(),
                                   database='RCC',
                                   port='3306')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM proveedores")
    datos = cursor.fetchall()
    for dato in datos:
        tabla.insert("", "end", values=dato)

    actualizar_btn = tkinter.Button(marco_btn, text="Actualizar",
                                    bd=0, relief="flat",
                                    font=("Barlow"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    width=20,
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    state="disabled",
                                    command=actualizar_datos)
    actualizar_btn.grid(column=0, row=0)
    actualizar_btn.bind("<Enter>", lambda event: hover_on(event, actualizar_btn))
    actualizar_btn.bind("<Leave>", lambda event: hover_off(event, actualizar_btn))

    registro_btn = tkinter.Button(marco_btn, text="Registrar",
                                  bd=0, relief="flat",
                                  font=("Barlow"),
                                  cursor="hand2",
                                  bg="#282e35",
                                  foreground="#00d2ff",
                                  activebackground="#282e35",
                                  activeforeground="#00d2ff",
                                  width=20,
                                  command=registrar_proveedor)
    registro_btn.grid(column=1, row=0)
    registro_btn.bind("<Enter>", lambda event: hover_on(event, registro_btn))
    registro_btn.bind("<Leave>", lambda event: hover_off(event, registro_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(padx=10)

    razon_social_entry.focus_set()

    ventana.bind("<Key>", limpiar_widgets)

    ventana.mainloop()
