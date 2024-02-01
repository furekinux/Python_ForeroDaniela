

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


num=int(input())

neg_num=negate(num)

if num<0:
    print("num:",num,"pos_num:",neg_num)
else:
    print("num:",num,"neg_num:",neg_num)

large_num(num)


##Errores del código enunciados abajo:

##Bugs:
## 1-El número positivo no retorna negativo en la función.
## 2-El número negativo clasifica como positivo y su positivo como negativo.
## 3-La función large_num no tiene condiciones, por lo tanto todos los números tendrán la misma respuesta.
## 4-Si el número ingresado es negativo, seguirá clasificando como pos_num.
 
exit()
def negate(num): ## El número no muestra el negativo en esta función
    return -num  ## -num no realiza alguna operación para generar el negativo

def large_num(num):
    res=(num>10000) ##No hay condición ni retorno

num=int(input())

negate(num)
neg_num=num
print("num:",num,"neg_num:",neg_num) ##Única respuesta sin tomar el caso de que el número sea negativo

big=large_num(num)
print("num is big:",num) ##Todos los numero son big porque no hay condición que diga lo contrario