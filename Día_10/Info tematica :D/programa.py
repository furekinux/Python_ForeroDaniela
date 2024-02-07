import json

#Abrir un archivo externo (JSON) y convertirlo a DICCIONARIO

miVariable = open('info.json')
miJson=json.load(miVariable)

x = int(input('Ingresa un entero:'))
miJson['entero']=x
print(miJson)

#Convertir diccionario a Json
jsonFinal= json.dumps(miJson)

#Cojer el JSON y guardarlo en un archivo
with open('info.json','w') as outfile:
    outfile.write(jsonFinal)
