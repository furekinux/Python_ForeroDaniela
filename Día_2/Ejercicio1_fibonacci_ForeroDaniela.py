##Fibonacci
import Modulo2 as XD
a=0##Valotes
b=1##Iniciales
d=1


print("Bienvenido usuario, por medio de este programa podrá generar la secuencia de fibonnaci")
rta=str(input("¿Empezar?"))
if rta=="Si":
  n=int(input("Ingrese la cantidad de pasos a generar: ")) ##El usuario ingresa la cantidad de numeros a generar
  XD.genfibo(a,b,n,d)
  print("¿Desea agregar más digitos?")
  rta=str(input("RTA: "))
  if rta=="Si":
      n=int(input("Ingrese la cantidad de pasos a generar: ")) ##El usuario ingresa la cantidad de numeros a generar
      print(XD.genfibo(a,b,n,d))
  else:
      print("Fin del proceso")

else:
  print("Fin del proceso")
##No corriò :(
