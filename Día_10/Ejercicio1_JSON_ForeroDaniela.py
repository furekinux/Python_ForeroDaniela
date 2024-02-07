import json

##1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.
##2. Devuelve todos los datos de los dos pedidos de mayor valor.
##3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.
##4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
##5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
##6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
##7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo segundo apellido  es NULL. El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
##8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P. El listado deberá estar ordenado alfabéticamente.
##9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deberá estar ordenado alfabéticamente.
##10. Devuelve un listado con los nombres de los comerciales que terminan por el o o. Tenga en cuenta que se deberán eliminar los nombres repetidos.


diccio_data=open("data.json")
myData=json.load(diccio_data)

pedidos=myData["ventas"]["pedidos"]
IDs=myData["ventas"]["pedidos"]
orden=str(input("Qué desea revisar?\n   -Add...-\n   -PEDIDOS-\n"))
if orden=="PEDIDOS" or orden=="pedidos":
    print("   -Pedidos generales-\n   -Pedidos de mayor valor-")
    select=str(input())
    if select=="generales" or select=="gen":
        for i in range(len(myData["ventas"]["pedidos"])):
            a=pedidos[i]
            IDs=a["id"]
            totales=a["total"]
            fechas=a["fecha"]
            lista_fecha=fechas.split("-")
            ID_client=a["id_cliente"]
            ID_commer=a["id_comercial"]
            ID_client=a["id_cliente"]
            for a in len(myData["ventas"]["pedidos"]):
                if (lista_fecha[0]==2015):
                    print(f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}")
                else:
                    a=a+1
            for i in range(len(myData["ventas"]["pedidos"])):
                if (lista_fecha[0]==2016):
                    print(f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}")
                else:
                    i+i+1
            for i in range(len(myData["ventas"]["pedidos"])):
                if (lista_fecha[0]==2017):
                    print(f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}")
                else:
                    i+i+1
            for i in range(len(myData["ventas"]["pedidos"])):
                if (lista_fecha[0]==2019):
                    print(f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}")
                else:
                    i+i+1
            i+i+1
    elif select=="add":
        print("WIP")
elif orden=="otro":
    print("wiiii")