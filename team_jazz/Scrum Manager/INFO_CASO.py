from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Data_Base import *

class CaseLife:
    def __init__(self, caso):
        self.caso = caso
        self.win = Toplevel(background="white")
        self.win.title("Detalles del caso")
        self.win.geometry("560x310+100+0")
        self.win.resizable(0,0)
        self.win.iconbitmap("./icon.ico")
        self.tabla()
        self.datos()
        self.balance()

    
    def balance(self):
        self.Balance = Label(self.ventana, text='{:,}'.format(self.bl.get()), font="barlow 11 bold" )
        self.txtBalance = Label(self.ventana, text="Balance:", font="barlow 12 bold", bg="white")
        if self.bl.get() < 0:
            self.Balance.config(foreground="red", background="white")
        else:
            self.Balance.config(foreground="green", background="white")
        self.Balance.place(relx=0.6,rely=0.01, width=120)
        self.txtBalance.place(relx=0.4,rely=0.01, width=120)

        

    def tabla(self):
        self.ventana = LabelFrame(self.win, text="Detalles del caso", background="white")
        self.ventana.config(width=540, height=300)
        self.ventana.grid(column=0,row=0, padx=20,pady=20)

        self.etq=Label(self.ventana,text=self.caso, font="barlow 12 bold", background="white")
        self.etq.place(relx=0.15, rely=0.01)
        self.bl = IntVar()

        self.etq=Label(self.ventana,text="Caso:", font="barlow 12 bold", background="white")
        self.etq.place(relx=0.005, rely=0.01)



        self.etq=Label(self.ventana,text="AFILIACIONES", font="barlow 11 bold", background="white")
        self.etq.place(relx=0.03, rely=0.1)
        self.vistaBD = ttk.Treeview(self.ventana, columns=(1,2,3), show="headings")
        self.vistaBD.heading(1, text="FECHA")
        self.vistaBD.heading(2, text="GESTOR")
        self.vistaBD.heading(3, text="MONTO")
        self.vistaBD.column(1, anchor="center", width=90)
        self.vistaBD.column(2, anchor="center", width=70)
        self.vistaBD.column(3, anchor="center", width=70)
        self.vistaBD.place(relx=0.03,rely=0.2, width=230,height=70)

        self.etq=Label(self.ventana,text="SEG.GTOR", font="barlow 11 bold", background="white")
        self.etq.place(relx=0.5, rely=0.1)
        self.vistabdg = ttk.Treeview(self.ventana, columns=(1,2,3), show="headings")
        self.vistabdg.heading(1, text="FECHA")
        self.vistabdg.heading(2, text="GESTOR")
        self.vistabdg.heading(3, text="MONTO")
        self.vistabdg.column(1, anchor="center", width=90)
        self.vistabdg.column(2, anchor="center", width=70)
        self.vistabdg.column(3, anchor="center", width=70)
        self.vistabdg.place(relx=0.48,rely=0.2, width=230,height=70)

        self.etpg=Label(self.ventana,text="PAGOS", font="barlow 11 bold", background="white")
        self.etpg.place(relx=0.03, rely=0.5)
        self.vistabdpg = ttk.Treeview(self.ventana, columns=(1,2,3), show="headings")
        self.vistabdpg.heading(1, text="FECHA")
        self.vistabdpg.heading(2, text="GESTOR")
        self.vistabdpg.heading(3, text="MONTO")
        self.vistabdpg.column(1, anchor="center", width=90)
        self.vistabdpg.column(2, anchor="center", width=70)
        self.vistabdpg.column(3, anchor="center", width=70)
        self.vistabdpg.place(relx=0.03,rely=0.6, width=230,height=70)

        self.etp=Label(self.ventana,text="PEDIDOS", font="barlow 11 bold", background="white")
        self.etp.place(relx=0.5, rely=0.5)
        self.vistabdp = ttk.Treeview(self.ventana, columns=(1,2,3), show="headings")
        self.vistabdp.heading(1, text="FECHA")
        self.vistabdp.heading(2, text="GESTOR")
        self.vistabdp.heading(3, text="MONTO")
        self.vistabdp.column(1, anchor="center", width=90)
        self.vistabdp.column(2, anchor="center", width=70)
        self.vistabdp.column(3, anchor="center", width=70)
        self.vistabdp.place(relx=0.48,rely=0.6, width=230,height=70)

    def datos(self):
        db = conexion()
        datos_afiliaciones = db.FchyPgoAF(self.caso)
        datos_gestor = db.Vlpro(self.caso)
        datos_pagos = db.pagos(self.caso)
        datos_pedidos = db.pedidos(self.caso)

        for i in datos_afiliaciones:
            self.vistaBD.insert("","end",values=i)

        for i in datos_gestor:
            self.vistabdg.insert("","end",values=i)

        for i in datos_pagos:
            self.vistabdpg.insert("","end",values=i)

        for i in datos_pedidos:
            self.vistabdp.insert("","end",values=i)

        sumaf = db.sumAF(self.caso)[0]
        Csstt = db.CstoTT(self.caso)
        suma_pagos = db.Suma_pagos(self.caso)[0]
        suma_pedidos = db.Suma_pedidos(self.caso)[0]

        sPedidos = suma_pedidos.__getitem__(0)
        sPagos = suma_pagos.__getitem__(0)
        sAfiliaciones = sumaf.__getitem__(0)
        cTotal = Csstt
        valores = [sPagos,sPedidos,sAfiliaciones]
                    

        if sPagos is None and sPedidos is None and sAfiliaciones is None:
            suma_iversion = 0
        elif sPagos is None and sPedidos is None:
            suma_iversion = float(sAfiliaciones)
        elif sPagos is None and sAfiliaciones is None:
            suma_iversion = float(sPedidos)
        elif sPedidos is None and sAfiliaciones is None:
            suma_iversion = float(sPagos)
        elif sPagos is None:
            suma_iversion = float(sAfiliaciones) + float(sPedidos)
        elif sPedidos is None:
            suma_iversion = float(sAfiliaciones) + float(sPagos)
        elif sAfiliaciones is None:
            suma_iversion = float(sPagos) + float(sPedidos)
        else:
            suma_iversion = float(sPagos) + float(sPedidos) + float(sAfiliaciones)



        if cTotal is not None:
            var = str(cTotal).replace(")","")
            var1 = var.replace("(","")
            var2 = var1.replace(",","")
            var3 = var2.replace("'","")
            
            balance = float(var3) - float(suma_iversion)
        else:
            balance = 0 - float(suma_iversion)
        
        self.bl.set(balance)
        