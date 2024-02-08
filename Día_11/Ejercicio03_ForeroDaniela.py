##3. Devuelve un listado con los identificadores de los clientes
##que han realizado algún pedido. Tenga en cuenta que no debe mostrar
##identificadores que estén repetidos.

import json
import MODULES.Modu as Modu

diccio_data=open("/home/user/Videos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)
j=0
pedidos=myData["ventas"]["pedidos"]
clientes_info=myData["ventas"]["clientes"]
for i in range(len(pedidos)):
    a=pedidos[i]
    b=clientes_info[j]
    IDs=a["id"]
    IDc=b["id"]
    totales=a["total"]
    fechas=a["fecha"]
    ID_client=a["id_cliente"]
    ID_commer=a["id_comercial"]
    ID_client=a["id_cliente"]
    if ID_client==IDc:
        print(f"[ID CLIENTE: {ID_client}]\n{pedidos[i]}\n\n[ID CLIENTE: {IDc}]\n{clientes_info[i]}\n")
        j=j+1
    else:
        j=j+1
        pass


