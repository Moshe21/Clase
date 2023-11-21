from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Data_Base import *
from datetime import datetime
from funciones import *


class Gestor_Afiliaciones:
    def __init__(self, usr):
        self.user = usr
        self.master = Toplevel()
        self.master.title("Scrum Manager | Afiliaciones")
        self.master.config(background="white")
        self.master.geometry(centrar_ventana(self.master, 940, 580))
        self.master.resizable(0, 0)
        self.master.iconbitmap("./icon.ico")
        self.frame()
        self.labelsandentrys()
        self.Botones()
        self.tabla()
        self.master.mainloop()

    def frame(self):

        self.titulo = Label(self.master, text="AFILIACIONES",
                            font="Barlow 22", background="#282e35", foreground="white")
        self.titulo.grid(column=0, row=0, padx=10, pady=10,
                         columnspan=2, sticky=(W, E))

        self.Marco_Registro = LabelFrame(
            self.master, text="Registro de afiliaciones", width=800, height=200, background="white")
        self.Marco_Registro.grid(column=0, row=1, padx=10, pady=10)

        self.marco_tablaBD = LabelFrame(
            self.master, text="Afiliaciones", width=820, height=310, background="white")
        self.marco_tablaBD.grid(
            column=0, row=2, padx=10, pady=10, columnspan=2)

        self.Marco_BT = Frame(self.master, background="white")
        self.Marco_BT.grid(column=1, row=1, padx=10)

        self.marco_Bus = Frame(self.marco_tablaBD, background="#071C4B")
        self.marco_Bus.place(width=800, height=40)

    def labelsandentrys(self):
        self.NameCase = Label(self.Marco_Registro, text="Caso",
                              font="Barlow 11", background="white")
        self.NameCase.grid(column=0, row=0, padx=5, pady=5)
        self.E_Caso1 = StringVar()
        self.set_case = Entry(self.Marco_Registro,
                              textvariable=self.E_Caso1, font="Barlow 10")
        self.set_case.grid(column=1, row=0)
        self.set_case.bind("<FocusOut>", self.validar_caso)

        self.Name = Label(self.Marco_Registro, text="Gestor",
                          font="Barlow 11", background="white")
        self.Name.grid(column=2, row=0, padx=5, pady=5)
        self.gestor = Entry(self.Marco_Registro, font="Barlow 10")
        self.gestor.insert(0, self.user)
        self.gestor.config(state="readonly")
        self.gestor.grid(column=3, row=0)


        self.NameAf = Label(
            self.Marco_Registro, text="Nombre y apellido", font="Barlow 11", background="white")
        self.NameAf.grid(column=0, row=1, padx=5, pady=5)
        
        db = conexion()
        self.opciones = db.lista_de_nombresTC()
        self.set_AF = Entry(self.Marco_Registro, font="Barlow 10")
        self.set_AF.grid(column=1, row=1)
        self.set_AF.bind("<FocusOut>", self.completar_datos)
        self.set_AF.bind("<KeyRelease>", self.autocompletar)

        

        self.NroCC = Label(self.Marco_Registro, text="N° Documento",
                           font="Barlow 11", background="white")
        self.NroCC.grid(column=2, row=1, padx=5, pady=5)
        self.set_NCC = Entry(self.Marco_Registro, font="Barlow 10")
        self.set_NCC.grid(column=3, row=1)

        self.txttlf = Label(self.Marco_Registro, text="N° TLF",
                              font="Barlow 11", background="white")
        self.txttlf.grid(column=4, row=0, padx=5, pady=5)
        self.tlf = ttk.Combobox(self.Marco_Registro,
                                width=17, font="Barlow 10", state="readonly")
        self.tlf.grid(column=5, row=0)

        self.fecha_af = Label(self.Marco_Registro, text="Desde",
                              font="Barlow 11", background="white")
        self.fecha_af.grid(column=0, row=2, padx=5, pady=5)
        self.faf = Entry(self.Marco_Registro, font="Barlow 10")
        self.faf.grid(column=1, row=2)
        self.faf.bind(
            "<Key>", lambda event: self.FormatoFecha(event, self.faf))
        self.faf.bind("<BackSpace>", lambda _: self.faf.delete(END))

        self.fecha_df = Label(self.Marco_Registro, text="Hasta",
                              font="Barlow 11", background="white")
        self.fecha_df.grid(column=2, row=2, padx=5, pady=5)
        self.fdf = Entry(self.Marco_Registro, font="Barlow 10")
        self.fdf.grid(column=3, row=2)
        self.fdf.bind(
            "<Key>", lambda event: self.FormatoFecha(event, self.fdf))
        self.fdf.bind("<BackSpace>", lambda _: self.fdf.delete(END))
        self.fdf.bind("<FocusOut>", lambda event: self.Calcular_dias_afiliación("",self.faf.get(), self.fdf.get()))

        self.tipoAF = Label(self.Marco_Registro, text="Régimen",
                            font="Barlow 11", background="white")
        self.tipoAF.grid(column=4, row=1, padx=5, pady=5)
        self.TAF = Entry(self.Marco_Registro, font="Barlow 10")
        self.TAF.grid(column=5, row=1)

        self.dias_afiliacion = Label(self.Marco_Registro, text="Días Afiliación",
                            font="Barlow 11", background="white")
        self.dias_afiliacion.grid(column=4, row=2, padx=5, pady=5)

        self.DiasAfiliacion = Entry(self.Marco_Registro, font="Barlow 10", width=6)
        self.DiasAfiliacion.grid(column=5, row=2, sticky=(W))

        self.dias_afiliacion = Label(self.Marco_Registro, text="$",
                            font="Barlow 11", background="white")
        self.dias_afiliacion.grid(column=5, row=2, padx=5, pady=5)
        
        self.CostoDAF = IntVar()
        self.costo_diario_afiliacion = Entry(self.Marco_Registro, font="Barlow 10", width=9)
        self.costo_diario_afiliacion.grid(column=5, row=2, sticky=(E))
        self.costo_diario_afiliacion.bind("<FocusOut>", self.costo_Total_afiliaciones)
        self.costo_diario_afiliacion.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.costo_diario_afiliacion))


        self.costoAF = Label(
            self.Marco_Registro, text="Costo afiliación", font="Barlow 11", background="white")
        self.costoAF.grid(column=0, row=3, padx=5, pady=5)
        self.CAF = Entry(self.Marco_Registro, font="Barlow 10")
        self.CAF.grid(column=1, row=3)

        self.EAF = Label(self.Marco_Registro, text="Estado afiliación",
                         background="white", font="Barlow 11")
        self.EAF.grid(column=2, row=3, padx=5, pady=5)
        self.Est = ttk.Combobox(self.Marco_Registro, values=[
                                "Afiliado", "Desafiliado"], state="disabled", background="green", width=17, font="Barlow 10")
        self.Est.insert(0, 0)
        self.Est.grid(column=3, row=3)

        self.txtCiudad = Label(self.Marco_Registro,
                               text="Ciudad", font="Barlow 11", bg="white")
        self.txtCiudad.grid(column=4, row=3)
        db1 = conexion()
        self.listaCiudades = db1.lista_ciudaddes()
        self.Ciudad = ttk.Combobox(self.Marco_Registro, font="Barlow 10", values=self.listaCiudades, width=17)
        self.Ciudad.grid(column=5, row=3)

        self.E_Bus = StringVar()
        self.Bus = Entry(
            self.marco_Bus, textvariable=self.E_Bus, font="Barlow 10")
        self.Bus.grid(column=0, row=0, padx=15, pady=5)

        self.lista_sugerencias = Listbox(self.Marco_Registro, relief="flat")

        self.lista_sugerencias.bind("<<ListboxSelect>>", self.seleccionar_sugerencia)



    def Botones(self):
        self.BT_Registro = Button(self.Marco_BT, text="Registrar", font="Barlow 12",
                                  background="#282e35", foreground="#00d2ff", command=self.Registro, width=10)
        self.BT_Registro.grid(column=0, row=0, pady=5)
        self.BT_Registro.bind(
            "<Enter>", lambda event: hover_on(event, self.BT_Registro))
        self.BT_Registro.bind(
            "<Leave>", lambda event: hover_off(event, self.BT_Registro))

        self.BT_Eliminar = Button(self.Marco_BT, text="Eliminar", font="Barlow 12",
                                  background="#282e35", foreground="#00d2ff", width=10, command=self.eliminar)
        self.BT_Eliminar.grid(column=0, row=1, pady=5)
        self.BT_Eliminar.bind(
            "<Enter>", lambda event: hover_on(event, self.BT_Eliminar))
        self.BT_Eliminar.bind(
            "<Leave>", lambda event: hover_off(event, self.BT_Eliminar))

        self.BT_enviar = Button(self.Marco_BT, text="Enviar", font="Barlow 12",
                                background="#282e35", foreground="#00d2ff", width=10, command=self.enviar)
        self.BT_enviar.grid(column=0, row=2, pady=5)
        self.BT_enviar.bind(
            "<Enter>", lambda event: hover_on(event, self.BT_enviar))
        self.BT_enviar.bind(
            "<Leave>", lambda event: hover_off(event, self.BT_enviar))

    def tabla(self):
        self.vsitabdg = ttk.Treeview(self.marco_tablaBD, columns=(
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21), show="headings")
        self.BarraV = Scrollbar(
            self.marco_tablaBD, orient="vertical", command=self.vsitabdg.yview)
        self.BarraV.place(relx=0.98, width=20, height=280)
        self.BarraH = Scrollbar(
            self.marco_tablaBD, orient="horizontal", command=self.vsitabdg.xview)
        self.BarraH.place(rely=0.95, width=815, height=20)
        self.vsitabdg.config(xscrollcommand=self.BarraH.set,
                             yscrollcommand=self.BarraV.set)

        self.vsitabdg.heading(1, text="ID")
        self.vsitabdg.heading(2, text="CASO")
        self.vsitabdg.heading(3, text="GESTOR")
        self.vsitabdg.heading(4, text="FECHA SOLICITUD")
        self.vsitabdg.heading(5, text="NOMBRE Y APELLIDO")
        self.vsitabdg.heading(6, text="N° DOCUMENTO")
        self.vsitabdg.heading(7, text="TLF")
        self.vsitabdg.heading(8, text="DESDE")
        self.vsitabdg.heading(9, text="HASTA")
        self.vsitabdg.heading(10, text="COSTO-AFL")
        self.vsitabdg.heading(11, text="REGIMEN")
        self.vsitabdg.heading(12, text="EST-AFL")
        self.vsitabdg.heading(13, text="CIUDAD")
        self.vsitabdg.heading(14, text="SALARIO")
        self.vsitabdg.heading(15, text="ARL")
        self.vsitabdg.heading(16, text="EPS")
        self.vsitabdg.heading(17, text="PENSION")
        self.vsitabdg.heading(18, text="CAJA COMPENSACIÓN")
        self.vsitabdg.heading(19, text="APORTES EN lINEA")
        self.vsitabdg.heading(20, text="COMENTARIO")
        self.vsitabdg.heading(21, text="HISTORIAL")

        self.vsitabdg.column(1, anchor="center", width=0)
        self.vsitabdg.column(2, anchor="center", width=90)
        self.vsitabdg.column(3, anchor="center", width=120)
        self.vsitabdg.column(4, anchor="center", width=120)
        self.vsitabdg.column(5, anchor="center", width=120)
        self.vsitabdg.column(6, anchor="center", width=90)
        self.vsitabdg.column(7, anchor="center", width=90)
        self.vsitabdg.column(8, anchor="center", width=90)
        self.vsitabdg.column(9, anchor="center", width=90)
        self.vsitabdg.column(10, anchor="center", width=90)
        self.vsitabdg.column(11, anchor="center", width=90)
        self.vsitabdg.column(12, anchor="center", width=90)
        self.vsitabdg.column(13, anchor="center", width=90)
        self.vsitabdg.column(14, anchor="center", width=90)
        self.vsitabdg.column(15, anchor="center", width=90)
        self.vsitabdg.column(16, anchor="center", width=90)
        self.vsitabdg.column(17, anchor="center", width=90)
        self.vsitabdg.column(18, anchor="center", width=90)
        self.vsitabdg.column(19, anchor="center", width=120)
        self.vsitabdg.column(20, anchor="center", width=120)
        self.vsitabdg.column(21, anchor="center", width=120)

        self.vsitabdg.place(width=800, height=280)

    def actualizartabla(self):
        self.vsitabdg.delete(*self.vsitabdg.get_children())
        self.tabla()

    def setCjTX(self):
        self.set_case.delete(0, END)
        
        self.set_AF.delete(0, END)
        self.set_NCC.delete(0, END)

        self.tlf.set("")
        self.faf.delete(0, END)
        self.fdf.delete(0, END)
        self.CAF.config(state="normal")
        self.CAF.delete(0, END)
        self.TAF.delete(0, END)
        self.Ciudad.delete(0, END)
        self.costo_diario_afiliacion.delete(0,END)
        self.DiasAfiliacion.config(state="normal")
        self.DiasAfiliacion.delete(0,END)

    def FormatoFecha(self, event, variable):
        if event.char.isdigit():
            texto = variable.get()
            letra = 0
            for i in texto:
                letra += 1
            if letra == 2:
                variable.insert(2, "/")
            elif letra == 5:
                variable.insert(5, "/")
        elif event.keysym == "Tab":
            pass
        else:
            return "break"

    def Registro(self):
        if self.set_case.get() != "" and self.gestor.get() != "" and self.set_AF.get() != "" and self.set_NCC.get() != "" and self.tlf.get() != "" and self.faf.get() != "" and self.fdf.get() != "" and self.CAF.get() != "":
            arr = ["", self.set_case.get().upper(), self.gestor.get().upper(), " ", self.set_AF.get().upper(), self.set_NCC.get().upper(),
                   self.tlf.get(), self.faf.get(), self.fdf.get(), self.total_costo_afiliacion, self.TAF.get(
            ).upper(), self.Est.get().upper(), self.Ciudad.get().upper(), 1, "SURA",
                self.eps, self.pension, self.caja_compensasion, "", ""]

            self.vsitabdg.insert('', 'end', values=arr)
            self.set_NCC.config(state="normal")
            self.tlf.config(state="normal")
            self.TAF.config(state="normal")
            self.setCjTX()
        else:
            messagebox.showerror("Error", "todos los datos son obligatorios")

    def enviar(self):
        datos2 = self.vsitabdg.get_children()
        if datos2:
            for i in datos2:
                bd = conexion()
                datosTV = self.vsitabdg.item(i)
                arr = [datosTV["values"][1], datosTV["values"][2], datosTV["values"][4], datosTV["values"][5], datosTV["values"][6], datosTV["values"][7], datosTV["values"][8], datosTV["values"][9], datosTV["values"]
                       [10], datosTV["values"][11], datosTV["values"][12], datosTV["values"][13], datosTV["values"][14], datosTV["values"][15], datosTV["values"][16], datosTV["values"][17], datosTV["values"][18], datosTV["values"][19]]
                bd.ResgiterAfiliaciones(arr)
            self.actualizartabla()
            messagebox.showinfo(
                "Proceso exitoso", "Afiliaciones realizadas con éxito")
        else:
            messagebox.showerror("Error", "no existe registro")

    def eliminar(self):
        try:
            self.vsitabdg.delete(self.vsitabdg.focus())
        except TclError:
            messagebox.showerror("Error", "no se ha seleccionado ninguna fila")

    def validar_caso(self, event):
        bd = conexion()
        validar = bd.validarcaso(self.set_case.get())

        try:
            validar[0][0] == self.E_Caso1.get()
            pass
        except IndexError:
            messagebox.showerror("Error", "El caso digitado no existe")
            self.set_case.delete(0, 'end')
            self.set_case.focus_set()

    def completar_datos(self, event):
        db = conexion()

        if db.validar_nombreTC(self.set_AF.get()) is True:
            self.set_NCC.config(state="normal")
            self.tlf.config(state="normal")
            self.TAF.config(state="normal")
            self.caja_compensasion = db.caja_compensacion_tecnico(
                self.set_AF.get())
            self.pension = db.pension_tecnico(self.set_AF.get())
            self.eps = db.eps_tecnico(self.set_AF.get())
            self.set_NCC.delete(0, END)
            self.tlf.set("")
            self.TAF.delete(0, END)
            self.set_NCC.insert(0, db.CC_tecnico(self.set_AF.get()))
            self.telefono = db.tlf_tecnico(self.set_AF.get())
            self.tlf.config(values=self.telefono)
            self.TAF.insert(0, db.regimen_tecnico(self.set_AF.get()))
            self.set_NCC.config(state="readonly")
            self.tlf.config(state="readonly")
            self.TAF.config(state="readonly")
        else:
            messagebox.showerror(
                "Error", "El técnico seleccionado no se encuentra registrado en la base de datos")
            self.set_AF.delete(0, 'end')
            self.set_AF.focus_set()
    

    def autocompletar(self,event):
        
            entrada_texto = self.set_AF.get()

            # Borra todas las sugerencias actuales
            self.lista_sugerencias.delete(0, END)

            if entrada_texto:
                sugerencias = [s for s in self.opciones if entrada_texto.upper() in s.upper()]
                for sugerencia in sugerencias:
                    self.lista_sugerencias.insert(END, sugerencia)
            self.lista_sugerencias.place(relx=0.17, rely=0.47)
        

    def seleccionar_sugerencia(self,event):
        try:
            entrada_texto = self.lista_sugerencias.get(self.lista_sugerencias.curselection())
            self.set_AF.delete(0, END)
            self.set_AF.insert(0, entrada_texto)
            self.lista_sugerencias.delete(0, END)
            self.lista_sugerencias.place_forget()
        except TclError:
            pass
    def Calcular_dias_afiliación(self, event, fecha1, fecha2):
        self.DiasAfiliacion.config(state="normal")
        self.DiasAfiliacion.delete(0,END)
        fecha1_obj = datetime.strptime(fecha1, "%d/%m/%Y")
        fecha2_obj = datetime.strptime(fecha2, "%d/%m/%Y")

        diferencia = fecha2_obj - fecha1_obj

        self.DiasAfiliacion.insert(0,diferencia.days)
        self.DiasAfiliacion.config(state="readonly")

    def costo_Total_afiliaciones(self,event):
        self.CAF.config(state="normal")
        self.CAF.delete(0,END)
        diasAfiliacion = int(self.DiasAfiliacion.get())
        costoAfiliacion = float(self.costo_diario_afiliacion.get())
        self.total_costo_afiliacion = 0
        if self.TAF.get() =="CONTRIBUTIVO":
            self.total_costo_afiliacion = diasAfiliacion*costoAfiliacion
        elif self.TAF.get() =="SUBSIDIADO":
            if diasAfiliacion <= 7:
                self.total_costo_afiliacion = costoAfiliacion
            elif diasAfiliacion > 7 <= 14:
                self.total_costo_afiliacion = costoAfiliacion*2
            elif diasAfiliacion > 14 <= 21:
                self.total_costo_afiliacion = costoAfiliacion*3
            elif diasAfiliacion > 21 <= 28:
                self.total_costo_afiliacion = costoAfiliacion*4
        self.validarseparadores("",self.CostoDAF, self.costo_diario_afiliacion)
        self.CAF.insert(0, "{:,}".format(self.total_costo_afiliacion))
        self.CAF.config(state="readonly")

    def validarseparadores(self, event, num,variable):
         variable.select_range(0,END)
         numero = float(variable.get())
         numero_formateado = "{:,}".format(numero)
         variable.delete(0, END)
         variable.insert(0, numero_formateado)
         num.set(numero)


    def vaciar_entry(self,event, variable):
        numero = variable.get()
        formateado = ""
        for i in numero:
            if i ==",":
                pass
            else:
                formateado += i
        variable.delete(0,"end")
        variable.insert(0, formateado)
        variable.select_range(0,"end")
            

   
