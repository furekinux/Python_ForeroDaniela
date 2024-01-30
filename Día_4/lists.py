def nkCheck():
    if not 1<n<100001:
        exit()
    if not 0<k<501:
        exit()

T=(int(input()))
if 0>T>100:
     exit()
else:
    nk=input("")
    a=[*nk]
    for i in range(2):
        data=int(a[i])
        a[i]=data
    print(a)
    n=2
    k=3
    nkCheck

