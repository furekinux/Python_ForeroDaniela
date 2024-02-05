import Día_6.MODULES.Modu6 as Wi

num=int(input())

neg_num=Wi.negate(num)

if num<0:
    print("num:",num,"pos_num:",neg_num)
else:
    print("num:",num,"neg_num:",neg_num)

Wi.large_num(num)


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