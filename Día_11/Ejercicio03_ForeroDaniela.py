##3. Devuelve un listado con los identificadores de los clientes
##que han realizado algún pedido. Tenga en cuenta que no debe mostrar
##identificadores que estén repetidos.

import json
import MODULES.Modu as Modu

diccio_data=open("/home/user/Vídeos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)

pedidos=myData["ventas"]["pedidos"]
clientes_info=myData["ventas"]["clientes"]
for i in range(len(pedidos)):
    a=pedidos[i]
    IDs=a["id"]
    ID_client=a["id_cliente"]
    for j in range(len(clientes_info)):
        b=clientes_info[j]
        
        IDc=b["id"]
        if ID_client==IDc:
            print(f"\n[ID CLIENTE: {IDc}]\n{clientes_info[j]}\n")
            if 
        else:
            j=j+1

