def infopedido(IDs,ID_client,totales,fechas,ID_commer):
    L=f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}"
    return L
import json

from datetime import datetime as fecha
diccio_data=open("/home/user/Vídeos/FB/Python_ForeroDaniela-1/Día_10/data.json")
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
    print(infopedido(IDs,ID_client,totales,fechas,ID_commer))