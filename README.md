# Taller Práctico

## Introduction

El objetivo de esta practica es comenzar a utilizar python con mongo, para ello usarermos una libreria llamada pymongo.
Para ello importaremos datos mock sobre usuarios de una aplicación. Lo podeis encontrar en el fichero [MOCK_DATA.json](MOCK_DATA.json)

Informacion UTIL para la práctica : [pymongo docs](https://api.mongodb.com/python/current/tutorial.html#making-a-connection-with-mongoclient)

### Apartado 0
Preparando el entorno
```bash

python3 -m venv myvenv
source myvenv/bin/activate
pip install pymongo
or
pip install -r requirements.txt

```


### Apartado 1
	Importar los datos a una base datos llamada upsa1 en la collecion users
	Se puede usar mongoimport o este fragmento de código python (recomiendo usar el código para aprender a importar desde python)
	
```python
MONGO_HOST = "127.0.0.1:27017"
def import_json(database, collection):
    client = MongoClient(MONGO_HOST)
    db = client[database]
    with open('MOCK_DATA.json') as f:
        file_data = json.load(f)
        db.get_collection(collection).insert_many(file_data)

```

### Apartado 2 
Insertar los siguientes objetos en la base de datos usando python. Para ello podeis crear una lista q contenga los datos

Podeis consultar el fichero [mongo_utils.py](mongo_utils.py), donde podeis ver un ejemplo básico de cada tipo de operación.
	
```python
	data =[
	{
	"first_name" : "Manuel",
	"last_name" : "Gomez",
	"email" : "manogo@gmail.com",
	"gender" : "Male",
	"ip_address" : "15.208.64.26",
	"Latitude" : 43.6342238,
	"Altitude" : -3.41144,
	"City" : "Madrid",
	"University" : "Upsa"
	},
	{
	"first_name" : "Lucia",
	"last_name" : "Sanchez",
	"email" : "lucisan@gmail.com",
	"gender" : "Female",
	"ip_address" : "5.208.64.76",
	"Latitude" : 43.1342238,
	"Altitude" : -2.41144,
	"City" : "Salamanca",
	"University" : "UPSA"
	},
	{
	"first_name" : "Sergio",
	"last_name" : "Suarez",
	"email" : "sergiosua@gmail.com",
	"gender" : "Male",
	"ip_address" : "5.208.65.29",
	"Latitude" : 43.1342238,
	"Altitude" : -2.61144,
	"City" : "Salamanca",
	"University" : "UPSA"
	}]
```




### Apartado 3
Hacer una query q me saque por consola el porcentaje de usuarios por género
Podeis consultar el fichero [mongo_utils.py](mongo_utils.py), donde podeis ver un ejemplo básico de cada tipo de operación.

Tip:
```python
db.get_collection(collection).count_documents(query)
```


### Apartado 4
Actualizar la ip de un usuario nombre "Jervis"" y actualizarlo con "109.150.230.156/24" and comprobarlo haciendo una query.


## Apartado 5
Buscar y sacar por consola los usuarios cuya latitud se mayor o igual que ﻿30.00 y la altitud menor que 10.00

## Apartado 6

Crear un metodo que borre todos los elementos de la collecion users.
Tip:
```python
db.get_collection(collection).delete_many(query)
```

### Apartado 7
Realizar un map reduce q de la siguiente salida para ello podeis consultar: [Map Reduce PyMongo](https://api.mongodb.com/python/2.0/examples/map_reduce.html)
```bash
{'_id': 'Female', 'value': 19.0}
{'_id': 'Male', 'value': 14.0}
```

 
