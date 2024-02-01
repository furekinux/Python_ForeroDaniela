#Creación de Diccionario - {llave1:valor1,llave2:valor2}
diccionario = {'Nombre':("Danna","Mozo","Andres"),"Edad":17,"Barrio":"Zapamanga"}
print(diccionario)
print(type(diccionario))

#Buscar valor de x llave del diccionario y buscar 
#el segundo dato que contiene la subdiccionario
print(diccionario['Nombre'][1])
diccionario['Nombre']="Danna"
print(diccionario)
print(type(diccionario))
print(diccionario['Nombre'])

#Recorrer un Diccionario por llaves
for i in diccionario:
    print(i)

#Recorrer un Diccionario por valor 
for valor in diccionario:
    print(diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in diccionario.items():
    print(llave,valor)