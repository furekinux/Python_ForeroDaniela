from os import system,name
import Día_4.MODULES.Modu4 as uwu

        
##FUNCIONES ARRIBA---^

T=(int(input()))
if 0>T>100:
     exit()
else:
    nk=input("")
    a=[*nk]
    for i in range(2):
        data=int(a[i])
        a[i]=data
        i=i+1
        n=int(a[0])
        k=int(a[1])
    uwu.nkCheck(n,k)
    aaa=input("")
    b=[*aaa]
    for l in range(n):
        dataA=int(b[l])
        b[l]=dataA
        l=l+1
    uwu.clear(name,system)
    print(f"{T}\n{n} {k}")
    print(b)
    uwu.couples(b,n)
    exit()
##Hecho por: Daniela Forero y Catalina Mulford :D
