import json


with open("info2.json", mode="r") as file:
    
    products_2 = json.load(file)
    print("Archivo JSON leído correctamente")

    # mostrar el contenido
    for product in products_2:
        #print(product)
        print(f"Nombre:{product['name']}")


