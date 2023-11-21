from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Data_Base import *
from datetime import *
from funciones import *
class novedades:
       
    def __init__(self):
            
            self.VentanaNovedad = Tk()
            self.VentanaNovedad.title("Scrum Manager | Registro de afiliaciones")
            self.VentanaNovedad.geometry(self.definir_medidas())
            self.VentanaNovedad.resizable(0,0)
            self.VentanaNovedad.config(bg="white")
            self.VentanaNovedad.iconbitmap("./icon.ico")
            self.novedades()
            self.mostrarDataBase()
            self.VentanaNovedad.mainloop()

    def definir_medidas(self):
        ancho_pantalla = self.VentanaNovedad.winfo_screenwidth()
        alto_pantalla = self.VentanaNovedad.winfo_screenheight()
        ancho_ventana = 875
        alto_ventana = 485
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla - (alto_ventana + 20)) // 2
        
        return f"{ancho_ventana}x{alto_ventana}+{x}+{y}"

    def novedades(self):
            self.marco_general = Frame(self.VentanaNovedad, bg="white")
            self.marco_general.pack()
            self.Novedad = Label(self.marco_general, text="Buscar", background="white", font="Barlow 13", bg="white")
            self.Novedad.grid(column=0,row=0, sticky=(W), pady=10)
            
            self.E_buscadoraf = StringVar()
            self.buscador = Entry(self.marco_general,textvariable=self.E_buscadoraf, font="Barlow 11", bd=1, width=28)
            self.buscador.grid(column=0, row=0, padx=60, sticky=(W))
            self.buscador.bind("<Return>", self.buscar_afiliciones_gestor)
            self.buscador.bind("<Key>", self.scape)

            self.txtNewNovedad = Label(self.marco_general, text="escribe la novedad", background="white", font="Barlow 11", bg="white")
            self.txtNewNovedad.grid(column=0,row=2,sticky=(W), padx=5)
            self.novedad = Text(self.marco_general, width=48, height=2)
            self.novedad.grid(column=0,row=3, pady=2, padx=5, sticky=(W))
            
            self.marco = Frame(self.marco_general, width=600, height=305, bg="white")
            self.marco.grid(column=0,row=1, columnspan=2)

            self.BT_Enviar_Novedad = Button(self.marco_general, text="Enviar",relief="flat", font="Barlow 11 bold", fg="#00d2ff", bg="#282e35", command= self.enviarN, state="disabled")
            self.BT_Enviar_Novedad.grid(column=1,row=3)
            self.BT_Enviar_Novedad.bind("<Enter>", lambda event: hover_on(event, self.BT_Enviar_Novedad) )
            self.BT_Enviar_Novedad.bind("<Leave>", lambda event: hover_off(event, self.BT_Enviar_Novedad))

            self.tablaNovedades = ttk.Treeview(self.marco, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20), show="headings")
            BarraV = Scrollbar(self.marco, orient="vertical", command=self.tablaNovedades.yview)
            BarraV.place(relx=0.97, width=20, height=340)
            BarraH = Scrollbar(self.marco, orient="horizontal", command=self.tablaNovedades.xview)
            BarraH.place(rely=0.935, width=585, height=20)
            self.tablaNovedades.config(xscrollcommand=BarraH.set, yscrollcommand=BarraV.set)

            style = ttk.Style()
            style.configure("Treeview", background = "#DEE9F4")
            style.theme_use("vista")
            style.map("Treeview", background = [("selected","#213842")], foreground = [("selected","#00EFE8")])
    
            self.tablaNovedades.heading(1, text="ID")
            self.tablaNovedades.heading(2, text="CASO")
            self.tablaNovedades.heading(3, text="GESTOR")
            self.tablaNovedades.heading(4, text="FECHA SOLICITUD")
            self.tablaNovedades.heading(5, text="NOMBRE Y APELLIDO")
            self.tablaNovedades.heading(6, text="N° DOCUMENTO")
            self.tablaNovedades.heading(7, text="TLF")
            self.tablaNovedades.heading(8, text="DESDE")
            self.tablaNovedades.heading(9, text="HASTA")
            self.tablaNovedades.heading(10, text="COSTO-AFL")
            self.tablaNovedades.heading(11, text="REGIMEN")
            self.tablaNovedades.heading(12, text="EST-AFL")
            self.tablaNovedades.heading(13, text="CIUDAD")
            self.tablaNovedades.heading(14, text="SALARIO")
            self.tablaNovedades.heading(15, text="ARL")
            self.tablaNovedades.heading(16, text="PENSION")
            self.tablaNovedades.heading(17, text="CAJA COMPENSACIÓN")
            self.tablaNovedades.heading(18, text="APORTES EN lINEA")
            self.tablaNovedades.heading(19, text="NOVEDAD") 
            self.tablaNovedades.heading(20, text="HISTORIAL")


            self.tablaNovedades.column(1, anchor="center", width=0)
            self.tablaNovedades.column(2, anchor="center", width=90)
            self.tablaNovedades.column(3, anchor="center", width=120)
            self.tablaNovedades.column(4, anchor="center", width=120)
            self.tablaNovedades.column(5, anchor="center", width=120)
            self.tablaNovedades.column(6, anchor="center", width=90)
            self.tablaNovedades.column(7, anchor="center", width=90)
            self.tablaNovedades.column(8, anchor="center", width=90)
            self.tablaNovedades.column(9, anchor="center", width=90)
            self.tablaNovedades.column(10, anchor="center", width=90)
            self.tablaNovedades.column(11, anchor="center", width=90)
            self.tablaNovedades.column(12, anchor="center", width=90)
            self.tablaNovedades.column(13, anchor="center", width=90)
            self.tablaNovedades.column(14, anchor="center", width=90)
            self.tablaNovedades.column(15, anchor="center", width=90)
            self.tablaNovedades.column(16, anchor="center", width=90)
            self.tablaNovedades.column(17, anchor="center", width=90)
            self.tablaNovedades.column(18, anchor="center", width=90)
            self.tablaNovedades.column(19, anchor="center", width=120)
            self.tablaNovedades.column(20, anchor="center", width=120)
            

            self.tablaNovedades.place(width=600, height=305)
            #evento
            self.tablaNovedades.bind("<ButtonRelease-1>", self.getrow)
            self.tablaNovedades.bind("<Key>",self.scape)

            
    def mostrarDataBase(self):
            db = conexion()
            elemento = db.ShowBDAF()
            for i in elemento:
                self.tablaNovedades.insert('','end',values=i)
            
            

    def enviarN(self):
        if self.novedad.get(1.0, 'end-1c')=="":  
            messagebox.showerror("Error", "No existe ninguna novedad")
        else:
            
            arr = [self.caso,
                    self.gestor,
                    self.fecha, 
                    self.tecnico,
                    self.cedula,
                    self.tlf,
                    self.desde,
                    self.hasta,
                    self.costo_afiliacion,
                    self.regimen,
                    self.estado_afiliacion,
                    self.ciudad,
                    self.sueldo,
                    self.arl,
                    self.eps,
                    self.pension,
                    self.caja_compensacion,
                    self.aporte_en_Linea,
                    self.historial]
            novedad = self.novedad.get(1.0,'end')

            db = conexion()    
            db.novedades(novedad,arr)
            self.VentanaNovedad.destroy()
            messagebox.showinfo("Novedad","el mensaje se envio correctamente")
            
        

    
    def getrow(self, event):
        try:
            elemento = self.tablaNovedades.item(self.tablaNovedades.focus())
            self.caso = elemento["values"][1]
            self.gestor = elemento["values"][2]
            self.fecha = elemento["values"][3]
            self.tecnico = elemento["values"][4]
            self.cedula = elemento["values"][5]
            self.tlf = elemento["values"][6]
            self.desde = elemento["values"][7]
            self.hasta = elemento["values"][8]
            self.costo_afiliacion = elemento["values"][9]
            self.regimen = elemento["values"][10]
            self.estado_afiliacion = elemento["values"][11]
            self.ciudad = elemento["values"][12]
            self.sueldo = elemento["values"][13]
            self.arl = elemento["values"][14]
            self.eps= elemento["values"][15]
            self.pension = elemento["values"][16]
            self.caja_compensacion = elemento["values"][17]
            self.aporte_en_Linea = elemento ["values"][18]
            self.historial = elemento["values"][20]
        
            self.BT_Enviar_Novedad.config(state="normal")

        except IndexError:
                 messagebox.showerror("","seleccione un caso ")

    def buscar_afiliciones_gestor(self, event):
        self.tablaNovedades.delete(*self.tablaNovedades.get_children())
        db = conexion()
        ref = [self.buscador.get(),self.buscador.get(),self.buscador.get(),self.buscador.get(),self.buscador.get()]
        elemento = db.SearchCaseAF(ref)
        for i in elemento:
            self.tablaNovedades.insert('','end',values=i)

    def scape(self, event):
          if event.keysym == "Escape":
                self.tablaNovedades.delete(*self.tablaNovedades.get_children())
                self.mostrarDataBase()
                self.E_buscadoraf.set("")
