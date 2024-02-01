def ntcheck(n,t):
    if 4<=n<=50:
        if 1<=t<=10:
           pass
        else:
           return exit()
    else:
        return exit()
    

nt=(input())
ntList=nt.split(" ")
n=int(ntList[0]) ##Types of coins
t=int(ntList[1]) ##Number of tables
ntcheck
VList=list()
LList=list()
for i in range(n):
    V=input("")
    VList.append(V)
print(VList)
for j in range(t):
    L=input("")
    LList.append(L)
