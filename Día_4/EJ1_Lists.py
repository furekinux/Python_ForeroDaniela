def nkCheck():
    if not 1<n<100001:
        exit()
    if not 0<k<501:
        exit()

from os import system,name
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")

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

x=1
y=2
def couple():
    (x,y)
    if not x==y and x<y:
        a=(x+y)/k
        if a==int:
            caseNum=caseNum+1
        
##Hecho por: Daniela Forero y Catalina Mulford :D
