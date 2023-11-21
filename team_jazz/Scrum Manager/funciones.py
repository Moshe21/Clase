"""
FUNCIONES PARA APP

"""

from tkinter import messagebox
import mysql.connector


def centrar_ventana(ventana, ancho, alto):
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    ancho_ventana = ancho
    alto_ventana = alto
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    return f"{ancho_ventana}x{alto_ventana}+{x}+{y}"

# FUNCION PARA DESCONECTAR USUARIO


def desconectar(estado, usuario):
    conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
    cursor = conexion.cursor()
    sql = f"UPDATE usuarios SET estado = '{estado}' WHERE usuario = '{usuario}'"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

# FUNCION PARA CONECTAR USUARIO


def conectar(estado, usuario):
    conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="RCC",
                                       port="3306")
    cursor = conexion.cursor()
    sql = f"UPDATE usuarios SET estado = '{estado}' WHERE usuario = '{usuario}'"
    cursor.execute(sql)
    conexion.commit()
    conexion.close()

# FUNCION QUE TRAE EL HOST

def importar_host():
        with open("./host.txt", "r") as f:
            valor = f.read()
            return valor.strip()

# FUNCION PARA VALIDAR USUARIO CONTRASEÑA Y ROL


def validar_usuario(variable):
    conexion = mysql.connector.connect(user="root", password="0000",
                                       host=importar_host(),
                                       database="rcc",
                                       port="3306")
    cursor = conexion.cursor()
    sql = f"SELECT * FROM usuarios WHERE usuario = '{variable}'"
    cursor.execute(sql)
    datos = cursor.fetchone()
    conexion.commit()
    conexion.close()

    return datos

# FUNCION PARA HOVER EN BOTONES


def hover_on(event, btn):
    btn.config(bg="#0052ff", foreground="White")


def hover_off(event, btn):
    btn.config(bg="#282e35", foreground="#00d2ff")

# FUNCION PARA FORMATEO DE FECHA EN ENTRYS


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
    else:
        return "break"

# FUNCION PARA FORMATEO DE MONTOS EN ENTRYS


def formatear_entry(event, variable):
    texto = str(variable.get())
    if texto == "":
        variable.insert(0, 0)
    else:
        contador = 0
        resultado = ""

        for numero in texto[::-1]:
            if contador == 3:
                resultado += "."
                contador = 0
            resultado += numero
            contador += 1
        monto_formateado = resultado[::-1]
        variable.delete(0, 'end')
        variable.insert(0, monto_formateado)


def vaciar_entry(event, variable):
    variable.delete(0, "end")

# FUNCION PARA QUITAR FORMATEO DE MONTOS EN ENTRYS


def quitar_formato(variable):
    try:
        texto = str(variable.get())
        nuevo_texto = texto.replace(".", "")
        monto_sin_formato = int(nuevo_texto)
        return monto_sin_formato
    except:
        messagebox.showerror("Error", "Debes llenar los campos de montos ($).")


def quitar_puntos_entry(event,entry):
    entry.insert(0,0)
    texto = str(entry.get())
    nuevo_texto = texto.replace(".", "")
    monto_sin_formato = int(nuevo_texto)
    entry.delete(0,'end')
    entry.insert(0, monto_sin_formato)
    entry.select_range(0,'end')

# FUNCION PARA FORMATEO DE MONTOS


def formatear_monto(monto):
    contador = 0
    resultado = ""

    for numero in monto[::-1]:
        if contador == 3:
            resultado += "."
            contador = 0
        resultado += numero
        contador += 1
    monto_formateado = resultado[::-1]
    return monto_formateado



def solo_numeros(event):
    if event.keysym == 'Tab' or event.keysym == 'BackSpace' or event.keysym == 'Left' or event.keysym == 'Right':
        pass
    elif event.char.isdigit():
        pass
    else:
        return "break"