
#Una máquina está entregando paquetes de 100 códigos, esos números o códigos están entre 1 y 500.
# Cada vez que se envía un paquete de 100 códigos la empresa tiene especial interés en los bits 3 y 5 estos deben estar en 0 y 1 respectivamente.
#Se van a enviar 20 paquetes en el intervalo de 1 hora.
#Se debe mostrar la ocurrencia de cada dato de interés durante 5 horas
#Se debe entregar una lista con la información requerida con resultado grafico de la tendencia
import numpy as np
import matplotlib.pyplot as po

def codigo():
    list_codigo=[]

    for a in range (100):
    
        
        list_codigo.append(np.random.randint(1,500))
        
    return list_codigo
po.plot(list_codigo)
po.show
infor=codigo ()

print ("los codigos establecidos son\n", infor)



