def calcular_definitiva(lista):
    lista[0]=lista[0]*0.3
    lista[1]=lista[1]*0.3
    lista[2]=lista[2]*0.4
    sumatoria=0
    for i in range(len(lista)):
        sumatoria=sumatoria+lista[i]

    return sumatoria

def notamayo(lista2):
    if notaMayor==lista[2]:
        print("Tu nota mayor es:",notaMayor," = ",((notaMayor*100)/40))
    elif notaMayor==lista[0] or notaMayor==lista[1]:
        print("Tu nota mayor es:",notaMayor," = ",((notaMayor*100)/30))
    else:
        print("No reconoce :(")
    
for i in range(5):
    print("\nEstudiante#",i+1)
    lista=[]
    notaMayor=0
    definitiva=0
    for i in range(3):
        if(i==2):
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+numerito
            lista.append(numerito)
        else:
            numerito=(float(input("Ingresa tu nota:")))
            print(numerito)
            definitiva=definitiva+numerito
            lista.append(numerito)
    
    for i in range(2): ##NOTA MAYOOOOOOOOOOOOOOOOOOOOOOOR :D!!!!
        if lista[i]>lista[i+1]:
           notaMayor=lista[i]
        else:
            notaMayor=lista[i+1]
        i=i+1
    lista2=lista
    print(lista)
    notamayo(lista2)
    
    definitiva=calcular_definitiva(lista)
    print("Tu definitiva es:",definitiva)
    if(definitiva<2):
        print("Perdiste tu vida.") ##NO PASA
    elif (definitiva<3):
        print("Pues... todo bien...recupera") ##PASA (?)
    elif(definitiva>4.5):
        print("Excelente estudiante! Sos ejemplar") ##PASA
    print(lista)

    