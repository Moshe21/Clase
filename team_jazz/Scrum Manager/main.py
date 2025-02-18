import tkinter
from tkinter import messagebox
from modulo_comercial import abrir_modulo_comercial
from modulo_compras import abrir_modulo_compras
from modulo_coordinador import abrir_modulo_coordinador
from modulo_facturacion import abrir_modulo_facturacion
from modulo_rrhh import abrir_modulo_rrhh
from modulo_superusuario import abrir_modulo_superusuario
from Data_Base import conexion
from funciones import *


def enter(event):
    login_system()
    
def login_system():
    entrada_usuario = username_entry.get()
    entrada_password = password_entry.get()

    datos = validar_usuario(entrada_usuario)
    if entrada_usuario == '':
            messagebox.showerror("Error","Usuario es campo obligatorio")
    elif entrada_password == '':
        messagebox.showerror("Error","Contraseña es campo obligatorio")
    else:
        try:
           
                
                if entrada_usuario == 1 and entrada_password == 1:
                    if entrada_usuario == 1:
                        
                        abrir_modulo_comercial(validar_us.us(entrada_usuario)[0][0])
                        
                    elif datos[4] == 'coordinador':
                        login.destroy()

                        conectar("online", entrada_usuario)
                        abrir_modulo_coordinador(str(datos[3]))
                        desconectar("offline",entrada_usuario)   
                    elif datos[4] == 'gerente':
                        login.destroy()

                        conectar("online", entrada_usuario)
                        abrir_modulo_superusuario(str(datos[3]))
                        desconectar("offline",entrada_usuario)   
                    elif datos[4] == 'rrhh':
                        login.destroy()

                        conectar("online", entrada_usuario)
                        abrir_modulo_rrhh()
                        desconectar("offline",entrada_usuario)   
                    elif datos[4] == 'compras':
                        login.destroy()

                        conectar("online", entrada_usuario)
                        abrir_modulo_compras()
                        desconectar("offline",entrada_usuario)
                    elif datos[4] == 'facturacion':
                        login.destroy()

                        conectar("online", entrada_usuario)
                        abrir_modulo_facturacion()
                        desconectar("offline",entrada_usuario)   
                else:
                    messagebox.showerror("Error","Usuario o contraseña inválidos")
            
        except Exception as ep:
            messagebox.showerror("Error","Usuario o contraseña inválidos")
    
login = tkinter.Tk()
login.title("Scrum Manager")
ancho_pantalla = login.winfo_screenwidth()
alto_pantalla = login.winfo_screenheight()
ancho_ventana = 390
alto_ventana = 210
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2
login.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
login.config(bg="white")
login.resizable(False, False)
login.iconbitmap("./icon.ico")
login.bind("<Return>", enter)

# CREACION DEL MARCO PARA CONTENER LOS WIDGETS

marco_login = tkinter.Frame(login, padx=10, pady=10, bg="white")
marco_login.pack(padx=10, pady=10)

# CREACION DE WIDGETS DENTRO DEL MARCO

username_label = tkinter.Label(
    marco_login, text="Username", font=("Barlow", 15), bg="white", foreground="black")
username_entry = tkinter.Entry(marco_login, font=("Barlow", 15), bd=0)
username_label.grid(row=0, column=0, padx=5, pady=5)
username_entry.grid(row=0, column=1, padx=5, pady=5)


password_label = tkinter.Label(
    marco_login, text="Password", font=("Barlow", 15), bg="white", foreground="black")
password_entry = tkinter.Entry(
    marco_login, font=("Barlow", 15), show="*", bd=0)
password_label.grid(row=1, column=0, padx=5, pady=5)
password_entry.grid(row=1, column=1, padx=5, pady=5)

btn_login = tkinter.Button(marco_login, text="Login",
                           bd=0, relief="flat",
                           cursor="hand2",
                           bg="#282e35",
                           foreground="#00d2ff",
                           activebackground="#282e35",
                           activeforeground="#00d2ff",
                           font=("Barlow bold", 15),
                           command=login_system)
btn_login.grid(row=2, column=0, columnspan=2, sticky="we")
btn_login.bind("<Enter>", lambda event: hover_on(event, btn_login))
btn_login.bind("<Leave>", lambda event: hover_off(event, btn_login))

# SEPARACION ENTRE WIDGETS CONTENIDOS EN EL MARCO

for widget in marco_login.winfo_children():
    widget.grid_configure(padx=10, pady=10)

# DECORACION DE ENTRYS

deco_username = tkinter.Frame(marco_login, border=1, bg="gray")
deco_username.place(height=1, width=203, x=126, y=41)

deco_password = tkinter.Frame(marco_login, border=1, bg="gray")
deco_password.place(height=1, width=203, x=126, y=94)

username_entry.focus_set()

login.mainloop()
