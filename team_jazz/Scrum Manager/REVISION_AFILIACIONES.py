from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Data_Base import *
from funciones import *


class MODULO_RRHH: 
    def __init__(self, master):
        self.window = master
        self.frame()
        self.labelsandentrys()
        self.tabla()
        self.mostrar_tabla_afiliaciones()
        self.Botones()
      
       

    def frame (self):
        self.master = Frame(self.window, bg="white")
        self.master.pack()
        self.titulo = Label (self.master, text="AFILIACIONES", font="Barlow 22", background="#282e35", foreground="white")
        self.titulo.grid(column=0, row=0, columnspan=2, sticky=(E,W))

        self.Marco_Registro = LabelFrame(self.master, width=800,height=200,background="white")
        self.Marco_Registro.grid(column=0, row=1, sticky=(N))

        self.marco_tablaBD = LabelFrame(self.master, width=620, height=450,background="white")
        self.marco_tablaBD.grid(column=1,row=1, sticky=(N))

        self.Marco_BT = Frame(self.master, background="white")
        self.Marco_BT.grid(column=0, row=2,  sticky=(N))

        self.marco_Bus = Frame(self.marco_tablaBD, background="#282e35")
        self.marco_Bus.place(width=920, height=40)
    
    def labelsandentrys (self):
        self.NameCase = Label(self.Marco_Registro, text="Caso", font="Barlow 11", background="white")
        self.NameCase.grid(column=0,row=0, padx=5,pady=5)
        self.E_Caso = StringVar()
        self.set_case = Entry(self.Marco_Registro, textvariable=self.E_Caso, font="Barlow 10")
        self.set_case.grid(column=1,row=0, padx=5,pady=5)
        self.set_case.bind("<FocusOut>", self.validar_caso)

        self.Name = Label(self.Marco_Registro, text="Gestor", font="Barlow 11", background="white")
        self.Name.grid(column=0,row=1, padx=5,pady=5)
        self.E_Gestor = StringVar()
        self.gestor = Entry(self.Marco_Registro, textvariable=self.E_Gestor,font="Barlow 10")
        self.gestor.grid(column=1,row=1, padx=5,pady=5)

        self.FR = Label(self.Marco_Registro, text="Fecha solicitud", font="Barlow 11", background="white")
        self.FR.grid(column=0,row=2, padx=5,pady=5)
        self.E_fecha = StringVar()
        self.fechaR = Entry(self.Marco_Registro, textvariable=self.E_fecha, state="disabled", font="Barlow 10")
        self.fechaR.grid(column=1,row=2, padx=5,pady=5)

        self.NameAf = Label(self.Marco_Registro, text="Nombre y apellido", font="Barlow 11", background="white")
        self.NameAf.grid(column=0,row=3, padx=5,pady=5)
        self.E_Afiliado = StringVar()
        self.set_AF = Entry(self.Marco_Registro, textvariable=self.E_Afiliado, font="Barlow 10")
        self.set_AF.grid(column=1,row=3, padx=5,pady=5)


        self.NroCC = Label(self.Marco_Registro, text="N° Documento", font="Barlow 11", background="white")
        self.NroCC.grid(column=0,row=4, padx=5,pady=5)
        self.E_NCC = StringVar()
        self.set_NCC = Entry(self.Marco_Registro, textvariable=self.E_NCC, font="Barlow 10")
        self.set_NCC.grid(column=1,row=4, padx=5,pady=5)

        self.fecha_df = Label(self.Marco_Registro, text="N° TLF", font="Barlow 11", background="white")
        self.fecha_df.grid(column=0,row=5, padx=5,pady=5)
        self.E_TLF = StringVar()
        self.tlf = Entry(self.Marco_Registro, textvariable=self.E_TLF, font="Barlow 10")
        self.tlf.grid(column=1,row=5, padx=5,pady=5)

        self.fecha_af = Label(self.Marco_Registro, text="Desde", font="Barlow 11", background="white")
        self.fecha_af.grid(column=0,row=6, padx=5,pady=5)
        self.E_FAF = StringVar()
        self.faf = Entry(self.Marco_Registro, textvariable=self.E_FAF, font="Barlow 10")
        self.faf.grid(column=1,row=6, padx=5,pady=5)

        self.fecha_df = Label(self.Marco_Registro, text="Hasta", font="Barlow 11", background="white")
        self.fecha_df.grid(column=0,row=7, padx=5,pady=5)
        self.E_FDF = StringVar()
        self.fdf = Entry(self.Marco_Registro, textvariable=self.E_FDF, font="Barlow 10")
        self.fdf.grid(column=1,row=7, padx=5,pady=5)

        self.faf.bind("<Key>", lambda event:self.FormatoFecha(event,self.faf))
        self.faf.bind("<BackSpace>", lambda _:self.faf.delete(END))

        self.fdf.bind("<Key>", lambda event:self.FormatoFecha(event,self.fdf))
        self.fdf.bind("<BackSpace>", lambda _:self.fdf.delete(END))

        self.tipoAF = Label(self.Marco_Registro, text="Regimen", font="Barlow 11", background="white")
        self.tipoAF.grid(column=0,row=8, padx=5,pady=5)
        self.E_TAF = StringVar()
        self.TAF = Entry(self.Marco_Registro, textvariable=self.E_TAF, font="Barlow 10")
        self.TAF.grid(column=1,row=8, padx=5,pady=5)

        self.costoAF = Label(self.Marco_Registro, text="Costo afiliación", font="Barlow 11", background="white")
        self.costoAF.grid(column=0,row=9, padx=5,pady=5)

        self.E_CAF = IntVar()
        self.CAF = Entry(self.Marco_Registro, font="Barlow 10")
        self.CAF.grid(column=1,row=9, padx=5,pady=5)
        self.CAF.bind("<FocusOut>", lambda event: self.validarseparadores(event,self.E_CAF ,self.CAF))
        self.CAF.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.CAF))

        self.EAF = Label(self.Marco_Registro, text="Estado afiliacion", background="white", font="Barlow 11")
        self.EAF.grid(column=0, row=10, padx=5,pady=5)
        self.E_EST = StringVar()
        self.E_EST.set("Desafiliado")
        self.Est = ttk.Combobox(self.Marco_Registro, textvariable=self.E_EST, values=["Afiliado","Desafiliado"], state="readonly", background="green", width=17, font="Barlow 10")
        self.Est.grid(column=1,row=10, padx=5,pady=5)
        
        self.txtCiudad = Label(self.Marco_Registro, text="Ciudad", background="white", font="Barlow 11")
        self.txtCiudad.grid(column=2, row=0, padx=5,pady=5)
        self.E_Ciudad = StringVar()
        self.ciudad= Entry(self.Marco_Registro, textvariable=self.E_Ciudad, font="Barlow 10")
        self.ciudad.grid(column=3,row=0, padx=5,pady=5)
       

        self.Salario = Label(self.Marco_Registro, text="Salario", font="Barlow 11", bg="white")
        self.Salario.grid(column=2,row=1, padx=5,pady=5)
        self.E_salario = IntVar()
        self.E_salario.set(1)
        self.Slrio = IntVar()
        self.Entrada_salario = Entry(self.Marco_Registro, font="Barlow 10", textvariable=self.Slrio)
        self.Entrada_salario.grid(column=3,row=1, padx=5,pady=5)
        self.Entrada_salario.bind("<FocusOut>", lambda event: self.validarseparadores(event,self.E_salario ,self.Entrada_salario))
        self.Entrada_salario.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.Entrada_salario))

        self.txt_Arl = Label(self.Marco_Registro, text="ARL", bg="white", font="Barlow 11")
        self.txt_Arl.grid(column=2,row=2, padx=5,pady=5)
        self.E_arl = StringVar()
        self.Entrada_arl = Entry(self.Marco_Registro, textvariable=self.E_arl, font="Barlow 10")
        self.Entrada_arl.grid(column=3, row=2, padx=5,pady=5)

        self.txt_Eps = Label( self.Marco_Registro, text="EPS", bg="white", font="Barlow 11")
        self.txt_Eps.grid(column=2, row=3, padx=5,pady=5)
        self.E_eps = StringVar()
        self.Entrada_eps = Entry(self.Marco_Registro, textvariable=self.E_eps, font="Barlow 10")
        self.Entrada_eps.grid(column=3, row=3, padx=5,pady=5)

        self.txt_Pension = Label(self.Marco_Registro, text="Pension", bg="white", font="Barlow 11")
        self.txt_Pension.grid(column=2, row=4,padx=5,pady=5)
        self.E_pension = StringVar()
        self.Entrada_pension = Entry(self.Marco_Registro, textvariable=self.E_pension, font="Barlow 10")
        self.Entrada_pension.grid(column=3, row=4, padx=5,pady=5)

        self.txt_CajaCompensacion = Label(self.Marco_Registro, text="Caja Compensación", bg="white", font="Barlow 11")
        self.txt_CajaCompensacion.grid(column=2, row=5, padx=5,pady=5)
        self.E_CajaCompensasion = StringVar()
        self.Entrada_CajaCompensacion = Entry(self.Marco_Registro, textvariable=self.E_CajaCompensasion, font="Barlow 10")
        self.Entrada_CajaCompensacion.grid(column=3,row=5, padx=5,pady=5)

     

        self.E_aportesEnLinea = BooleanVar()
        self.Entrada_Aportesenlinea = Checkbutton(self.Marco_Registro, font="Barlow 11",text="Aportes en línea",bg="white",variable=self.E_aportesEnLinea,command=self.Aportes_en_linea)
        self.Entrada_Aportesenlinea.grid(column=3,row=6, columnspan=2)
        

        self.novedad = Label(self.Marco_Registro, text="Comentario", background="white", font="Barlow 11")
        self.novedad.grid(column=2, row=7, padx=5,pady=5)
        
        self.Novedad= Text(self.Marco_Registro, width=18, height=3, font="Barlow 10")
        self.Novedad.grid(column=3, row=7, padx=5,pady=5, rowspan=2)

        self.E_Bus = StringVar()
        self.Bus = Entry (self.marco_Bus, textvariable=self.E_Bus, relief="flat", width=25)
        self.Bus.grid(column=0,row=0, padx=15, pady=5)
        self.Bus.bind("<Return>", self.metodo_Buscar)
        
        
    
    def Botones(self):
        self.BT_Eliminar = Button(self.Marco_BT, text="Eliminar", font="Barlow 11", background="#282e35", foreground="#00d2ff",width=9, state="disabled", command=self.eliminarAF,relief="flat")
        self.BT_Eliminar.grid(column=1, row=0, padx=5)
        self.BT_Eliminar.bind("<Enter>", lambda event:hover_on(event, self.BT_Eliminar))
        self.BT_Eliminar.bind("<Leave>", lambda event:hover_off(event, self.BT_Eliminar))

        self.BT_Actualizar = Button(self.Marco_BT, text="Actualizar", font="Barlow 11", background="#282e35", foreground="#00d2ff",state="disabled", command=self.actualizarAF, width=9, relief="flat")
        self.BT_Actualizar.grid(column=2, row=0, padx=5)
        self.BT_Actualizar.bind("<Enter>", lambda event:hover_on(event, self.BT_Actualizar))
        self.BT_Actualizar.bind("<Leave>", lambda event: hover_off(event, self.BT_Actualizar))
        
        self.nombre_boton = "Registro diario"
        self.BT_Cambiar_tabla = Button(self.marco_Bus,font="barlow 11", text=self.nombre_boton,background="#282e35", relief="flat", foreground="#00d2ff",width=20, command=self.metodo_toggle)
        self.BT_Cambiar_tabla.grid(column=1, row=0, padx=5, pady=3) 
        self.BT_Cambiar_tabla.bind("<Enter>", lambda event:hover_on(event, self.BT_Cambiar_tabla))
        self.BT_Cambiar_tabla.bind("<Leave>", lambda event: hover_off(event, self.BT_Cambiar_tabla))

        self.BT_filtrar_hasta = Button(self.marco_Bus,font="barlow 11", text="Desafiliar", bg="#282e35", relief="flat", foreground="#00d2ff",width=10, command=self.filtro_fecha_Hasta)
        self.BT_filtrar_hasta.grid(column=3, row=0, padx=5, pady=3)
        self.BT_filtrar_hasta.bind("<Enter>", lambda event:hover_on(event, self.BT_filtrar_hasta))
        self.BT_filtrar_hasta.bind("<Leave>", lambda event: hover_off(event, self.BT_filtrar_hasta))

        self.tablaDeNovedad = "Novedades"
        self.BT_revisar_novedades = Button(self.marco_Bus,font="barlow 11", text=self.tablaDeNovedad,background="#282e35", relief="flat", foreground="#00d2ff",width=15, command=self.Mostrar_novedades)
        self.BT_revisar_novedades.grid(column=2, row=0, padx=5, pady=3) 
        self.BT_revisar_novedades.bind("<Enter>", lambda event:hover_on(event, self.BT_revisar_novedades))
        self.BT_revisar_novedades.bind("<Leave>", lambda event: hover_off(event, self.BT_revisar_novedades))


    def tabla(self):
        self.vistaBD = ttk.Treeview(self.marco_tablaBD, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21), show="headings")
        self.BarraV = Scrollbar(self.marco_tablaBD, orient="vertical", command=self.vistaBD.yview)
        self.BarraV.place(rely=0.11, relx=0.97, width=20, height=380)
        self.BarraH = Scrollbar(self.marco_tablaBD, orient="horizontal", command=self.vistaBD.xview)
        self.BarraH.place(rely=0.96, width=620, height=20)
        self.vistaBD.config(xscrollcommand=self.BarraH.set, yscrollcommand=self.BarraV.set)

        self.vistaBD.heading(1, text="ID")
        self.vistaBD.heading(2, text="CASO")
        self.vistaBD.heading(3, text="GESTOR")
        self.vistaBD.heading(4, text="FECHA SOLICITUD")
        self.vistaBD.heading(5, text="NOMBRE Y APELLIDO")
        self.vistaBD.heading(6, text="N° DOCUMENTO")
        self.vistaBD.heading(7, text="TLF")
        self.vistaBD.heading(8, text="DESDE")
        self.vistaBD.heading(9, text="HASTA")
        self.vistaBD.heading(10, text="COSTO-AFL")
        self.vistaBD.heading(11, text="REGIMEN")
        self.vistaBD.heading(12, text="EST-AFL")
        self.vistaBD.heading(13, text="CIUDAD")
        self.vistaBD.heading(14, text="SALARIO")
        self.vistaBD.heading(15, text="ARL")
        self.vistaBD.heading(16, text="EPS")
        self.vistaBD.heading(17, text="PENSION")
        self.vistaBD.heading(18, text="CAJA COMPENSACIÓN")
        self.vistaBD.heading(19, text="APORTES EN lINEA")
        self.vistaBD.heading(20, text="COMENTARIO") 
        self.vistaBD.heading(21, text="HISTORIAL")
        

        self.vistaBD.column(1, anchor="center", width=0)
        self.vistaBD.column(2, anchor="center", width=90)
        self.vistaBD.column(3, anchor="center", width=120)
        self.vistaBD.column(4, anchor="center", width=120)
        self.vistaBD.column(5, anchor="center", width=120)
        self.vistaBD.column(6, anchor="center", width=90)
        self.vistaBD.column(7, anchor="center", width=90)
        self.vistaBD.column(8, anchor="center", width=90)
        self.vistaBD.column(9, anchor="center", width=90)
        self.vistaBD.column(10, anchor="center", width=90)
        self.vistaBD.column(11, anchor="center", width=90)
        self.vistaBD.column(12, anchor="center", width=90)
        self.vistaBD.column(13, anchor="center", width=90)
        self.vistaBD.column(14, anchor="center", width=90)
        self.vistaBD.column(15, anchor="center", width=90)
        self.vistaBD.column(16, anchor="center", width=90)
        self.vistaBD.column(17, anchor="center", width=90)
        self.vistaBD.column(18, anchor="center", width=90)
        self.vistaBD.column(19, anchor="center", width=120)
        self.vistaBD.column(20, anchor="center", width=120)
        self.vistaBD.column(21, anchor="center", width=120)

        self.vistaBD.bind("<ButtonRelease-1>",self.FileSelec)
        self.vistaBD.bind("<Key>",self.volver)
        

    def mostrar_tabla_afiliaciones(self):
        db = conexion()
        elementos = [self.E_Bus.get(),self.E_Bus.get(),self.E_Bus.get(),self.E_Bus.get(),self.E_Bus.get()]
        buscarcaso=db.SearchCaseAF(elementos)
        elemento = db.ShowBDAF()
        if self.E_Bus.get()=="":
            for i in elemento:
                item = self.vistaBD.insert('', 'end',values=i)
        else:
            for i in buscarcaso:
                self.vistaBD.insert('',"end",values=i)
            

        self.vistaBD.place(rely=0.11, width=600, height=380)

    def actualizartabla(self):
        self.vistaBD.delete(*self.vistaBD.get_children())
        self.mostrar_tabla_afiliaciones()


    def actualizarAF(self):
        Aaf = conexion()
        ref = self.id
        arr = [self.E_FAF.get(),self.E_FDF.get(),self.E_CAF.get(),self.E_EST.get().upper(),self.valor_checkButton,self.E_salario.get(), self.E_arl.get().upper(), self.Novedad.get(1.0,END).upper()]
        Aaf.ActualizarAF(arr, ref)
        self.setCjTX()
        self.actualizartabla()
        messagebox.showinfo("Actualizado", "Afiliación actualizada")
    
    def eliminarAF(self):
        bd = conexion()
        arr =[self.E_Caso.get(), self.E_Gestor.get(), self.E_fecha.get()]
        bd.EliminarAF(arr)
        self.setCjTX()
        self.actualizartabla()
        self.BT_Actualizar.config(state="disabled")
        self.BT_Eliminar.config(state="disabled")
        
        messagebox.showinfo("afiliaciones", "afiliación borrada")


    def FileSelec(self,event):
        elemento = self.vistaBD.item(self.vistaBD.focus())
        try:
            self.Novedad.delete(0.0,END)
            self.CAF.delete(0,END)
            self.id = elemento["values"][0]
            self.caso=elemento["values"][1]
            gestor=elemento["values"][2]
            fecha=elemento["values"][3]
            afi=elemento["values"][4]
            nd=elemento["values"][5]
            tlf=elemento["values"][6]
            fa=elemento["values"][7]
            fd=elemento["values"][8]
            caf=elemento["values"][9]
            taf=elemento["values"][10]
            est = elemento["values"][11]
            ciudad = elemento["values"][12]
            salario = elemento["values"][13]
            arl = elemento["values"][14]
            pension = elemento["values"][16]
            eps = elemento["values"][15]
            caja_compensasion = elemento["values"][17]
            
            self.nov = elemento["values"][19]


            self.E_Caso.set(self.caso)
            self.E_Gestor.set(gestor)
            self.E_fecha.set(fecha)
            self.E_Afiliado.set(afi)
            self.E_NCC.set(nd)
            self.E_TLF.set(tlf)
            self.E_FAF.set(fa)
            self.E_FDF.set(fd)
            self.CAF.insert(0,caf)
            self.E_TAF.set(taf)
            self.E_EST.set(est)
            self.E_Ciudad.set(ciudad)
            self.Novedad.insert(END,self.nov)
            self.Slrio.set(salario)
            self.E_arl.set(arl)
            self.E_eps.set(eps)
            self.E_pension.set(pension)
            if elemento["values"][18]:
                self.Entrada_Aportesenlinea.select()
            else:
                self.Entrada_Aportesenlinea.deselect()

            self.E_CajaCompensasion.set(caja_compensasion)
            
            self.mostrarNumSeparadors(self.E_salario,self.Entrada_salario)
            self.mostrarNumSeparadors(self.E_CAF, self.CAF)
            self.BT_Actualizar.config(state="normal")
            self.BT_Eliminar.config(state="normal")
            self.Aportes_en_linea()
            
        except IndexError:
            messagebox.showerror("error","no se ha seleccionado ninguna afiliación")
    
    def setCjTX(self):
        self.E_Caso.set("")
        self.E_Gestor.set("")
        self.E_fecha.set("")
        self.E_Afiliado.set("")
        self.E_NCC.set("")
        self.E_TLF.set("")
        self.E_FAF.set("")
        self.E_FDF.set("")
        self.CAF.delete(0,END)
        self.E_TAF.set("")
        self.E_EST.set("Desafiliado")
        self.E_Ciudad.set("")
        self.Entrada_salario.delete(0,END)
        self.CAF.delete(0,END)
        self.E_arl.set("")
        self.E_eps.set("")
        self.E_pension.set("")
        self.E_CajaCompensasion.set("")
        self.Entrada_Aportesenlinea.deselect()
        self.Novedad.delete(0.0,END)
        
        
        
    def FormatoFecha(self,event,variable):
        if event.char.isdigit():
            texto = variable.get()
            letra = 0
            for i in texto:
                letra +=1
            if letra ==2:
                    variable.insert(2,"/")
            elif letra == 5:
                    variable.insert(5,"/")
        else:
            return "break"
        
    def volver(self, event):
        if event.keysym == 'Escape':
            self.setCjTX()
            self.actualizartabla()
            self.BT_Eliminar.config(state="disabled")
            self.BT_Actualizar.config(state="disabled")
            self.nombre_boton ="Registro diario"
            self.BT_Cambiar_tabla.destroy()
            self.BT_Cambiar_tabla = Button(self.marco_Bus,font="barlow 11", text=self.nombre_boton,background="#282e35", relief="flat", foreground="#00d2ff",width=20, command=self.metodo_toggle)
            self.BT_Cambiar_tabla.grid(column=1, row=0, padx=5, pady=3) 
            self.BT_Cambiar_tabla.bind("<Enter>", lambda event:hover_on(event, self.BT_Cambiar_tabla))
            self.BT_Cambiar_tabla.bind("<Leave>", lambda event: hover_off(event, self.BT_Cambiar_tabla))
            self.BT_Actualizar.config(command=self.actualizarAF)
            self.Bus.config(state="normal")


    def cleartable(self):
        self.vistaBD.delete(*self.vistaBD.get_children())

    def metodo_Buscar(self, event):
        self.cleartable()
        self.mostrar_tabla_afiliaciones()
      

    def validar_caso(self,event):
        bd = conexion()
        validar = bd.validarcaso(self.set_case.get())
        try :
            validar[0][0] == self.E_Caso.get()
            pass
        except IndexError:
            messagebox.showerror("error","el caso no existe")

    def mostrar_tabla_afiliaciones_diarias(self):
        self.vistaBD.delete(*self.vistaBD.get_children())
        db = conexion()
        for i in db.mostrarTablaAfiliacionesDiarias():
            self.vistaBD.insert("","end", values=i)

    
    def actualizar_enviar(self):
        Aaf = conexion()
        db = conexion()
        ref = self.E_Caso.get()
        nombre = self.E_Afiliado.get()
        arr = [self.E_FAF.get(),self.E_FDF.get(),self.E_CAF.get(),self.E_EST.get().upper(),self.valor_checkButton, self.E_salario.get(), self.E_arl.get().upper(), self.Novedad.get(1.0,END).upper()]
        Aaf.ActuarlizarAfiliacionesDiarias(arr,ref,nombre)
        db.enviarAfiliacionesalHistorico(ref,nombre)
        self.setCjTX()
        self.mostrar_tabla_afiliaciones_diarias()
        messagebox.showinfo("Actualizado", "Afiliación actualizada.")

    def metodo_toggle(self):
        if self.nombre_boton == "Registro diario":
            self.mostrar_tabla_afiliaciones_diarias()
            self.nombre_boton = "Historial"
            self.BT_Cambiar_tabla.destroy()
            self.BT_Cambiar_tabla = Button(self.marco_Bus,font="barlow 11", text=self.nombre_boton,background="#282e35", relief="flat", foreground="#00d2ff",width=20, command=self.metodo_toggle)
            self.BT_Cambiar_tabla.grid(column=1, row=0, padx=5, pady=3) 
            self.BT_Cambiar_tabla.bind("<Enter>", lambda event:hover_on(event, self.BT_Cambiar_tabla))
            self.BT_Cambiar_tabla.bind("<Leave>", lambda event: hover_off(event, self.BT_Cambiar_tabla))
            self.BT_Actualizar.config(command=self.actualizar_enviar)
            self.BT_Eliminar.grid_forget()
            self.setCjTX()
            self.BT_Actualizar.config(state="disabled")
            self.Bus.config(state="disabled")
            
        elif self.nombre_boton =="Historial":
            self.actualizartabla()
            self.nombre_boton ="Registro diario"
            self.BT_Cambiar_tabla.destroy()
            self.BT_Cambiar_tabla = Button(self.marco_Bus,font="barlow 11", text=self.nombre_boton,background="#282e35", relief="flat", foreground="#00d2ff",width=20, command=self.metodo_toggle)
            self.BT_Cambiar_tabla.grid(column=1, row=0, padx=5, pady=3) 
            self.BT_Cambiar_tabla.bind("<Enter>", lambda event:hover_on(event, self.BT_Cambiar_tabla))
            self.BT_Cambiar_tabla.bind("<Leave>", lambda event: hover_off(event, self.BT_Cambiar_tabla))
            self.BT_Actualizar.config(command=self.actualizarAF)
            self.BT_Eliminar.grid(column=1, row=0, padx=5)
            self.setCjTX()
            self.BT_Eliminar.config(state="disabled")
            self.BT_Actualizar.config(state="disabled")
            self.Bus.config(state="normal")
            

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

    # metodo para mostrar separadores de mil al seleccionar un caso
    def mostrarNumSeparadors(self, num,variable):
        
            numero = float(variable.get())
            numero_formateado = "{:,}".format(numero)
            variable.delete(0, END)
            variable.insert(0, numero_formateado)
            num.set(numero)
    def Mostrar_novedades(self):
        if self.tablaDeNovedad == "Novedades":
            
            db = conexion()
            BaseDeDatosNovedades = db.Mostrar_BD_Novedades()
            self.cleartable()
            self.setCjTX()
            for i in BaseDeDatosNovedades:
                self.vistaBD.insert("","end",values=i)
            self.BT_Actualizar.config(text="Anular",command=self.novedad_reportada, state="disabled")
            self.BT_Eliminar.grid_forget()
            self.BT_Cambiar_tabla.config(state="disabled")
            self.tablaDeNovedad = "Volver"
            self.BT_revisar_novedades.config(text=self.tablaDeNovedad)
            self.Bus.config(state="disabled")

        elif self.tablaDeNovedad =="Volver":
            self.setCjTX()
            self.actualizartabla()
            self.tablaDeNovedad = "Novedades"
            self.nombre_boton = "Registro diario"
            self.BT_Cambiar_tabla.config(text=self.nombre_boton)
            self.BT_revisar_novedades.config(text=self.tablaDeNovedad)
            self.BT_Eliminar.grid(column=1, row=0, padx=5)
            self.BT_Actualizar.config(text="Actualizar",command=self.actualizarAF, state="disabled")
            self.BT_Eliminar.config(state="disabled")
            self.BT_Cambiar_tabla.config(state="normal")
            self.Bus.config(state="normal")
            
            
           

    def novedad_reportada(self):
        db = conexion()
        db1 = conexion()
        db2 = conexion()
        refe = [self.E_Caso.get(), self.E_fecha.get(), self.E_Afiliado.get(), self.E_Gestor.get()]
        db.anular_afiliacion(refe)
        db1.anular_afiliacion_tabla(refe)
        self.vistaBD.delete(*self.vistaBD.get_children())
        messagebox.showinfo("Anulación", "Afiliación anulada con exito")
        for i in db2.Mostrar_BD_Novedades():
            self.vistaBD.insert("","end", values=i)
        self.setCjTX()

    def Aportes_en_linea(self):
        if self.E_aportesEnLinea.get():
            self.valor_checkButton = "OK"
        else:
            self.valor_checkButton = ""

    def filtro_fecha_Hasta(self):
        db = conexion()
        lista = db.filtro_fecha_desafiliacion()
        self.cleartable()
        for i in lista:
            self.vistaBD.insert("","end",values=i)
        self.setCjTX()
        self.BT_Actualizar.config(state="disabled")
        self.BT_Eliminar.config(state="disabled")
        


    

    
