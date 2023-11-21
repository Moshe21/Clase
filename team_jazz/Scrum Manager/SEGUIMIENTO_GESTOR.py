from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Data_Base import *
from ExportarExecel import*
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from INFO_CASO import *
from idlelib.tooltip import Hovertip
from funciones import *



class Gestor:
    def __init__(self,user,master, ventana):
        self.ven = ventana
        self.user = user
        self.vacio = ["","","","","","","","","","","","",""]
        self.Windows = master
        self.Frame()
        self.LabelsAndEntrys()
        self.FallowUpView()
       
        self.E_PUB = StringVar()
        self.E_PUB.set("1")
        self.E_CO = StringVar()
        self.E_CO.set("1")
        self.buttons()
        self.funcionnrocasos()
        self.actualizarGrafica()
        self.showDataBase(self.vacio)
        
        
#______________________________________contenedores de los widgets___________________________________________________
    def Frame(self):
        self.ven.bind("<Key>",self.Restart)
        #contenedor general de todos los contenedores para mostrarlo centrado en la raiz
        self.Frame_General = Frame(self.Windows, background="white")
        self.Frame_General.pack()
        #etiqueta para encabezado del modulo
       

        self.Titulo=Label(self.Frame_General, text=self.user.capitalize(), font="barlow 28 ", bg="#282e35", foreground="white")
        self.Titulo.grid(column=0,row=0)

    
        # contenedor de los widgets que se usan para visualizar o ingresar nuevos casos
        self.Frame_registro = LabelFrame(self.Frame_General,bg="white")
        self.Frame_registro.grid(column=0,row=1, sticky=(N))     

        #contenedor de tabla de navegacion de casos
        self.Frame_Table = LabelFrame(self.Frame_General, width=655,height=413, bg="white")
        self.Frame_Table.grid(column=1,row=1, sticky=(N), padx=3)
        
        #contenedore del buscador o filtros
        self.BarDate = Frame(self.Frame_Table, background="#282e35")
        self.BarDate.place(width=650, height=50)

        #contenedor de botones de acción
        self.Frame_Botones = Frame(self.Frame_registro, bg="white")
        self.Frame_Botones.grid(column=0, row=12, pady=15, columnspan=4)

   
#__________funcion para crear los widgets de ingreso de datos (cajas de textos), etiquetas para identificarlos___________
                                        # y variables ligadas a las cajas de textos
    def LabelsAndEntrys(self):
        db = conexion()

  
        self.txtcaso=Label(self.Frame_registro, text="CASO", font="barlow 11 ", bg="white")
        self.txtcaso.grid(column=0, row=0, padx=5, pady=5)
        self.E_Caso = StringVar()
        self.Caso=Entry(self.Frame_registro, textvariable=self.E_Caso, font="barlow 11", state="readonly")
        self.Caso.grid(column=1, row=0, padx=5, pady=5)

        self.txtEM=Label(self.Frame_registro, text="REF", font="barlow 11 ", bg="white")
        self.txtEM.grid(column=0, row=1, padx=5, pady=5)
        self.EM = StringVar()
        self.Em=Entry(self.Frame_registro, textvariable=self.EM, font="barlow 11")
        self.Em.grid(column=1, row=1, padx=5, pady=5)

        self.txtfecha=Label(self.Frame_registro, text="FECHA", font="barlow 11 ", bg="white")
        self.txtfecha.grid(column=0, row=2, padx=5, pady=5)
        self.E_Fecha = StringVar()
        self.Fecha=Entry(self.Frame_registro, textvariable=self.E_Fecha, font="barlow 11", state="readonly")
        self.Fecha.grid(column=1, row=2, padx=5, pady=5)
        self.Fecha.bind("<Key>", lambda event:self.FormatoFecha(event,self.Fecha))
        self.Fecha.bind("<BackSpace>", lambda _: self.Fecha.delete(END))
        
        self.txtcliente=Label(self.Frame_registro, text="CLIENTE", font="barlow 11 ", bg="white")
        self.txtcliente.grid(column=0, row=3, padx=5, pady=5)
        self.E_Cliente = StringVar()
        self.Cliente=Entry(self.Frame_registro, textvariable=self.E_Cliente, font="barlow 11", state="readonly")
        self.Cliente.grid(column=1, row=3, padx=5, pady=5)

        self.txtdenominacion=Label(self.Frame_registro, text="DENOMINACIÓN", font="barlow 11 ", bg="white")
        self.txtdenominacion.grid(column=0, row=4, padx=5, pady=5)
        self.E_Denominacion = StringVar()
        self.Denominacion=Entry(self.Frame_registro, textvariable=self.E_Denominacion, font="barlow 11", state="readonly")
        self.Denominacion.grid(column=1, row=4, padx=5, pady=5)

        self.txtciudad_sede=Label(self.Frame_registro, text="CIUDAD O SEDE", font="barlow 11 ", bg="white")
        self.txtciudad_sede.grid(column=0, row=5, padx=5, pady=5)
        self.E_Ciudad_Sede = StringVar()
        self.Ciudad_Sede=Entry(self.Frame_registro, textvariable=self.E_Ciudad_Sede, font="barlow 11", state="readonly")
        self.Ciudad_Sede.grid(column=1, row=5)

        self.txtterritorial=Label(self.Frame_registro, text="TERRITORIAL", font="barlow 11 ", bg="white")
        self.txtterritorial.grid(column=0, row=6, padx=5, pady=5)
        self.E_Territorial = StringVar()
        self.Territorial=Entry(self.Frame_registro, textvariable=self.E_Territorial, font="barlow 11", state="readonly")
        self.Territorial.grid(column=1, row=6, padx=5, pady=5)

        self.estadorcc = ["EN PROCESO DE EJECUCIÓN", "DESASIGNADO"]
        self.txtestado=Label(self.Frame_registro, text="ESTADO RCC", font="barlow 11 ", bg="white")
        self.txtestado.grid(column=0, row=7, padx=5, pady=5)
        self.E_Estado = StringVar()
        self.Estado=ttk.Combobox(self.Frame_registro, textvariable=self.E_Estado, values=self.estadorcc,font="barlow 11", width=17)
        self.Estado.grid(column=1, row=7, padx=5, pady=5)
        

        self.txtestadoSAP=Label(self.Frame_registro, text="ESTADO", font="barlow 11 ", bg="white")
        self.txtestadoSAP.grid(column=0, row=8, padx=5, pady=5)
        self.E_EstadoSAP = StringVar()
        estadosDeSap = db.EstadoSap()
        self.EstadoSAP=ttk.Combobox(self.Frame_registro, textvariable=self.E_EstadoSAP, values=estadosDeSap,font="barlow 11", width=17)
        self.EstadoSAP.grid(column=1, row=8, padx=5, pady=5)
        self.EstadoSAP.bind("<FocusOut>", self.validar_estado_rcc)

        self.txtgestor=Label(self.Frame_registro, text="GESTOR", font="barlow 11 ", bg="white")
        self.txtgestor.grid(column=0, row=9, padx=5, pady=5)
        self.E_Gestor = StringVar()
        self.Ngestores =db.nombre_de_gestores()
        self.Gestor= ttk.Combobox(self.Frame_registro, textvariable=self.E_Gestor, values=self.Ngestores, width=17, font="barlow 11", state="disabled")
        self.Gestor.grid(column=1, row=9, padx=5, pady=5)

        self.txtcomentario=Label(self.Frame_registro, text="COMENTARIO", font="barlow 11 ", bg="white")
        self.txtcomentario.grid(column=0, row=10)
        self.E_Comentario = StringVar()
        self.Comentario=Entry(self.Frame_registro, textvariable=self.E_Comentario, font="barlow 11")
        self.Comentario.grid(column=1, row=10, padx=5, pady=5)

        self.txtsintoma=Label(self.Frame_registro, text="SÍNTOMA", font="barlow 11 ", bg="white")
        self.txtsintoma.grid(column=0, row=11, sticky=(N))
        self.E_Sintoma = StringVar()
        self.Sintoma=Entry(self.Frame_registro, textvariable=self.E_Sintoma, font="barlow 11", state="readonly")
        self.Sintoma.grid(column=1, row=11, padx=5, pady=5,sticky=(N))

        self.txttecnico=Label(self.Frame_registro, text="TÉCNICO", font="barlow 11 ", bg="white")
        self.txttecnico.grid(column=2, row=0, padx=5, pady=5, sticky=(N))
        self.opciones = db.lista_de_nombresTC()
        self.E_Tecnico = StringVar()
        self.Tecnico=Entry(self.Frame_registro, textvariable=self.E_Tecnico, font="barlow 11")
        self.Tecnico.grid(column=3, row=0, padx=5, pady=5, sticky=(N))
        self.Tecnico.bind("<KeyRelease>", self.autocompletar)
        self.Tecnico.bind("<FocusOut>", lambda event: self.lista_sugerencia.place_forget())


        self.txtmano_obra=Label(self.Frame_registro, text="MANO DE OBRA", font="barlow 11 ", bg="white")
        self.txtmano_obra.grid(column=2, row=1, padx=5, pady=5)
        self.E_Mano_Obra = IntVar()
        self.E_Mano_Obra.set(1)
        self.MO = DoubleVar()
        self.MO.set(1)
        self.Mano_Obra=Entry(self.Frame_registro, textvariable=self.E_Mano_Obra, font="barlow 11")
        self.Mano_Obra.grid(column=3, row=1, padx=5, pady=5)
        self.Mano_Obra.bind("<FocusOut>", lambda event:self.validarseparadores(event,self.MO,self.Mano_Obra))
        self.Mano_Obra.bind("<Key>", self.ValidarValorNumerico)
        self.Mano_Obra.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.Mano_Obra))

        self.txtmateriales=Label(self.Frame_registro, text="MATERIALES", font="barlow 11 ", bg="white")
        self.txtmateriales.grid(column=2, row=2, padx=5, pady=5)
        self.E_Materiales = IntVar()
        self.E_Materiales.set(1)
        self.Mt = DoubleVar()
        self.Mt.set(1)
        self.Materiales=Entry(self.Frame_registro, textvariable=self.E_Materiales, font="barlow 11")
        self.Materiales.grid(column=3, row=2, padx=5, pady=5)
        self.Materiales.bind("<FocusOut>", lambda event:self.validarseparadores(event,self.Mt,self.Materiales))
        self.Materiales.bind("<Key>",self.ValidarValorNumerico)
        self.Materiales.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.Materiales))

        self.txtparafiscales=Label(self.Frame_registro, text="PARAFISCALES", font="barlow 11 ", bg="white")
        self.txtparafiscales.grid(column=2, row=3, padx=5, pady=5)
        self.E_Parafiscales = IntVar()
        self.E_Parafiscales.set(1)
        self.P = DoubleVar()
        self.P.set(1)
        self.Parafiscales=Entry(self.Frame_registro, textvariable=self.E_Parafiscales, font="barlow 11")
        self.Parafiscales.grid(column=3, row=3, padx=5, pady=5)
        self.Parafiscales.bind("<FocusOut>", lambda event:self.validarseparadores(event,self.P,self.Parafiscales))
        self.Parafiscales.bind("<Key>",self.ValidarValorNumerico)
        self.Parafiscales.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.Parafiscales))

        self.txtsub_total=Label(self.Frame_registro, text="SUB-TOTAL", font="barlow 11 ", bg="white")
        self.txtsub_total.grid(column=2, row=4, padx=5, pady=5)
        self.E_Sub_Total = IntVar()
        self.E_Sub_Total.set(1)
        self.ST = DoubleVar()
        self.ST.set(1)
        self.Sub_Total=Entry(self.Frame_registro, textvariable=self.E_Sub_Total, font="barlow 11")
        self.Sub_Total.grid(column=3, row=4, padx=5, pady=5)
        self.Sub_Total.bind("<FocusOut>", lambda event:self.validarseparadores(event, self.ST,self.Sub_Total))
        self.Sub_Total.bind("<Key>",self.ValidarValorNumerico)
        self.Sub_Total.bind("<FocusIn>", lambda event: self.vaciar_entry(event, self.Sub_Total))

        self.txtoc=Label(self.Frame_registro, text="OC", font="barlow 11 ", bg="white")
        self.txtoc.grid(column=2, row=5, padx=5, pady=5)
        self.txtoc.grid_forget()
        self.E_Oc = StringVar()
        self.Oc=Entry(self.Frame_registro, textvariable=self.E_Oc, font="barlow 11", state="readonly")
        self.Oc.grid(column=3, row=5, padx=5, pady=5)
        self.Oc.grid_forget()

        self.txtocf=Label(self.Frame_registro, text="OC FÍSICA", font="barlow 11 ", bg="white")
        self.txtocf.grid(column=2, row=5, padx=5, pady=5)
        self.E_OcF = StringVar()
        self.Ocf=Entry(self.Frame_registro, textvariable=self.E_OcF, font="barlow 11", state="readonly")
        self.Ocf.grid(column=3, row=5, padx=5, pady=5)


        self.txtfchini=Label(self.Frame_registro, text="FECHA INICIO ", font="barlow 11 ", bg="white")
        self.txtfchini.grid(column=2, row=6)
        self.E_FCini = StringVar()
        self.fcini=Entry(self.Frame_registro, textvariable=self.E_FCini, font="barlow 11")
        self.fcini.grid(column=3, row=6, padx=5, pady=5)
        self.fcini.bind("<Key>", lambda event:self.FormatoFecha(event,self.fcini))
        self.fcini.bind("<BackSpace>", lambda _: self.fcini.delete(END))

        self.txtfchfinal=Label(self.Frame_registro, text="FECHA FINAL", font="barlow 11 ", bg="white")
        self.txtfchfinal.grid(column=2, row=7)
        self.E_FCfinal = StringVar()
        self.fcfinal=Entry(self.Frame_registro, textvariable=self.E_FCfinal, font="barlow 11")
        self.fcfinal.grid(column=3, row=7, padx=5, pady=5)
        self.fcfinal.bind("<Key>", lambda event:self.FormatoFecha(event,self.fcfinal))
        self.fcfinal.bind("<BackSpace>", lambda _: self.fcfinal.delete(END))

        self.txtFV=Label(self.Frame_registro, text="FACTURA VENTA", font="barlow 11 ", bg="white")
        self.txtFV.grid(column=2, row=8)
        self.E_FV = StringVar()
        self.FV=Entry(self.Frame_registro, textvariable=self.E_FV, font="barlow 11", state="readonly")
        self.FV.grid(column=3, row=8, padx=5, pady=5)

        self.txtFCF=Label(self.Frame_registro, text="FECHA FACTURADO", font="barlow 11 ", bg="white")
        self.txtFCF.grid(column=2, row=9)
        self.E_FCF = StringVar()
        self.FCF=Entry(self.Frame_registro, textvariable=self.E_FCF, font="barlow 11", state="readonly")
        self.FCF.grid(column=3, row=9, padx=5, pady=5)
        self.FCF.bind("<Key>", lambda event:self.FormatoFecha(event,self.FCF))
        self.FCF.bind("<BackSpace>", lambda _: self.FCF.delete(END))

        self.lista_sugerencia = Listbox(self.Frame_registro, relief="flat")
        self.lista_sugerencia.bind("<<ListboxSelect>>", self.seleccionar_sugerencia)


        
        self.E_Search = StringVar()
        self.E_Search.set("")
        self.txtBuscar = Label(self.BarDate, text="Buscar", font="Barlow 11", bg="#282e35", foreground="white")
        self.txtBuscar.grid(column=0,row=0,padx=10, pady=10)
        self.Search = Entry(self.BarDate, textvariable=self.E_Search, width=25, relief="flat", font="barlow 11")
        self.Search.grid(column=1,row=0, padx=10, pady=10)    
        self.Search.bind("<Return>",self.Busacador)  

        self.txtporcentaje = Label(self.Frame_registro, font="barlow 15 bold", bg="white", foreground="#2EAD00")
        self.txtutilidadBruta = Label(self.Frame_registro, font="barlow 11 bold", bg="white", text="UTILIDAD BRUTA")
        self.txtutilidadBruta.grid(column=2, row=11, padx=5, pady=5)
#________________________________________________tabla de seguimiento____________________________________________________________
    def FallowUpView(self):
        self.Table_View = ttk.Treeview(self.Frame_Table, show="headings", columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37))
        self.ScrollV = Scrollbar(self.Frame_Table, orient="vertical",command=self.Table_View.yview)
        self.ScrollV.place(relx=0.976, rely=0.12, width=15, height=343)
        self.ScrollH = Scrollbar(self.Frame_Table, orient="horizontal", command=self.Table_View.xview)
        self.ScrollH.place(rely=0.960, width=650, height=15)
        self.Table_View.config(xscrollcommand=self.ScrollH.set, yscrollcommand=self.ScrollV.set)

        style = ttk.Style()
        style.configure("Treeview", background = "#DEE9F4", font="barlow 11")
        style.theme_use("vista")
        style.map("Treeview", background = [("selected","#213842")], foreground = [("selected","#00EFE8")])

        self.Table_View.heading(1, text="CASO")
        self.Table_View.heading(2, text="FECHA")
        self.Table_View.heading(3, text="MES")
        self.Table_View.heading(4, text="AÑO")
        self.Table_View.heading(5, text="CLIENTE")
        self.Table_View.heading(6, text="DENOMINACIÓN")
        self.Table_View.heading(7, text="CIUDAD O SEDE")
        self.Table_View.heading(8, text="TERRITORIAL")
        self.Table_View.heading(9, text="ESTADO RCC")
        self.Table_View.heading(10, text="OC")
        self.Table_View.heading(11, text="OC FÍSICA")
        self.Table_View.heading(12, text="REF")
        self.Table_View.heading(13, text="ESTADO_SAP")
        self.Table_View.heading(14, text="GESTOR")
        self.Table_View.heading(15, text="COMENTARIO")
        self.Table_View.heading(16, text="SÍNTOMA")
        self.Table_View.heading(17, text="TÉCNICO")
        self.Table_View.heading(18, text="FECHA INICIO EJE")
        self.Table_View.heading(19, text="FECHA FINALIZADO EJE")
        self.Table_View.heading(20, text="MANO DE OBRA")
        self.Table_View.heading(21, text="MATERIALES")
        self.Table_View.heading(22, text="PARAFISCALES")
        self.Table_View.heading(23, text="TOTAL")
        self.Table_View.heading(24, text="SUBTOTAL")
        self.Table_View.heading(25, text="IVA")
        self.Table_View.heading(26, text="TOTAL CON IVA")
        self.Table_View.heading(27, text="COMISION A OTROS")
        self.Table_View.heading(28, text="UTILIDAD BRUTA")
        self.Table_View.heading(29, text="% U.B")
        self.Table_View.heading(30, text="RTE FUENTE")
        self.Table_View.heading(31, text="RTE IVA")
        self.Table_View.heading(32, text="RTE ICA")
        self.Table_View.heading(33, text="PAGO FINAL")
        self.Table_View.heading(34, text="UTILIDAD NETA")
        self.Table_View.heading(35, text="% U.N")
        self.Table_View.heading(36, text="FACTURA VENTA")
        self.Table_View.heading(37, text="FECHA FACTURADO")

        self.Table_View.column(1, anchor="center", width=120)
        self.Table_View.column(2, anchor="center", width=120)
        self.Table_View.column(3, anchor="center", width=120)
        self.Table_View.column(4, anchor="center", width=120)
        self.Table_View.column(5, anchor="center", width=120)
        self.Table_View.column(6, anchor="center", width=120)
        self.Table_View.column(7, anchor="center", width=120)
        self.Table_View.column(8, anchor="center", width=120)
        self.Table_View.column(9, anchor="center", width=120)
        self.Table_View.column(10, anchor="center", width=120)
        self.Table_View.column(11, anchor="center", width=120)
        self.Table_View.column(12, anchor="center", width=120)
        self.Table_View.column(13, anchor="center", width=120)
        self.Table_View.column(14, anchor="center", width=120)
        self.Table_View.column(15, anchor="center", width=120)
        self.Table_View.column(16, anchor="center", width=120)
        self.Table_View.column(17, anchor="center", width=120)
        self.Table_View.column(18, anchor="center", width=120)
        self.Table_View.column(19, anchor="center", width=120)
        self.Table_View.column(20, anchor="center", width=120)
        self.Table_View.column(21, anchor="center", width=120)
        self.Table_View.column(22, anchor="center", width=120)
        self.Table_View.column(23, anchor="center", width=120)
        self.Table_View.column(24, anchor="center", width=120)
        self.Table_View.column(25, anchor="center", width=120)
        self.Table_View.column(26, anchor="center", width=120)
        self.Table_View.column(27, anchor="center", width=120)
        self.Table_View.column(28, anchor="center", width=120)
        self.Table_View.column(29, anchor="center", width=120)
        self.Table_View.column(30, anchor="center", width=120)
        self.Table_View.column(31, anchor="center", width=120)
        self.Table_View.column(32, anchor="center", width=120)
        self.Table_View.column(33, anchor="center", width=120)
        self.Table_View.column(34, anchor="center", width=120)
        self.Table_View.column(35, anchor="center", width=120)
        self.Table_View.column(36, anchor="center", width=120)
        self.Table_View.column(37, anchor="center", width=120)

        self.Table_View.place(rely=0.12, width=635,height=343)
        #__________________________eventos del seguimineto_________________________________
        self.Table_View.bind("<ButtonRelease-1>", self.GetRow)
        
        self.Table_View.bind("<Double-Button-1>", self.CostoCaso)
#_________________________________________________________botones de accion________________________________________________________
    def buttons(self):
        self.BT_Actualizar = Button (self.Frame_Botones, text="Actualizar", relief="flat", bg="#282e35",  font="barlow 10", width=12, foreground="#00d2ff",activebackground="#282e35",state="disabled", command=self.UpDate)
        self.BT_Actualizar.grid(column=0,row=0)
        self.BT_Actualizar.bind("<Enter>", lambda event: hover_on(event, self.BT_Actualizar) )
        self.BT_Actualizar.bind("<Leave>", lambda event: hover_off(event, self.BT_Actualizar))

        self.BT_exportar_base_datos = Button (self.BarDate, text="Exportar Excel", relief="flat", bg="#282e35", font="barlow 10", width=12, foreground="#00d2ff",activebackground="#282e35", command=self.exportar)
        self.BT_exportar_base_datos.grid(column=5,row=0, padx=20)
        self.BT_exportar_base_datos.bind("<Enter>", lambda event: hover_on(event, self.BT_exportar_base_datos) )
        self.BT_exportar_base_datos.bind("<Leave>", lambda event: hover_off(event, self.BT_exportar_base_datos))

        
#________________metodos bakend del sistema _______________________________________________________________________   
    def ClearTable(self):
        self.Table_View.delete(*self.Table_View.get_children())
    # metodo para mostrar los datos del caso seleccionado en los entrys
    def GetRow(self, event):
        elementos = self.Table_View.item(self.Table_View.focus())
        try:
                self.ot=elementos["values"][0]
                fecha=elementos["values"][1]
                cliente=elementos["values"][4]
                denominacion=elementos["values"][5]
                ciudasede=elementos["values"][6]
                territorial=elementos["values"][7]
                estado=elementos["values"][8]
                oc = elementos["values"][9]
                ocf = elementos["values"][10]
                em = elementos["values"][11]
                essap = elementos["values"][12]
                gestor=elementos["values"][13]
                comentario=elementos["values"][14]
                sint = elementos ["values"][15]
                tecnico=elementos["values"][16]
                fechini = elementos["values"][17]
                fecfini = elementos["values"][18]
                manoobra=elementos["values"][19]
                materiales=elementos["values"][20]
                parafiscales=elementos["values"][21]
                self.costo_total = elementos["values"][22]
                sub_total=elementos["values"][23]
                self.comision_otros =elementos["values"][26]
                self.ub = elementos["values"][27]
                fv = elementos["values"][35]
                fcfv=elementos["values"][36]

                
                self.BT_Actualizar.config(state="normal")
                
                self.E_Caso.set(self.ot)
                self.E_Fecha.set(fecha)
                self.E_Cliente.set(cliente)
                self.E_Denominacion.set(denominacion)
                self.E_Ciudad_Sede.set(ciudasede)
                self.E_Territorial.set(territorial)
                self.E_Estado.set(estado)
                self.E_Gestor.set(gestor)
                self.E_Comentario.set(comentario)
                self.E_Tecnico.set(tecnico)
                self.E_Mano_Obra.set(manoobra)
                self.E_Materiales.set(materiales)
                self.E_Parafiscales.set(parafiscales)
                self.E_Sub_Total.set(sub_total)
                self.E_Oc.set(oc)
                self.E_OcF.set(ocf)
                self.EM.set(em)
                self.E_Sintoma.set(sint)
                self.E_FCini.set(fechini)
                self.E_FCfinal.set(fecfini)
                self.E_EstadoSAP.set(essap)
                self.E_FV.set(fv)
                self.E_FCF.set(fcfv)
                self.E_PUB.set(self.ub)
                self.E_CO.set(self.comision_otros)
                self.actualizarGrafica()
                self.mostrarNumSeparadors(self.MO,self.Mano_Obra)
                self.mostrarNumSeparadors(self.Mt,self.Materiales)
                self.mostrarNumSeparadors(self.P,self.Parafiscales)
                self.mostrarNumSeparadors(self.ST,self.Sub_Total)
                Hovertip(self.Comentario,self.E_Comentario.get())
                self.validar_estado_rcc("")

        except IndexError:
                 messagebox.showerror("","seleccione un caso")
    
    # metodo para actualizar caso
    def UpDate(self):
         arreglo =[self.E_Caso.get().upper(), self.E_Cliente.get().upper(), self.E_Denominacion.get().upper(), self.E_Ciudad_Sede.get().upper(),
                self.E_Territorial.get().upper(), self.E_Estado.get().upper(),self.E_Oc.get(), self.E_OcF.get(),self.Em.get(), self.E_EstadoSAP.get().upper(),
                self.E_Gestor.get().upper(), self.E_Comentario.get().upper(),self.E_Sintoma.get().upper(), self.E_Tecnico.get().upper(),self.E_FCini.get().upper(), 
                self.E_FCfinal.get().upper(),self.MO.get(), self.Mt.get(), self.P.get(), self.ST.get(), self.E_FV.get().upper(), self.FCF.get().upper()]
         ref = self.E_Caso.get()
         DB = conexion()
         DB.UpDateCase(arreglo,ref)
         if self.E_Estado.get()=="DESASIGNADO":
              self.enviar_desasignadas()
         elif self.E_Estado.get()=="FINALIZADO":
              self.enviar_finalizado()
         self.ClearTable()
         self.SetearVar()
         self.showDataBase(self.vacio)
         self.destroy_widgets_numeroCasos()
         self.funcionnrocasos()
         self.BT_Actualizar.config(state="disabled")
         messagebox.showinfo(title="Actualización", message="Base de datos, actualizada correctamente")

    # metodo para setear los entrys    
    def SetearVar (self):
      
        self.E_Caso.set("")
        self.E_Fecha.set("")
        self.E_Cliente.set("")
        self.E_Denominacion.set("")
        self.E_Ciudad_Sede.set("")
        self.E_Territorial.set("")
        self.E_Estado.set("")
        self.E_Gestor.set("")
        self.E_Comentario.set("")
        self.E_Tecnico.set("")
        self.E_Mano_Obra.set(1)
        self.E_Materiales.set(1)
        self.E_Parafiscales.set(1) 
        self.E_Sub_Total.set(1)
        self.E_Oc.set("")
        self.E_Search.set("")
        self.E_OcF.set("")
        self.E_EstadoSAP.set("")
        self.E_FCF.set("")
        self.E_FCfinal.set("")
        self.E_FV.set("")
        self.E_FCini.set("")
        self.E_PUB.set("")
        self.E_Sintoma.set("")
        self.EM.set("")
        self.actualizarGrafica()


    # metodo para buscar caso
    def Busacador(self, event): 
        caso = self.E_Search.get()
        ciudad = self.E_Search.get()
        estado = self.E_Search.get()
        tecnico = self.E_Search.get()
        gestor = self.E_Search.get()
        territorial = self.E_Search.get()
        mes = self.E_Search.get()
        año = self.E_Search.get()
        fecha = self.E_Search.get()
        cliente = self.E_Search.get()
        denominacion = self.E_Search.get()
        oc = self.E_Search.get()
        comentario = self.E_Search.get()
        elemento = [caso, ciudad, estado, tecnico, gestor, territorial, mes, año, fecha, cliente, denominacion, oc, comentario]
        self.ClearTable()
        self.showDataBase(elemento)
        self.destroy_widgets_numeroCasos()
        self.funcionnrocasos()

    # metodo para mostrar la base de datos 
    def showDataBase(self, elemento):
        DB = conexion()
        self.BaseDatos = DB.ShowDataBaseG(self.user)
        FiltroBD = DB.SearchCaseGestor(self.user,elemento)
        if elemento[0]=="" and elemento[1]=="" and elemento[2]=="" and elemento[3]=="" and elemento[4]=="" and elemento[5]=="" and elemento[6]=="" and elemento[7]=="" and elemento[8]=="" and elemento[9] =="" and elemento[10]=="" and elemento[11]=="":
            for i in self.BaseDatos:
                self.Table_View.insert('','end',values=i)
        else:
             for i in FiltroBD:
                  self.Table_View.insert('','end',values=i)
    # metodo para riniciar el modulo para habilitar el boton registro
    def Restart(self, event):
         if event.keysym =='Escape':
              self.SetearVar()
              self.ClearTable()
              self.showDataBase(self.vacio)
              self.BT_Actualizar.config(state="disabled")
              self.destroy_widgets_numeroCasos()
              self.funcionnrocasos()
              self.actualizarGrafica()
              
              

    def ValidarValorNumerico(self,event):
         if event.char.isdigit():
            pass
         elif event.keysym == 'BackSpace':
            pass
         elif event.keysym == 'Left':
            pass
         elif event.keysym == 'Tab':
              pass
         else:
              return "break"

 
    #exportar casos en un excel
    def exportar(self):
         Exportar_Base_Datos("", self.user)
    #muestra el costo del caso segun afiliaciones, pagos y pedidos
    def CostoCaso(self,event):
          vidaDelCaso = CaseLife(self.ot)        

    #metodo para mostrar los numeros de casos de toda la base de datos
    def funcionnrocasos(self): 
        Contar_casos = conexion()
        estados = Contar_casos.EstadosCasos()
        self.container_info = Frame(self.Frame_General, bg="#DEE9F4")
        self.container_info.grid(column=1, row=0, sticky=(S,W), padx=6, pady=5)
        
        contador = 0
        for i in estados:
            std = estados[contador]
            self.nrcase = Label(self.container_info, text=Contar_casos.CountCaseGestor(std[0],self.user), foreground="#282e35", font="barlow 10", background="#DEE9F4")
            self.nrcase.grid(column=contador,row=1, sticky=(E,W))
            self.txtnrcase = Label(self.container_info, text=std[0], foreground="white", font="barlow 10", background="#282e35")
            self.txtnrcase.grid(column=contador,row=0)
            contador +=1
    def destroy_widgets_numeroCasos(self):
        self.container_info.destroy()
        self.nrcase.destroy()
        self.txtnrcase.destroy()

    # metodo para colocar separadores de mil en los entrys
    def validarseparadores(self, event, num,variable):
         if variable.get() !="":
            variable.select_range(0,END)
            numero = float(variable.get())
            numero_formateado = "{:,}".format(numero)
            variable.delete(0, END)
            variable.insert(0, numero_formateado)
            num.set(numero)
         elif variable.get() == "":
              variable.insert(0,float(1))
              num.set(variable.get())
              


    # metodo para mostrar separadores de mil al seleccionar un caso
    def mostrarNumSeparadors(self, num,variable):
         numero = float(variable.get())
         numero_formateado = "{:,}".format(numero)
         variable.delete(0, END)
         variable.insert(0, numero_formateado)
         num.set(numero)


    # metodo para formatear los entrys donde van las fechas de tipo fecha
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
        elif event.keysym == 'Tab':
             pass
        else:
            return "break"
        

    # dibujo de graficas para mostrar el porcentaje de la utilidad bruta
            
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
            
         
    #metodo para actualizar la grafica al seleccionar otro caso
    def actualizarGrafica(self):
        try:
            elemento = self.Table_View.item(self.Table_View.focus())
            porcentaje = "{:.2%}".format(float(elemento["values"][28]))
            if float(elemento["values"][28]) <= 0.39:
                self.txtporcentaje.config(foreground="red")
            else:
                self.txtporcentaje.config(foreground="#2EAD00")
            self.txtporcentaje.grid_forget()
            self.txtporcentaje.config(text=porcentaje)
            self.txtporcentaje.grid(column=3,row=11,padx=5,pady=5)
        except IndexError:
            porcentaje = 0 
            self.txtporcentaje.grid_forget()
            self.txtporcentaje.config(text=porcentaje,foreground="red")
            self.txtporcentaje.grid(column=3,row=11,padx=5,pady=5)


    def validar_estado_rcc(self, event):
        if self.E_EstadoSAP.get()=="REAL" or self.E_EstadoSAP.get()=="VISA":
            self.estadorcc = ["EN PROCESO DE EJECUCIÓN", "FINALIZADO", "DESASIGNADO"]
            self.Estado.config(values=self.estadorcc)
        else:
            self.estadorcc = ["EN PROCESO DE EJECUCIÓN", "DESASIGNADO"]
            self.Estado.config(values=self.estadorcc)
            
    def enviar_desasignadas(self):
         db = conexion()
         db1 = conexion()
         db.metodo_desasignadas(self.E_Estado.get().upper())
         db1.DeleteCase(self.E_Caso.get().upper())

    def enviar_finalizado(self):
         db = conexion()
         db1 = conexion()
         db.metodo_finalizado(self.E_Estado.get().upper())
         db1.DeleteCase(self.E_Caso.get().upper())


    def autocompletar(self, event):
         entrada_texto = self.Tecnico.get()
         
         self.lista_sugerencia.delete(0,END)

         if entrada_texto:
            sugerencias = [s for s in self.opciones if entrada_texto.upper() in s.upper()]
            for sugerencia in sugerencias:
                self.lista_sugerencia.insert(END, sugerencia)
         self.lista_sugerencia.place(relx=0.72, rely=0.045)

    def seleccionar_sugerencia(self,event):
        try:
            entrada_texto = self.lista_sugerencia.get(self.lista_sugerencia.curselection())
            self.Tecnico.delete(0, END)
            self.Tecnico.insert(0, entrada_texto)
            self.lista_sugerencia.delete(0, END)
            self.lista_sugerencia.place_forget()
        except TclError:
             pass
                 

