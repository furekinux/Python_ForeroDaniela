def PrecioFinal(cantidad,precio):
    PF=cantidad*precio
    return PF


def negate(num): ##CORRECCIÓN CÓDIGO:
    if num>0:
        a=num*-1
        return a
    else:
        b=num*-1
        return b

def large_num(num):
    if (num>10000):
        print("num is big: ",num)
    elif (num<-10000):
        print("num is small: ",num)
    else:
        print("num isn't big: ",num)