##1. Devuelve un listado con todos los pedidos que se han realizado.
##Los pedidos deien estar ordenados por la fecha de realización,
##mostrando en primer lugar los pedidos más recientes.

import json
import MODULES.Modu as Modu

from datetime import datetime as fecha
diccio_data=open("/home/user/Videos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)


pedidos=myData["ventas"]["pedidos"]
orden_fecha=sorted(pedidos, key=lambda order: fecha.strptime(order["fecha"],"%Y-%m-%d"),reverse=True)
for i in orden_fecha:
    a=i
    IDs=a["id"]
    totales=a["total"]
    fechas=a["fecha"]
    ID_client=a["id_cliente"]
    ID_commer=a["id_comercial"]
    ID_client=a["id_cliente"]
    print(Modu.infopedido(IDs,ID_client,totales,fechas,ID_commer))