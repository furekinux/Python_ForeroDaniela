##---------------------------------------------
##--------------- Ejercicio #1 ----------------
##---------------------------------------------

# Impresión en consola
print("Hello, world!^w^")

# -------- Datos primitivos --------
print(" ")
#1. String
texto="Campus!"
print(texto)
print(type (texto))
print(" ")
#2. Int
numEnt=24
print(numEnt)
print(type(numEnt))
print(" ")
#3. Double
numDec=2.0
print(numDec)
print(type(numDec))
print(" ")
#4. Float
numDecLar=3.141516
print(numDecLar)
print(type(numDecLar))
print(" ")
#5. Boolean
print(True)
print(type(True))
print(" ")

#--------Entradas * parte del usuario con/sin def de tipo de dato primitivo----------
entradausuarioNumero=int(input("Enter your age:"))
#o
numeroFinal=int(entradausuarioNumero)
print(" ")
print("Your age is: ",entradausuarioNumero,"!")

#----- Ciclos :3 -----

#Ciclo For(Para)
for i in range(5,10,3):#for contador in range (Desde,Hasta,Pasos)
    print(i)

#Ciclo while
Boool=True
while Boool==True: #While condición a cumplir :
    print("Sigo vivo(Bait)")
    Boool=False

#----- Condicionales -----
texto2="Wumpus"
if texto2=="Wumpus":
    print("Soy camper")
else:
    print("No soy camper :(")

##Desarrollado por DANIELA FORERO BALLÉN - 1142714225
