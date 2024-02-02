#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO
  
import Modu6 as Hi

Diccio={"Productos":("Alimento Perros 25Kg(AD)","Alimento Gatos 20Kg(AC)","Alimento Peces Tarro 0,1Kg(AF)"),"Precios":(25000,24500,52000)}

a=Diccio["Productos"]
b=Diccio["Precios"]
print("Bienvenido usuario, ¿Que producto busca para su mascota?")
print(f"Productos disponibles: {a}")
rta=input("\nAgregue la cantidad despues del elemento: ")
rtaList=rta.split(" ")
producto=str(rtaList[0])
cantidad=int(rtaList[1])

while producto!="AD" and producto!="AC" and producto!="AF":
    print("Este producto no està disponible.")
    producto=input("Volver a intentar producto: ")

if producto=="AD":
    precio=(b[0])
    producto=a[0]
elif producto=="AC":
    precio=(b[1])
    producto=a[1]
elif producto=="AF":
    precio=(b[2])
    producto=a[2]
    
print(f"El elemento seleccionado es: {producto}.")

print(f"\nEl precio a pagar es: ${Hi.PrecioFinal(cantidad,precio)}")

##Hecho por Daniela Forero Ballén 1142714225*