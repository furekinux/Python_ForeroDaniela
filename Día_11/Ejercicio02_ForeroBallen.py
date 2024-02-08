##2. Devuelve todos los datos de los dos pedidos de mayor valor.

import json
import MODULES.Modu as Modu

diccio_data=open("/home/user/Videos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)
pedidos=myData["ventas"]["pedidos"]
lista_totales=[]
orden=sorted(pedidos,key=lambda order: order["total"], reverse=True)

for i in orden:
    a=i
    IDs=a["id"]
    totales=a["total"]
    fechas=a["fecha"]
    ID_client=a["id_cliente"]
    ID_commer=a["id_comercial"]
    ID_client=a["id_cliente"]
    print(Modu.infopedido(IDs,ID_client,totales,fechas,ID_commer))