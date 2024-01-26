##---------------------Funciones-----------------------

##Función con retorno y parámetros
##Esta función genera la suma de 2 números ingresados por el usuario :D
num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese otro número: "))
def suma(num1,num2):
    rta=num1+num2
    return rta
print("La suma de los dos números ingresados es: ",suma(num1,num2))


##Función con retorno y sin parámetros
##Esta función genera una respuesta al saludo del usuario ^^
print(" ")
user_says=str(input("-Hola! "))
def saludo():
    if user_says=="Hola":
        answer=print("Adios :)")
    return answer
(saludo())


##Función sin retorno y sin parámetros
##Esta función multiplica dos números ingresados por el usuario
print(" ")
def multiplicar():
    print("El resultado de la multiplicación es: ",(Num1*Num2))
print("Ingrese dos números para generar el resultado de su multiplicación")
Num1=int(input("Número uno: "))
Num2=int(input("Número dos: "))
multiplicar()


##Función sin retorno y con parámetros
##Juego de pingpong
print(" ")
ans=str(input("¿Iniciar ping-pong? "))
ans2=str
def pingpong(ans,ans2):
    if ans=="Si":
        print("Computador: Ping")
        ans2=str(input("Su turno: "))
        if ans2=="Pong":
            print("Gracias por jugar :)")
        else:
            print("Game over :(")
pingpong(ans,ans2)
##Realizado por: Daniela Forero Ballén - T.I. 1142714225
