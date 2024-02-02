def check(Interg,n,k):
    couples=set()
    for i in range(n):
        for j in range(i+1,n):
            if(Interg[i]+Interg[j])%k==0:
                couples.add((min(Interg[i],Interg[j]),max(Interg[i],Interg[j])))
    return len(couples)