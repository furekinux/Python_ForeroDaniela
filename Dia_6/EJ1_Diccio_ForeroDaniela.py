#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO
  
def PrecioFinal():
    PF=cantidad*precio
    return PF

Diccio={"Productos":("Alimento Perros 25Kg(AD)","Alimento Gatos 20Kg(AC)","Alimento Peces Tarro 0,1Kg(AF)"),"Precios":(25000,24500,52000)}
a=Diccio["Productos"]
b=Diccio["Precios"]
print("Bienvenido usuario, ¿Que producto busca para su mascota?")
print(f"Productos disponibles: {a}\nAgregue la cantidad despues del elemento")
rta=input()
rtaList=rta.split(" ")
producto=str(rtaList[0])
if producto=="AD":
    precio=(b[0])
    producto=a[0]
else:
    if producto=="AC":
        precio=(b[1])
        producto=a[1]
    else:
        if producto=="AF":
            precio=(b[2])
            producto=a[2]
        else:
            exit()
cantidad=int(rtaList[1])
print(f"El elemento seleccionado es: {producto}.")
print(PrecioFinal())