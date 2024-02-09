##4. Devuelve un listado de todos los pedidos que se realizaron durante el
##año 2017, cuya cantidad total sea superior a 500€.

import json
import MODULES.Modu as Modu
from datetime import datetime as fecha

diccio_data=open("/home/user/Vídeos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)
pedidos=myData["ventas"]["pedidos"]

lista_2017=[]
ped_list=[]
for i in range(len(pedidos)):
    a=pedidos[i]
    IDs=a["id"]
    totales=a["total"]
    fechas=a["fecha"]
    ID_client=a["id_cliente"]
    ID_commer=a["id_comercial"]
    ID_client=a["id_cliente"]
    ped_list=a["fecha"].split("-")
    if ped_list[0]=="2017" and a["total"]>500:
        print(Modu.infopedido(IDs,ID_client,totales,fechas,ID_commer))
    else:
        pass