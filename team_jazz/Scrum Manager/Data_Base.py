import mysql.connector
from funciones import *


class conexion:
    def __init__(self):
        self.Conexion = mysql.connector.connect(
            host=importar_host(),
            user="root",
            password="0000",
            database="RCC"
        )

        self.cursor = self.Conexion.cursor()

# ________________________________interaccion con tabla general de los casos________________________________
    # retorna base de datos general de todos los casos
    def ShowDataBase(self):
        sql = "SELECT * FROM casos_rcc"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # retorna base de datos general con el filtro por gestor
    def ShowDataBaseG(self, user):
        sql = "SELECT * FROM casos_rcc WHERE GESTOR = '{}'".format(user)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para registrar un nuevo caso en la tabla de casos
    def NewCase(self, elemento):
        SQ = "SET lc_time_names = 'es_ES'"
        sql = "INSERT INTO casos_rcc(CASO, FECHA, MES, AÑO, CLIENTE, DENOMINACION, CIUDAD_SEDE, TERRITORIAL, ESTADO_RCC, OC, OC_FISICA, EM, ESTADO_SAP, GESTOR, COMENTARIO,SINTOMA, TECNICO, FECHA_INICIO_EJECUCION, FECHA_FINAL_EJECUCION, MANO_OBRA, MATERIAL, PARAFISCALES, COSTO_TOTAL, SUBTOTAL_SAP, IVA,TOTAL_IVA, COMISION_OTROS, UTILIDAD_BRUTA, PORCENTAJE_UB, RTE_FUENTE, RTE_IVA, RTE_ICA, PAGO_FINAL, UTILIDAD_NETA, PORCENTA_UN, FACTURA_VENTA, FECHA_FACTURA) VALUES('{}','{}',monthname(CURDATE()),YEAR(CURDATE()),'{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}', '{}', '{}','{}','{}','{}','{}','{}','{}', MANO_OBRA + MATERIAL + PARAFISCALES,'{}' ,SUBTOTAL_SAP * 0.19, SUBTOTAL_SAP + IVA, SUBTOTAL_SAP * 0.05, SUBTOTAL_SAP - COSTO_TOTAL - COMISION_OTROS,UTILIDAD_BRUTA / SUBTOTAL_SAP, SUBTOTAL_SAP * 0.04, IVA * 0.15, SUBTOTAL_SAP * 0.011, TOTAL_IVA - RTE_FUENTE - RTE_IVA - RTE_ICA, SUBTOTAL_SAP - RTE_FUENTE - RTE_IVA - RTE_ICA - COSTO_TOTAL, UTILIDAD_NETA / SUBTOTAL_SAP, '{}','{}')".format(
            elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5], elemento[6], elemento[7], elemento[8], elemento[9], elemento[10], elemento[11], elemento[12], elemento[13], elemento[14], elemento[15], elemento[16], elemento[17], elemento[18], elemento[19], elemento[20], elemento[21], elemento[22])
        self.cursor.execute(SQ)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para actualizar caso
    def UpDateCase(self, elemento, ref):
        sql = "UPDATE casos_rcc set CASO = '{}', CLIENTE = '{}', DENOMINACION = '{}', CIUDAD_SEDE = '{}', TERRITORIAL = '{}', ESTADO_RCC = '{}',OC = '{}', OC_FISICA = '{}', EM = '{}', ESTADO_SAP='{}', GESTOR = '{}', COMENTARIO = '{}', SINTOMA = '{}', TECNICO = '{}',FECHA_INICIO_EJECUCION = '{}', FECHA_FINAL_EJECUCION ='{}', MANO_OBRA = '{}', MATERIAL = '{}', PARAFISCALES = '{}', SUBTOTAL_SAP = '{}',COSTO_TOTAL = MANO_OBRA + MATERIAL + PARAFISCALES, IVA = SUBTOTAL_SAP * 0.19, TOTAL_IVA = SUBTOTAL_SAP + IVA, COMISION_OTROS = SUBTOTAL_SAP * 0.05, UTILIDAD_BRUTA = SUBTOTAL_SAP - COSTO_TOTAL - COMISION_OTROS, PORCENTAJE_UB = UTILIDAD_BRUTA / SUBTOTAL_SAP, RTE_FUENTE = SUBTOTAL_SAP * 0.04, RTE_IVA = IVA * 0.15, RTE_ICA = SUBTOTAL_SAP * 0.011, PAGO_FINAL = TOTAL_IVA - RTE_FUENTE - RTE_IVA - RTE_ICA, UTILIDAD_NETA = SUBTOTAL_SAP - RTE_FUENTE - RTE_IVA - RTE_ICA - COSTO_TOTAL, PORCENTA_UN = UTILIDAD_NETA / SUBTOTAL_SAP, FACTURA_VENTA = '{}', FECHA_FACTURA = '{}' where CASO = '{}'".format(
            elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5], elemento[6], elemento[7], elemento[8], elemento[9], elemento[10], elemento[11], elemento[12], elemento[13], elemento[14], elemento[15], elemento[16], elemento[17], elemento[18], elemento[19], elemento[20], elemento[21], ref)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para borrar caso
    def DeleteCase(self, ref):
        sql = "DELETE FROM casos_rcc WHERE CASO = '{}'".format(ref)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def DeleteCaseDesasignados(self, ref):
        sql = "DELETE FROM casos_desasignados WHERE CASO = '{}'".format(ref)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def DeleteCaseFacturados(self, ref):
        sql = "DELETE FROM casos_finalizados WHERE CASO = '{}'".format(ref)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para filtrar o buscar casos
    def SearchCase(self, elemento):
        sql = "SELECT * FROM casos_rcc WHERE CASO LIKE '%{}%' or CIUDAD_SEDE LIKE '%{}%' or ESTADO_SAP LIKE '%{}%' or TECNICO LIKE '%{}%' or GESTOR = '{}' or TERRITORIAL = '{}' or MES LIKE '%{}%' or AÑO LIKE '%{}%' or FECHA LIKE'%{}%' or CLIENTE = '{}' or DENOMINACION LIKE '%{}%' or OC LIKE '%{}%' or COMENTARIO LIKE '%{}%'".format(
            elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5], elemento[6], elemento[7], elemento[8], elemento[9], elemento[10],elemento[11], elemento[12])
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para filtrar o buscar casos en el usuario del gestor
    def SearchCaseGestor(self, user, elemento):
        sql = "SELECT * FROM casos_rcc WHERE GESTOR = '{}' and (CASO LIKE '%{}%' or CIUDAD_SEDE LIKE '%{}%' or ESTADO_SAP LIKE '%{}%' or TECNICO LIKE '%{}%' or TERRITORIAL = '{}' or MES LIKE '%{}%' or AÑO LIKE '%{}%' or FECHA LIKE'%{}%' or CLIENTE = '{}' or DENOMINACION LIKE '%{}%' or OC_FISICA like '%{}%' or COMENTARIO LIKE '%{}%')".format(
            user, elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5], elemento[6], elemento[7], elemento[8], elemento[9], elemento[10], elemento[11])
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para contar los casos por etiqueta del estado en sap
    def CountCase(self, estado):
        sql = "SELECT COUNT(CASO) FROM casos_rcc WHERE ESTADO_SAP = '{}'".format(
            estado)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para contar caso por etiquetas segun el gestor
    def CountCaseGestor(self, estado, user):
        sql = "SELECT COUNT(CASO) FROM casos_rcc WHERE ESTADO_SAP ='{}' AND GESTOR = '{}'".format(
            estado, user)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para exportar la base de datos general de los casos a un archivo excel
    def ExportarDBExcel(self):
        mycursor = self.Conexion.cursor(dictionary=True)
        sql = "SELECT * FROM casos_rcc"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def Exportar_desasignadas(self):
        mycursor = self.Conexion.cursor(dictionary=True)
        sql = "SELECT * FROM casos_desasignados"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def Exportar_facturadas(self):
        mycursor = self.Conexion.cursor(dictionary=True)
        sql = "SELECT * FROM casos_finalizados"
        mycursor.execute(sql)
        return mycursor.fetchall()

    def Exportar_BD_gestor(self, gestor):
        mycursor = self.Conexion.cursor(dictionary=True)
        sql = f"SELECT * FROM casos_rcc where gestor = '{gestor}'"
        mycursor.execute(sql)
        return mycursor.fetchall()

    # retorna la fecha, gestor y costototal por caso
    def Vlpro(self, ref):
        sql = "SELECT FECHA, GESTOR, COSTO_TOTAL FROM casos_rcc WHERE CASO = '{}'".format(
            ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # retorna el costo total por caso
    def CstoTT(self, ref):
        sql = "SELECT COSTO_TOTAL FROM casos_rcc WHERE CASO = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # valida que el caso exista en la base de datos
    def validarcaso(self, ref):
        sql = "SELECT CASO FROM casos_rcc WHERE CASO = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

      # retorna las etiqutas de los estados de los casos
    def EstadosCasos(self):
        sql = "select distinct estado_SAP from casos_rcc"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # retorna los nombres de los gestores en la base de datos
    def nombre_de_gestores(self):
        sql = "select nombre from usuarios where rol = 'gestor' order by nombre asc "
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def EstadoSap(self):
        sql = "select distinct ESTADO_SAP from casos_rcc order by estado_sap asc"
        self.cursor.execute(sql)
        lista = self.cursor.fetchall()
        resultado = []
        for i in lista:
            resultado.append(i[0])
        return resultado

    def EstadoRcc(self):
        sql = "select distinct ESTADO_RCC from casos_rcc"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def metodo_desasignadas(self, desasignado):
        sql = f"insert into casos_desasignados select * from casos_rcc where	ESTADO_RCC = '{desasignado}'"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def metodo_finalizado(self, Finalizado):
        sql = f"insert into casos_finalizados select * from casos_rcc where	ESTADO_RCC = '{Finalizado}'"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()
        

    def Revivir_desasignados(self, caso):
        sql = f"insert into casos_rcc select * from casos_desasignados where	CASO = '{caso}'"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def Revivir_finalizados(self, caso):
        sql = f"insert into casos_rcc select * from casos_finalizados where	CASO = '{caso}'"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def mostrar_tabla_desasignados(self, buscador):
        if buscador == ["","","","","","","","","",""]:
            sql = "select * from casos_desasignados"
        else:
            sql = f"select * from casos_desasignados where caso LIKE '%{buscador[0]}%' or mes LIKE '%{buscador[1]}%' or gestor LIKE '%{buscador[2]}%' or fecha LIKE '%{buscador[3]}%' or cliente LIKE '%{buscador[5]}%' or territorial LIKE '%{buscador[6]}%' or tecnico LIKE '%{buscador[7]}%' or oc like '%{buscador[8]}%' or ciudad_sede like '%{buscador[9]}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def mostrar_tabla_finalizados(self, buscador):
        if buscador == ["","","","","","","","","",""]:
            sql = "select * from casos_finalizados"
        else:
            sql = f"select * from casos_finalizados where caso LIKE '%{buscador[0]}%' or mes LIKE '%{buscador[1]}%' or gestor LIKE '%{buscador[2]}%' or fecha LIKE '%{buscador[3]}%' or cliente LIKE '%{buscador[5]}%' or territorial LIKE '%{buscador[6]}%' or tecnico LIKE '%{buscador[7]}%' or oc like '%{buscador[8]}%' or ciudad_sede like '%{buscador[9]}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def mostrar_tabla_facturados(self, buscador):
        if buscador == ["","","","","","","","","",""]:
            sql = "select * from casos_facturados"
        else:
            sql = f"select * from casos_facturados where caso LIKE '%{buscador[0]}%' or mes LIKE '%{buscador[1]}%' or gestor LIKE '%{buscador[2]}%' or fecha LIKE '%{buscador[3]}%' or cliente LIKE '%{buscador[5]}%' or territorial LIKE '%{buscador[6]}%' or tecnico LIKE '%{buscador[7]}%' or oc like '%{buscador[8]}%' or ciudad_sede like '%{buscador[9]}%'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def Caso_facturado(self, elemento):
        SQ = "SET lc_time_names = 'es_ES'"
        sql = "INSERT INTO casos_facturados(CASO, FECHA, MES, AÑO, CLIENTE, DENOMINACION, CIUDAD_SEDE, TERRITORIAL, ESTADO_RCC, OC, OC_FISICA, EM, ESTADO_SAP, GESTOR, COMENTARIO,SINTOMA, TECNICO, FECHA_INICIO_EJECUCION, FECHA_FINAL_EJECUCION, MANO_OBRA, MATERIAL, PARAFISCALES, COSTO_TOTAL, SUBTOTAL_SAP, IVA,TOTAL_IVA, COMISION_OTROS, UTILIDAD_BRUTA, PORCENTAJE_UB, RTE_FUENTE, RTE_IVA, RTE_ICA, PAGO_FINAL, UTILIDAD_NETA, PORCENTA_UN, FACTURA_VENTA, FECHA_FACTURA, FECHA_PROBABLE_FACTURACION) VALUES('{}','{}',monthname(CURDATE()),YEAR(CURDATE()),'{}','{}','{}','{}','{}','{}','{}','{}','{}', '{}', '{}', '{}','{}','{}','{}','{}','{}','{}', MANO_OBRA + MATERIAL + PARAFISCALES,'{}' ,SUBTOTAL_SAP * 0.19, SUBTOTAL_SAP + IVA, SUBTOTAL_SAP * 0.05, SUBTOTAL_SAP - COSTO_TOTAL - COMISION_OTROS,UTILIDAD_BRUTA / SUBTOTAL_SAP, SUBTOTAL_SAP * 0.04, IVA * 0.15, SUBTOTAL_SAP * 0.011, TOTAL_IVA - RTE_FUENTE - RTE_IVA - RTE_ICA, SUBTOTAL_SAP - RTE_FUENTE - RTE_IVA - RTE_ICA - COSTO_TOTAL, UTILIDAD_NETA / SUBTOTAL_SAP, '{}','{}', '{}')".format(
            elemento[0], elemento[1], elemento[2], elemento[3], elemento[4], elemento[5], elemento[6], elemento[7], elemento[8], elemento[9], elemento[10], elemento[11], elemento[12], elemento[13], elemento[14], elemento[15], elemento[16], elemento[17], elemento[18], elemento[19], elemento[20], elemento[21], elemento[22], elemento[23])
        self.cursor.execute(SQ)
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # _______________________________interaccion con la tabla de afiliaciones______________________________________________________________________________

    # metdo para registrar una nueva afiliacion
    def ResgiterAfiliaciones(self, elemento):
        sql = f"INSERT INTO registro_diario_afiliaciones (CASO, GESTOR, FECHA_SOLICITUD, NOMBRE_APELLIDO, N°DOCUMENTO, TLF, DESDE, HASTA, COSTO_AF, REGIMEN, EST_AF, CIUDAD, SALARIO, ARL,EPS,PENSION,CAJA_COMPENSACIÓN, APORTE_EN_LINEA, NOVEDADES)VALUES('{elemento[0]}','{elemento[1]}',Date_Format(curdate(),'%d/%m/%y'),'{elemento[2]}','{elemento[3]}','{elemento[4]}','{elemento[5]}','{elemento[6]}',{elemento[7]},'{elemento[8]}','{elemento[9]}', '{elemento[10]}','{elemento[11]}','{elemento[12]}','{elemento[13]}','{elemento[14]}','{elemento[15]}','{elemento[16]}','{elemento[17]}')"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para actualizar afiliacion
    def ActualizarAF(self, elemento, ref):
        sql = f"UPDATE AFILIACIONES SET DESDE = '{elemento[0]}', HASTA = '{elemento[1]}', COSTO_AF = '{elemento[2]}', EST_AF = '{elemento[3]}', APORTE_EN_LINEA = '{elemento[4]}', SALARIO = '{elemento[5]}', ARL = '{elemento[6]}', NOVEDADES = '{elemento[7]}' WHERE ID = {ref}"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para eliminar afiliacion
    def EliminarAF(self, ref):
        sql = "DELETE FROM AFILIACIONES WHERE CASO = '{}' AND GESTOR ='{}' AND FECHA_SOLICITUD = '{}'".format(
            ref[0], ref[1], ref[2])
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    # metodo para mostrar base de datos de afiliacion
    def ShowBDAF(self):
        sql = "SELECT * FROM AFILIACIONES ORDER BY FECHA_SOLICITUD DESC"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para mostrar base de datos de afiliacion por gestor
    def ShowBDAFGestor(self, ref):
        sql = "SELECT * FROM AFILIACIONES WHERE GESTOR = '{}'".format(ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para buscar segun los casos de cada gestor
    def SearchBDAFGestor(self, user, elemento):
        sql = "SELECT * FROM afiliaciones WHERE GESTOR = '{}' and (CASO = '{}' or FECHA_SOLICITUD LIKE '%{}%' or NOMBRE_APELLIDO LIKE '%{}%' or EST_AF LIKE '%{}%')".format(
            user, elemento[0], elemento[1], elemento[2], elemento[3])
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para buscar dato en la tabla de afiliaciones
    def SearchCaseAF(self, elemento):
        sql = "SELECT * FROM afiliaciones WHERE CASO LIKE '%{}%' or GESTOR LIKE '%{}%' or FECHA_SOLICITUD LIKE '%{}%' or NOMBRE_APELLIDO LIKE '%{}%' or EST_AF LIKE '%{}%'".format(
            elemento[0], elemento[1], elemento[2], elemento[3], elemento[4])
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para registrar una novedad de un caso
    def novedades(self, novedades, elemento):
        sql = f"insert into novedades values(null,'{elemento[0]}','{elemento[1]}','{elemento[2]}','{elemento[3]}','{elemento[4]}','{elemento[5]}','{elemento[6]}','{elemento[7]}',{elemento[8]},'{elemento[9]}','{elemento[10]}', '{elemento[11]}','{elemento[12]}','{elemento[13]}','{elemento[14]}','{elemento[15]}','{elemento[16]}','{elemento[17]}','{novedades}')"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

    def Mostrar_BD_Novedades (self):
        sql ="select * from novedades"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def anular_afiliacion(self, elemento):
        sql = f"delete from novedades where caso = '{elemento[0]}' and fecha_solicitud = '{elemento[1]}' and nombre_apellido = '{elemento[2]}' and gestor = '{elemento[3]}'"
        self.cursor.execute(sql) 
        self.Conexion.commit()
        self.Conexion.close()

    def anular_afiliacion_tabla(self, elemento):
        sql = f"delete from afiliaciones where caso = '{elemento[0]}' and fecha_solicitud = '{elemento[1]}' and nombre_apellido = '{elemento[2]}' and gestor = '{elemento[3]}'"
        self.cursor.execute(sql)
        self.Conexion.commit()
        self.Conexion.close()

   

    # retorna fecha, gestor y costo de afiliaciones por caso
    def FchyPgoAF(self, ref):
        sql = "SELECT DESDE, GESTOR, COSTO_AF FROM afiliaciones WHERE CASO = '{}'".format(
            ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # suma las afiliaciones que se hacen por casos
    def sumAF(self, ref):
        sql = "SELECT sum(COSTO_AF) FROM afiliaciones WHERE CASO = '{}'".format(
            ref)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # retorna la cantidad de casos de un tecnico por mes
    def Casos_Tc_mes(self, tecnico, mes):
        sql = "SELECT  COUNT(caso) from casos_rcc where TECNICO = '{}' and MES ='{}'".format(
            tecnico, mes)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # retorna los meses de un año
    def Año_Mes(self, año):
        sql = "SELECT distinct MES FROM casos_rcc WHERE AÑO = '{}'".format(año)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # metodo para enviar afiliaciones diarias al seguimiento general de afiliaciones
    def mostrarTablaAfiliacionesDiarias(self):
        sql = "select * from registro_diario_afiliaciones"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def ActuarlizarAfiliacionesDiarias(self, elemento, ref, nombre):
        sql = f"UPDATE registro_diario_afiliaciones SET DESDE = '{elemento[0]}', HASTA = '{elemento[1]}', COSTO_AF = {elemento[2]}, EST_AF = '{elemento[3]}', APORTE_EN_LINEA = '{elemento[4]}', SALARIO = {elemento[5]}, ARL = '{elemento[6]}', NOVEDADES = '{elemento[7]}' WHERE CASO = '{ref}' AND NOMBRE_APELLIDO = '{nombre}'"
        self.cursor.execute(sql)
        # self.variable = self.cursor.fetchall()
        self.Conexion.commit()
        self.Conexion.close()

    def enviarAfiliacionesalHistorico(self, ref, nombre):
        sql = f"""insert into afiliaciones(CASO, GESTOR, FECHA_SOLICITUD, NOMBRE_APELLIDO, N°DOCUMENTO, TLF, DESDE, HASTA, COSTO_AF,
                REGIMEN, EST_AF, CIUDAD, SALARIO, ARL, EPS, PENSION, CAJA_COMPENSACIÓN, APORTE_EN_LINEA, NOVEDADES) SELECT CASO, GESTOR, FECHA_SOLICITUD, NOMBRE_APELLIDO, N°DOCUMENTO, TLF, DESDE, HASTA, COSTO_AF,
                REGIMEN, EST_AF, CIUDAD, SALARIO, ARL, EPS, PENSION, CAJA_COMPENSACIÓN, APORTE_EN_LINEA, NOVEDADES FROM registro_diario_afiliaciones where caso = '{ref}' and NOMBRE_APELLIDO = '{nombre}'"""
        sql1 = f"delete from registro_diario_afiliaciones where caso = '{ref}' and  NOMBRE_APELLIDO = '{nombre}'"
        self.cursor.execute(sql)
        self.cursor.execute(sql1)
        self.Conexion.commit()
        self.Conexion.close()

    def lista_ciudaddes(self):
        sql = "select distinct ciudad from afiliaciones order by ciudad asc"
        self.cursor.execute(sql)
        lista = self.cursor.fetchall()
        resultado = []
        for i in lista:
            resultado.append(i)
        return resultado
    
    def filtro_fecha_desafiliacion(self):
        sql = "select * from afiliaciones where hasta = Date_format(curdate(), '%d/%m/%Y') and EST_AF ='AFILIADO'"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # _______________________________________________iteraccion con la tabla de pagos____________________________________________________

    # retorna fecha, gestor y valor de pago de los tabla de pagos
    def pagos(self, caso):
        sql = "SELECT FECHA_SOLICITUD, COMERCIAL_RCC, VALOR_PAGO FROM pagos_realizados WHERE CASO= '{}'".format(
            caso)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # suma los pagos de una ot
    def Suma_pagos(self, caso):
        sql = "SELECT SUM(VALOR_PAGO) FROM pagos_realizados WHERE CASO= '{}'".format(
            caso)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # ____________________________________________interaccion con la tabla de pedidos______________________________________________________

    # retorna fecha, gestor y valor de los materiales de la tabla de pedidos

    def pedidos(self, caso):
        sql = "SELECT FECHA_SOLICITUD, COMERCIAL_RCC,valor_pago FROM pagos_realizados_proveedores WHERE CASO = '{}'".format(
            caso)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # suma el valor unitario de los materiales de una ot
    def Suma_pedidos(self, caso):
        sql = "SELECT SUM(valor_pago) FROM pagos_realizados_proveedores WHERE CASO = '{}'".format(
            caso)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # _________________________________interaccion con la tabla de usuario___________________________________________________________________________________

    def us(self, user):
        sql = "select nombre from usuarios where usuario = '{}'".format(user)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # ____________________________________interaccion con tabla de tecnicos__________________________________________________________________________________

    def validar_nombreTC(self, nombre):
        sql = f"SELECT  NOMBRE FROM TECNICOS WHERE NOMBRE ='{nombre}'"
        self.cursor.execute(sql)
        return bool(self.cursor.fetchall())
    
    def lista_de_nombresTC(self):
        sql = f"SELECT distinct NOMBRE FROM TECNICOS"
        self.cursor.execute(sql)
        lista = self.cursor.fetchall()
        resultado = []
        for i in lista:
            resultado.append(i[0])
        return resultado

    def CC_tecnico(self, nombre):
        sql = "SELECT distinct cc FROM tecnicos WHERE nombre = '{}'".format(
            nombre)
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        lista = []
        for i in resultado:
            lista.append(i)
        return lista

    def tlf_tecnico(self, nombre):
        sql = f"SELECT distinct telefono FROM tecnicos WHERE nombre = '{nombre}'"
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        lista = []
        for i in resultados:
            lista.append(i)
        return lista

    def regimen_tecnico(self, nombre):
        sql = f"SELECT distinct regimen FROM tecnicos WHERE nombre = '{nombre}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        lista = []
        for i in resultado:
            lista.append(i)
        return lista

    def eps_tecnico(self, nombre):
        sql = f"SELECT distinct eps FROM tecnicos WHERE nombre = '{nombre}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()[0]
        return resultado

    def pension_tecnico(self, nombre):
        sql = f"SELECT distinct pension FROM tecnicos WHERE nombre = '{nombre}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        return resultado[0]

    def caja_compensacion_tecnico(self, nombre):
        sql = f"SELECT  distinct caja_compensacion FROM tecnicos WHERE nombre = '{nombre}'"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchone()
        return resultado[0]
