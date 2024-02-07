Diccio={'Nombre':'Ella','Edad':20,'Barrio':'Zapamanga'}
print(Diccio)
print(type(Diccio))
print(Diccio['Nombre'])
Diccio['Nombre']="Jhon"##CAMBIA NOMBRE O ITEM
print(Diccio)
print(type(Diccio))
print(Diccio['Nombre'])

##recorrer Diccio
for i in Diccio:
    print(i)

##Valor * valor :D
for valor in Diccio:
    print(Diccio[valor])

for llave,valor in Diccio.items():
    print(llave,valor)

print("··························")
##CLEAR() limpia diccio

## BORRA LLAVES --> Diccio.pop("LLAVE")
## BORRA ITEMS --> Diccio.popitem("ITEM")

##CRUZAR DICCIOS (REEMPLAZA LAS LLAVES)
Diccio2={'Edad':23,'Barrio':'Ruitoque'}
Diccio.update(Diccio2)
print(Diccio)
