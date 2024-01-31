def check(Interg,n,k):
    pairs=set()
    for i in range(n):
        for j in range(i+1,n):
            if(Interg[i]+Interg[j])%k==0:
                pairs.add((min(Interg[i],Interg[j]),max(Interg[i],Interg[j])))
    return len(pairs)

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
    result=check(Interg,n,k)
    print("Case {}:{}".format(case+1,result))

    ##Daniela Forero y Catalina Mulford :D