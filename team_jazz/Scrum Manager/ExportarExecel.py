from Data_Base import conexion
import openpyxl
import pandas as pd
from tkinter import filedialog

class Exportar_Base_Datos:
    def __init__(self, variable, usuario):
        self.tabla = variable
        self.usuario = usuario
        self.guardar_excel()

    def guardar_excel(self):
    # Crear un nuevo libro de trabajo de Excel
        libro = openpyxl.Workbook()
        hoja = libro.active

        # Agregar datos de ejemplo a la hoja
        exportar = conexion()
        if self.usuario !="": 
            if self.tabla == "FINALIZADOS":
                lista_BD = exportar.ExportarDBExcel()
            elif self.tabla == "DESASIGNADOS":
                lista_BD = exportar.Exportar_facturadas()
            elif self.tabla =="SEGUIMIENTO":
                lista_BD = exportar.Exportar_desasignadas()
            elif self.tabla =="":
                lista_BD = exportar.Exportar_BD_gestor(self.usuario)
                
        hoja.append(('CASO', 'FECHA', 'MES', 'AÑO', 'CLIENTE', 'DENOMINACION', 'CIUDAD_SEDE', 'TERRITORIAL', 'ESTADO_RCC', 'OC', 'OC_FISICA', 'EM', 'ESTADO_SAP', 'GESTOR', 'COMENTARIO','SINTOMA', 'TECNICO', 'FECHA_INICIO_EJECUCION', 'FECHA_FINAL_EJECUCION', 'MANO_OBRA', 'MATERIAL', 'PARAFISCALES', 'COSTO_TOTAL', 'SUBTOTAL_SAP', 'IVA','TOTAL_IVA', 'COMISION_OTROS', 'UTILIDAD_BRUTA', 'PORCENTAJE_UB', 'RTE_FUENTE','RTE_IVA', 'RTE_ICA', 'PAGO_FINAL', 'UTILIDAD_NETA', 'PORCENTA_UN', 'FACTURA_VENTA', 'FECHA_FACTURA'))
        for caso in lista_BD:
            hoja.append((caso['CASO'], caso['FECHA'], caso['MES'], caso['AÑO'], caso['CLIENTE'], caso['DENOMINACION'], caso['CIUDAD_SEDE'], caso['TERRITORIAL'], caso['ESTADO_RCC'],caso['OC'],caso['OC_FISICA'],caso['GESTOR'],caso['COMENTARIO'],caso['SINTOMA'],caso['TECNICO'],caso['FECHA_INICIO_EJECUCION'],caso['MANO_OBRA'],caso['MATERIAL'],caso['PARAFISCALES'],caso['COSTO_TOTAL'],caso['SUBTOTAL_SAP'],caso['IVA'], caso['TOTAL_IVA'], caso['COMISION_OTROS'], caso['UTILIDAD_BRUTA'], caso['PORCENTAJE_UB'], caso['RTE_FUENTE'], caso['RTE_IVA'], caso['RTE_ICA'], caso['PAGO_FINAL'], caso['UTILIDAD_NETA'], caso['PORCENTA_UN'],caso['FACTURA_VENTA'],caso['FECHA_FACTURA']))


        # Obtener la ubicación y el nombre del archivo de destino
        archivo_guardar = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos de Excel", "*.xlsx")])

        if archivo_guardar:
            # Guardar el libro de trabajo en el archivo seleccionado
            libro.save(archivo_guardar)
            libro.close()
            
