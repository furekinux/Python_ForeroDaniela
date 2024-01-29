##Fibonacci

a=0##Valotes
b=1##Iniciales
d=1

def genfibo():
    while (n-1>d): ##Mientras d es menor que c repetir:
        a+b==a
        b+a==b
    print(a)
    print(b)
    d=d+1

print("Bienvenido usuario, por medio de este programa podrá generar la secuencia de fibonnaci")
rta=str(input("¿Empezar?"))
if rta=="Si":
  n=int(input("Ingrese la cantidad de pasos a generar: ")) ##El usuario ingresa la cantidad de numeros a generar
  genfibo()
  print("¿Desea agregar más digitos?")
  rta=str(input("RTA: "))
  if rta=="Si":
      n=int(input("Ingrese la cantidad de pasos a generar: ")) ##El usuario ingresa la cantidad de numeros a generar
      print(genfibo())
  else:
      print("Fin del proceso")

else:
  print("Fin del proceso")
##No corriò :(
