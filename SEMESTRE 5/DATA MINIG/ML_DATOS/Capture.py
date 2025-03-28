import requests
from pymongo.mongo_client import MongoClient

class CapturaDatos:
    def __init__(self):
        self.dataJson = []
        self.jsonPrepared = []
        # Conexión a MongoDB
        self.client = MongoClient("mongodb+srv://moshezabacruz:Moshe21@cluster0.lq65f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # Cambia esto por tu URI
        self.db = self.client["moshe_DB"]  # Reemplaza por tu nombre de base de datos
        self.collection = self.db["moshe_datos2"]  # Reemplaza por tu nombre de colección

    def Captura(self):
        resultado_busqueda = requests.get(f"https://www.datos.gov.co/resource/m5pi-7cau.json")
        self.dataJson = resultado_busqueda.json()


    def limpieza(self):
        for ind in range(len(self.dataJson)):
            jsonClean = {
                "Year": "",
                "Quarter": "",
                "Provider": "",
                "Income": "",
                "amountSMS":""
            }
            if self.dataJson[ind]['proveedor'] == "ALMACENES EXITO INVERSIONES S.A.S.":
                jsonClean['Provider'] = "MOVIL EXITO"
            elif self.dataJson[ind]['proveedor'] == "AVANTEL S.A.S":
                jsonClean['Provider'] = "WOM"
            elif self.dataJson[ind]['proveedor'] == "VIRGIN MOBILE COLOMBIA S.A.S.":
                jsonClean['Provider'] = "VIRGIN MOBILE"
            elif self.dataJson[ind]['proveedor'] == "SUMA MOVIL S.A.S.":
                jsonClean['Provider'] = "SUMA MOVIL"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA MOVIL  S.A ESP":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "LOGISTICA FLASH COLOMBIA S.A.S":
                jsonClean['Provider'] = "FLASH"
            elif self.dataJson[ind]['proveedor'] == "COMUNICACION CELULAR S A COMCEL S A":
                jsonClean['Provider'] = "CLARO"
            elif self.dataJson[ind]['proveedor'] == "EMPRESA DE TELECOMUNICACIONES DE BOGOTA S.A. ESP":
                jsonClean['Provider'] = "ETB"
            elif self.dataJson[ind]['proveedor'] == "SETROC MOBILE GROUP SAS":
                jsonClean['Provider'] = "SETROC"
            elif self.dataJson[ind]['proveedor'] == "PARTNERS TELECOM COLOMBIA SAS":
                jsonClean['Provider'] = "PARTNERS"
            elif self.dataJson[ind]['proveedor'] == "LIWA SAS ESP":
                jsonClean['Provider'] = "LIWA"
            elif self.dataJson[ind]['proveedor'] == "LOV TELECOMUNICACIONES SAS":
                jsonClean['Provider'] = "LOV"
            elif self.dataJson[ind]['proveedor'] == "UFF MOVIL SAS":
                jsonClean['Provider'] = "UFF"
            elif self.dataJson[ind]['proveedor'] == "COLOMBIA TELECOMUNICACIONES S.A. E.S.P.":
                jsonClean['Provider'] = "MOVISTAR"
            jsonClean['Year'] = self.dataJson[ind]['anno']
            jsonClean['Quarter'] = self.dataJson[ind]['trimestre']
            jsonClean['Income'] = self.dataJson[ind]['ingresos_por_mensajes']
            jsonClean['amountSMS'] = self.dataJson[ind]['cantidad_de_mensajes']
            self.jsonPrepared.append(jsonClean)
        return self.jsonPrepared

    def enviar_a_mongodb(self):
        # Inserta los datos en MongoDB
        if self.jsonPrepared:
            self.collection.insert_many(self.jsonPrepared)
            print("Datos enviados a MongoDB.")

# Crear una instancia de la clase y ejecutar los métodos
captura_datos = CapturaDatos()
captura_datos.Captura()
captura_datos.limpieza()
captura_datos.enviar_a_mongodb()




