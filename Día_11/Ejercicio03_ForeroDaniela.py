##3. Devuelve un listado con los identificadores de los clientes
##que han realizado algún pedido. Tenga en cuenta que no debe mostrar
##identificadores que estén repetidos.

import json
import MODULES.Modu as Modu

diccio_data=open("/home/user/Vídeos/FB/Python_ForeroDaniela-1/Día_10/data.json")
myData=json.load(diccio_data)

pedidos=myData["ventas"]["pedidos"]
clientes_info=myData["ventas"]["clientes"]
for i in range(len(pedidos)):
    a=pedidos[i]
    IDs=a["id"]
    totales=a["total"]
    fechas=a["fecha"]
    ID_client=a["id_cliente"]
    ID_commer=a["id_comercial"]
    ID_client=a["id_cliente"]
    if pedidos["id_cliente"]==clientes_info["id"]:
        print(Modu.infopedido(IDs,ID_client,totales,fechas,ID_commer))