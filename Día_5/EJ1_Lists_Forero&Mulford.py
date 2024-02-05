import Día_5.MODULES.Modu5 as Name

T=int(input())
for case in range(T):
    text=input("")
    nums=input("")
    n=0
    k=0
    Interg=list()
    textList=text.split(" ")
    numsList=nums.split(" ")
    n=int(textList[0])
    k=int(textList[1])
    for p in range(n):
        num=int(numsList[p])
        Interg.append(abs(num))
    result=Name.check(Interg,n,k)
    print("Case {}:{}".format(case+1,result))

    ##Daniela Forero y Catalina Mulford :D