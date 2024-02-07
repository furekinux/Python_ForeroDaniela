import json

diccio_data=open("data.json")
myData=json.load(diccio_data)

pedidos=myData["ventas"]["pedidos"]
IDs=myData["ventas"]["pedidos"]
orden=str(input("Qué desea revisar?\n   -Add...-\n   -PEDIDOS-\n"))
if orden=="PEDIDOS" or orden=="pedidos":
    print("   -Pedidos generales-\n   -Pedidos de mayor valor-")
    select=str(input())
    if select=="generales":
        for i in range(len(myData["ventas"]["pedidos"])):
            a=pedidos[i]
            IDs=a["id"]
            totales=a["total"]
            fechas=a["fecha"]
            ID_client=a["id_cliente"]
            ID_commer=a["id_comercial"]
            print(f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}")
elif orden=="otro":
    print("wiiii")