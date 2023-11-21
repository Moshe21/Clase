import tkinter
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from funciones import *


def abrir_registro_tecnico():
    def seleccionar_fila(event):
        try:
            elementos = tabla.item(tabla.focus())
            if elementos:
                actualizar_btn.config(state="normal")
                bloquear_btn.config(state="normal")
                registro_btn.config(state="disabled")
                nombre_entry.delete(0, 'end')
                cc_entry.delete(0, 'end')
                telefono_entry.delete(0, 'end')
                cuenta_entry.delete(0, 'end')
                banco_entry.delete(0, 'end')
                tipo_cuenta_combobox.set("")
                regimen_entry.delete(0, 'end')
                pension_entry.delete(0, 'end')
                eps_entry.delete(0, 'end')
                caja_compensacion_entry.delete(0, 'end')

                nombre_entry.insert(0, elementos["values"][1])
                cc_entry.insert(0, elementos["values"][2])
                telefono_entry.insert(0, elementos["values"][3])
                cuenta_entry.insert(0, elementos["values"][4])
                banco_entry.insert(0, elementos["values"][5])
                tipo_cuenta_combobox.set(elementos["values"][6])
                regimen_entry.insert(0, elementos["values"][7])
                pension_entry.insert(0, elementos["values"][8])
                eps_entry.insert(0, elementos["values"][9])
                caja_compensacion_entry.insert(0, elementos["values"][10])
        except:
            messagebox.showerror("Error", "Seleciona un registro válido.")

    def limpiar_widgets(event):
        if event.keysym == 'Escape':
            nombre_entry.delete(0, 'end')
            cc_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            regimen_entry.delete(0, 'end')
            pension_entry.delete(0, 'end')
            eps_entry.delete(0, 'end')
            caja_compensacion_entry.delete(0, 'end')
            actualizar_btn.config(state="disabled")
            bloquear_btn.config(state="disabled")
            registro_btn.config(state="normal")

    def registrar_tecnico():
        nombre = nombre_entry.get().upper()
        cedula = cc_entry.get()
        telefono = telefono_entry.get()
        cuenta = cuenta_entry.get().upper()
        banco = banco_entry.get().upper()
        tipo_cuenta = tipo_cuenta_combobox.get()
        regimen = regimen_entry.get().upper()
        pension = pension_entry.get().upper()
        eps = eps_entry.get().upper()
        caja_compensacion = caja_compensacion_entry.get().upper()

        if nombre and cedula and telefono and cuenta and banco and tipo_cuenta and regimen:

            tabla.delete(*tabla.get_children())

            conn = mysql.connector.connect(user='root', password='0000',
                                           host=importar_host(),
                                           database='RCC',
                                           port='3306')

            data_insert_query = f'''INSERT INTO tecnicos  VALUES (null,'{nombre}', {cedula}, '{telefono}', '{cuenta}', '{banco}', '{tipo_cuenta}','{regimen}', '{pension}', '{eps}','{caja_compensacion}' )'''
            cursor = conn.cursor()
            cursor.execute(data_insert_query)
            cursor.execute("SELECT * FROM tecnicos")
            datos = cursor.fetchall()
            for dato in datos:
                tabla.insert("", "end", values=dato)
            tabla.pack()
            conn.commit()
            conn.close()
            nombre_entry.delete(0, 'end')
            cc_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            regimen_entry.delete(0, 'end')
            pension_entry.delete(0, 'end')
            eps_entry.delete(0, 'end')
            caja_compensacion_entry.delete(0, 'end')
            nombre_entry.focus_set()

            messagebox.showinfo(title="Registro realizado",
                                message="El registro fue realizado con éxito.")
        else:
            messagebox.showerror(title="Error de registro",
                                 message="Debes llenar los campos obligatorios.")

    def actualizar_datos():
        elementos = tabla.item(tabla.focus())
        id = elementos["values"][0]
        nombre = nombre_entry.get().upper()
        cedula = cc_entry.get()
        telefono = telefono_entry.get()
        cuenta = cuenta_entry.get().upper()
        banco = banco_entry.get().upper()
        tipo_cuenta = tipo_cuenta_combobox.get()
        regimen = regimen_entry.get().upper()
        pension = pension_entry.get().upper()
        eps = eps_entry.get().upper()
        caja_compensacion = caja_compensacion_entry.get().upper()

        if nombre and cedula and telefono and cuenta and banco and tipo_cuenta and regimen:
            tabla.delete(*tabla.get_children())

            conn = mysql.connector.connect(user='root', password='0000',
                                           host=importar_host(),
                                           database='RCC',
                                           port='3306')
            cursor = conn.cursor()
            query = f'''UPDATE tecnicos SET nombre = %s, cc = %s, cuenta = %s, tipo_cuenta = %s, banco = %s, telefono = %s, regimen = %s, pension = %s, eps = %s, caja_compensacion = %s WHERE id = {id}'''
            info = (nombre, cedula, telefono, cuenta, banco,
                    tipo_cuenta, regimen, pension, eps, caja_compensacion)
            cursor.execute(query, info)
            cursor.execute("SELECT * FROM tecnicos")
            datos = cursor.fetchall()
            for dato in datos:
                tabla.insert("", "end", values=dato)
            tabla.pack()
            conn.commit()
            conn.close()
            nombre_entry.delete(0, 'end')
            cc_entry.delete(0, 'end')
            telefono_entry.delete(0, 'end')
            cuenta_entry.delete(0, 'end')
            banco_entry.delete(0, 'end')
            tipo_cuenta_combobox.set("")
            regimen_entry.delete(0, 'end')
            pension_entry.delete(0, 'end')
            eps_entry.delete(0, 'end')
            caja_compensacion_entry.delete(0, 'end')
            nombre_entry.focus_set()

            messagebox.showinfo(title="Proceso exitoso",
                                message="La actualización de datos fue realizada con éxito.")
        else:
            messagebox.showerror(title="Error",
                                 message="Estás eliminando un dato obligatorio.")
    
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
                instruccion = f"""INSERT INTO tecnicos_bloqueados (nombre, cc, cuenta, tipo_cuenta, banco, telefono, regimen, pension, eps, caja_compensacion) SELECT nombre, cc, cuenta, tipo_cuenta, banco, telefono, regimen, pension, eps, caja_compensacion FROM tecnicos WHERE id = {id}"""
                cursor.execute(instruccion)
                eliminar_tecnico = f"DELETE FROM tecnicos WHERE id = {id}"
                cursor.execute(eliminar_tecnico)
                filas = tabla.get_children()
                for fila in filas:
                    tabla.delete(fila)
                instruccion_refresh = "SELECT * FROM tecnicos"
                cursor.execute(instruccion_refresh)
                registros = cursor.fetchall()
                for registro in registros:
                    tabla.insert('', 'end', values=registro)
                tabla.pack()
                conn.commit()
                conn.close()
                messagebox.showinfo("Proceso exitoso","El técnico se ha bloqueado con éxito.")

    ventana = tkinter.Tk()
    ventana.title("Scrum Manager | Registro de técnicos")
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = 635
    alto_ventana = 680
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - (alto_ventana + 30)) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    ventana.config(bg="white")
    ventana.iconbitmap("./icon.ico")

    marco = tkinter.Frame(ventana)
    marco.pack(padx=10, pady=10, fill="x")
    marco.config(bg="white")

    registro_tec_frame = tkinter.LabelFrame(
        marco, text="Registro de personal técnico")
    registro_tec_frame.pack(padx=10, pady=10, fill="x")
    registro_tec_frame.config(
        bg="white", foreground="black", font="Barlow 13 ")

    marco_btn = tkinter.Frame(ventana, bg="white")
    marco_btn.pack(padx=50, pady=5)

    nombre_label = tkinter.Label(
        registro_tec_frame, text="Nombre", font="Barlow 11 ", bg="white")
    nombre_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10")
    nombre_label.grid(column=0, row=0)
    nombre_entry.grid(column=1, row=0)

    cc_label = tkinter.Label(
        registro_tec_frame, text="Cedula", font="Barlow 11 ", bg="white")
    cc_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10")
    cc_label.grid(column=0, row=1)
    cc_entry.grid(column=1, row=1)

    telefono_label = tkinter.Label(
        registro_tec_frame, text="Teléfono", font="Barlow 11 ", bg="white")
    telefono_label.grid(column=0, row=2)
    telefono_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10")
    telefono_entry.grid(column=1, row=2)

    regimen_label = tkinter.Label(
        registro_tec_frame, text="Régimen", font="Barlow 11 ", bg="white")
    regimen_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10", )
    regimen_label.grid(column=0, row=3)
    regimen_entry.grid(column=1, row=3)

    pension_label = tkinter.Label(
        registro_tec_frame, text="Pensión", font="Barlow 11 ", bg="white")
    pension_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10", )
    pension_label.grid(column=0, row=4)
    pension_entry.grid(column=1, row=4)

    cuenta_label = tkinter.Label(
        registro_tec_frame, text="Cuenta", font="Barlow 11 ", bg="white")
    cuenta_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10")
    cuenta_label.grid(column=2, row=0)
    cuenta_entry.grid(column=3, row=0)

    banco_label = tkinter.Label(
        registro_tec_frame, text="Banco", font="Barlow 11 ", bg="white")
    banco_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10")
    banco_label.grid(column=2, row=1)
    banco_entry.grid(column=3, row=1)

    tipo_cuenta_label = tkinter.Label(
        registro_tec_frame, text="Tipo de cuenta", font="Barlow 11 ", bg="white")
    tipo_cuenta_combobox = ttk.Combobox(
        registro_tec_frame, state="readonly", values=["AHORROS", "CORRIENTE", "N/A"])
    tipo_cuenta_label.grid(column=2, row=2)
    tipo_cuenta_combobox.grid(column=3, row=2)

    eps_label = tkinter.Label(
        registro_tec_frame, text="EPS", font="Barlow 11 ", bg="white")
    eps_entry = tkinter.Entry(registro_tec_frame, font="Barlow 10", )
    eps_label.grid(column=2, row=3)
    eps_entry.grid(column=3, row=3)

    caja_compensacion_label = tkinter.Label(
        registro_tec_frame, text="Caja de compensación", font="Barlow 11 ", bg="white")
    caja_compensacion_entry = tkinter.Entry(
        registro_tec_frame, font="Barlow 10", )
    caja_compensacion_label.grid(column=2, row=4)
    caja_compensacion_entry.grid(column=3, row=4)

    for widget in registro_tec_frame.winfo_children():
        widget.grid_configure(padx=10, pady=10)

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
    cursor.execute("SELECT * FROM tecnicos")
    datos = cursor.fetchall()
    for dato in datos:
        tabla.insert("", "end", values=dato)
    conn.commit()
    conn.close()

    vertical_bar.pack(fill="y", side="right")
    tabla.pack(fill="x")
    horizontal_bar.pack(fill="x")

    tabla.bind("<ButtonRelease-1>", seleccionar_fila)

    actualizar_btn = tkinter.Button(marco_btn, text="Actualizar",
                                    bd=0, relief="flat",
                                    font=("Barlow"),
                                    cursor="hand2",
                                    bg="#282e35",
                                    width=20,
                                    foreground="#00d2ff",
                                    activebackground="#282e35",
                                    activeforeground="#00d2ff",
                                    command=actualizar_datos,
                                    state="disabled")
    actualizar_btn.grid(column=0, row=0)
    actualizar_btn.bind(
        "<Enter>", lambda event: hover_on(event, actualizar_btn))
    actualizar_btn.bind(
        "<Leave>", lambda event: hover_off(event, actualizar_btn))

    registro_btn = tkinter.Button(marco_btn, text="Registrar",
                                  bd=0, relief="flat",
                                  font=("Barlow"),
                                  cursor="hand2",
                                  bg="#282e35",
                                  width=20,
                                  foreground="#00d2ff",
                                  activebackground="#282e35",
                                  activeforeground="#00d2ff",
                                  command=registrar_tecnico)
    registro_btn.grid(column=1, row=0)
    registro_btn.bind("<Enter>", lambda event: hover_on(event, registro_btn))
    registro_btn.bind("<Leave>", lambda event: hover_off(event, registro_btn))

    bloquear_btn = tkinter.Button(marco_btn, text="Bloquear",
                                  bd=0, relief="flat",
                                  font=("Barlow"),
                                  cursor="hand2",
                                  bg="#282e35",
                                  width=20,
                                  foreground="#00d2ff",
                                  activebackground="#282e35",
                                  activeforeground="#00d2ff",
                                  state="disabled",
                                  command=bloquear_tecnico)
    bloquear_btn.grid(column=0, row=1, columnspan=2)
    bloquear_btn.bind("<Enter>", lambda event: hover_on(event, bloquear_btn))
    bloquear_btn.bind("<Leave>", lambda event: hover_off(event, bloquear_btn))

    for widget in marco_btn.winfo_children():
        widget.grid_configure(pady=10, padx=10)

    nombre_entry.focus_set()

    ventana.bind("<Key>", limpiar_widgets)

    ventana.mainloop()
