from os import system,name
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")

def nkCheck():
    if not 1<n<100001:
        exit()
    if not 0<k<501:
        exit()

def couple():
        (b[i],b[i])
        if not b[i]==b[i+1] and b[i+1]<b[i+1]:
            a=(b[i]+b[i])/k
            if a==int:
                caseNum=caseNum+1
            else:
                caseNum=caseNum+0
def couples(b):
    for i in range(0,len(b)-1,2):
        (b[i],b[i+1])
        print(f"{b[i],b[i+1]}")
        i+1
        if i>n:
           print("")
           break
        
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
    nkCheck
    aaa=input("")
    b=[*aaa]
    for l in range(n):
        dataA=int(b[l])
        b[l]=dataA
        l=l+1
    clear()
    print(f"{T}\n{n} {k}")
    print(b)
    couples(b)
    
    print
##Hecho por: Daniela Forero y Catalina Mulford :D
