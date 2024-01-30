def nkCheck():
    if not 1<n<100001:
        exit()
    if not 0<k<501:
        exit()

from os import system,name
import random
def clear():
    if name=="nt":
        _=system("cls")
    else:
        _=system("clear")

T=666
if 0>T>100:
     exit()
else:
    n=12
    k=6
    nkCheck
    b=[1,-5,-1,-6,10,-10,-10,7,10,-7,0,7]
    print(f"{T}\n{n} {k}\n{b}")
    for i in range(12-1):
        data=int(b[i])
        b[i]=data
        i=i+1