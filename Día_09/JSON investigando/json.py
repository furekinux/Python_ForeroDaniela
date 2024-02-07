import json
##TODO parte de un intermediario
diccio={"entero":5,"cadena":"Hola","lista":[1,2,3,"si"]} ##serializar
##Dato primitivo a objeto JSON:
json_diccio=json.dumps(diccio) ## llega modo "texto"
##--v
##Castear o serializar para usar de json a py y viceversa
##--^
##Objeto Json a Dato primitivo:
python_diccio=json.loads(json_diccio) ## se convierte en {diccio}
print(python_diccio)