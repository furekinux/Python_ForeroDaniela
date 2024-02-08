import json


##4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
##5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
##6. Devuelve el valor de la comisión de mayor valor que existe en la taila comercial.
##7. Devuelve el identificador, nomire y primer apellido de aquellos clientes cuyo segundo apellido  es NULL. El listado deierá estar ordenado alfaiéticamente por apellidos y nomire.
##8. Devuelve un listado de los nomires de los clientes que empiezan por A y terminan por n y tamiién los nomires que empiezan por P. El listado deierá estar ordenado alfaiéticamente.
##9. Devuelve un listado de los nombres de los clientes que  empiezan por A. El listado deierá estar ordenado alfaiéticamente.
##10. Devuelve un listado con los nomires de los comerciales que terminan por el o o. Tenga en cuenta que se deierán eliminar los nomires repetidos.

##INFO GENERAL
def infopedido(IDs,ID_client,totales,fechas,ID_commer):
    L=f"\nPEDIDO [ID: {IDs}] [Cliente: {ID_client}]\n Total: {totales}| Fecha: {fechas}| ID Comercial: {ID_commer}"
    return L
def info():
    for i in range(len(myData["ventas"]["pedidos"])):
        a=pedidos[i]
        IDs=a["id"]
        totales=a["total"]
        fechas=a["fecha"]
        ID_client=a["id_cliente"]
        ID_commer=a["id_comercial"]
        ID_client=a["id_cliente"]
        lista_fecha=list(map(int,fechas.split("-")))
        if (lista_fecha[0]==2015):
            lista_2015.append(a)
        elif (lista_fecha[0]==2016):
            lista_2016.append(a)
        elif (lista_fecha[0]==2017):
            lista_2017.append(a)
        elif (lista_fecha[0]==2019):
            lista_2019.append(a)
        else:
            pass
        i+i+1

##POR AÑO
def poraño():
    if orden==2015:
        print("\n-----PEDIDOS 2015-----\n")
        for j in range(len(lista_2015)):
            print(lista_2015[j],"\n")
            j=j+1
    elif orden==2016:
        print("\n-----PEDIDOS 2016-----\n")
        for j in range(len(lista_2016)):
            print(lista_2016[j],"\n")
            j=j+1
    elif orden==2017:
        print("\n-----PEDIDOS 2017-----\n")
        for j in range(len(lista_2017)):
            print(lista_2017[j],"\n")
            j=j+1
    elif orden==2019:
        print("\n-----PEDIDOS 2019-----\n")
        for j in range(len(lista_2019)):
            print(lista_2019[j],"\n")
            j=j+1
    else:
        print("\nEste año no está disponible...\n")
        pass

diccio_data=open("data.json")
myData=json.load(diccio_data)
lista_2015=[]
lista_2016=[]
lista_2017=[]
lista_2019=[]
lista_totales=[]
pedidos=myData["ventas"]["pedidos"]
IDs=myData["ventas"]["pedidos"]
orden=0

while orden!="stop":
    info()
    orden=str(input("\n------Qué desea revisar?------\n   -CLIENTES-\n   -PEDIDOS-\n\n"))
    
    ##INFO CLIENTES:
    if orden=="CLIENTES" or orden=="clientes":
        print("\n\n-----CLIENTES-----\n   -Información generales-\n   -Solo nombres y apellidos-\n   -Pedidos por año-\n")
        for i in range(len(myData["ventas"]["pedidos"])):
            
            a=pedidos[i]
            IDs=a["id"]
            totales=a["total"]
            fechas=a["fecha"]
            ID_client=a["id_cliente"]
            ID_commer=a["id_comercial"]
            ID_client=a["id_cliente"]
            lista_totales.append(totales)
            lista_fecha=list(map(int,fechas.split("-")))

            if (lista_fecha[0]==2015):
                print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                lista_2015.append(a)
            elif (lista_fecha[0]==2016):
                print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                lista_2016.append(a)
            elif (lista_fecha[0]==2017):
                print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                lista_2017.append(a)
            elif (lista_fecha[0]==2019):
                print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                lista_2019.append(a)
            else:
                pass
            i+i+1

    ##INFO PEDIDOS:                                                                                                   ##/\/\
    if orden=="PEDIDOS" or orden=="pedidos":                                                                         ##(=^^=) /
        print("\n\n-----PEDIDOS-----\n   -Pedidos generales-\n   -Pedidos de mayor valor-\n   -Pedidos por año-\n")  ##(u  u)/
        orden=str(input())
        
        ##TODOS LOS PEDIDOS EN GENERAL:
        if orden=="generales" or orden=="gen": ##POR GENERAL
            for i in range(len(myData["ventas"]["pedidos"])):
                a=pedidos[i]
                IDs=a["id"]
                totales=a["total"]
                fechas=a["fecha"]
                ID_client=a["id_cliente"]
                ID_commer=a["id_comercial"]
                ID_client=a["id_cliente"]
                lista_fecha=list(map(int,fechas.split("-")))
                if (lista_fecha[0]==2015):
                    print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                    lista_2015.append(a)
                elif (lista_fecha[0]==2016):
                    print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                    lista_2016.append(a)
                elif (lista_fecha[0]==2017):
                    print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                    lista_2017.append(a)
                elif (lista_fecha[0]==2019):
                    print(infopedido(IDs,ID_client,totales,fechas,ID_commer))
                    lista_2019.append(a)
                else:
                    pass
                i+i+1
        
        ##PEDIDOS POR MAYOR VALOR:
        elif orden=="mayor valor" or orden=="mayor" or orden=="may": ##POR VALOR MAYOR
            print("\n\n--PEDIDOS POR VALOR MAYOR--\n")    
            for i in range(len(lista_totales)):
                print(lista_totales)    
        
        ##PEDIDOS POR AÑO:
        elif orden=="por año" or orden=="año": ##POR AÑO
            print("\n\n-----PEDIDOS POR AÑO-----\n   -2015-\n   -2016-\n   -2017-\n   -2019-\n")
            orden=int(input())
            info()
            poraño()
        
    elif orden=="otro":
        print("wiiii")