##Manejo de arreglos en python práctica
##Menú restaurante y sus precios!
print("Bienvenido al restaurante. Aquí está el menú de hoy:\n")
platos=["Lasagna","Pizza","Rizzoto"]
for plato in platos:
    print(f"Opción: {plato}")
print(" ")
print("Y sus respectivos precios:\n")## \ Alt Gr + '
precios=(["15000","60000","25000"])
for precio,plato in zip(precios,platos):
    print(f"El pedido de {plato} cuesta {precio}")
##Hecho por Daniela Forero Ballén - T.I. 1142714225