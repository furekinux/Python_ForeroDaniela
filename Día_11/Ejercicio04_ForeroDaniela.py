##4. Devuelve un listado de todos los pedidos que se realizaron durante el
##año 2017, cuya cantidad total sea superior a 500€.

import json
import MODULES.Modu as Modu
from datetime import datetime as fecha

diccio_data=open("/home/user/Videos/FB/Python_ForeroDaniela/Día_10/data.json")
myData=json.load(diccio_data)
pedidos=myData["ventas"]["pedidos"]

lista_2017=[]
for i in range(len(pedidos)):
    ped=fecha.strptime(pedidos["fecha"],"%Y-%m-%d")

    if "%Y"==2017:
        lista_2017.append(ped)