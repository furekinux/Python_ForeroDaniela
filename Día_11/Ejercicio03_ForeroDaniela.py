##3. Devuelve un listado con los identificadores de los clientes
##que han realizado algún pedido. Tenga en cuenta que no debe mostrar
##identificadores que estén repetidos.

import json
import MODULES.Modu as Modu

diccio_data=open("/home/user/Vídeos/FB/Python_ForeroDaniela-1/Día_10/data.json")
myData=json.load(diccio_data)