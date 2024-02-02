##---------------------Funciones-----------------------

import Modu1 as XD

##Función con retorno y parámetros
##Esta función genera la suma de 2 números ingresados por el usuario :D
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))

print("La suma de los dos números ingresados es: ",XD.suma(num1,num2))

##Función con retorno y sin parámetros
##Esta función genera una respuesta al saludo del usuario ^^
print(" ")
user_says=str(input("-Hola! "))

XD.saludo(user_says)

##Función sin retorno y sin parámetros
##Esta función multiplica dos números ingresados por el usuario
print(" ")

print("Ingrese dos números para generar el resultado de su multiplicación")
Num1=int(input("Número uno: "))
Num2=int(input("Número dos: "))
XD.multiplicar(Num1,Num2)


##Función sin retorno y con parámetros
##Juego de pingpong
print(" ")
ans=str(input("¿Iniciar ping-pong? "))
ans2=str

XD.pingpong(ans,ans2)
##Realizado por: Daniela Forero Ballén - T.I. 1142714225
