def suma(num1,num2):
    rta=num1+num2
    return rta

def saludo(user_says):
    if user_says=="Hola":
        answer=print("Adios :)")
    return answer

def multiplicar(Num1,Num2):
    print("El resultado de la multiplicación es: ",(Num1*Num2))

def pingpong(ans,ans2):
    if ans=="Si":
        print("Computador: Ping")
        ans2=str(input("Su turno: "))
        if ans2=="Pong":
            print("Gracias por jugar :)")
        else:
            print("Game over :(")