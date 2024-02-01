def C(x, ye):
    for i in range(x):
        n = int(input())
        ye.append(n)

def T(x, ye):
    for i in range(x):
        n = int(input())
        ye.append(n)

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

cont=bool

while cont:
    legita=[]
    coins = []
    table = []
    cosito = input()
    cc, ct = map(int, cosito.split())

    if cc == 0 and ct == 0:
        cont = False
    else:
        C(cc, coins)
        T(ct, table)

        if 4 <= len(coins) <= 50:
            pass
        else:
            exit()

        if 1 <= len(table) <= 10:
            pass 
        else:
            exit()
    mcd = mcd(cc, ct)
    mcm = mcm(cc, ct)
print(mcm,mcd)