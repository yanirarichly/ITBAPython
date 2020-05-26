import pandas as pd

# aca almacenamos las bases de datos que vamos a unificar
self.nombre = ["lista1.csv", "lista2.csv"]

# en este diccionario vamos a ir amlacenando la información de la base de datos unificada
# la clave son los mails, el contenido la información de los usuarios

self.union = dict()

# en este set almacenamos todas las columnas que se van progresivamente encontrando
self.column = set()  # set=conjunto

for x in self.nombre[0]:  # iteramos todas las bases de datos

    # leemos el contenido indexando por mail (es decir la clave de los diccionarios será el mail de los usuarios)
    archivo = pd.read_excel(self.nombre[0][j], index_col=["Mail"])
    data = archivo.to_dict("index")

    # iteramos los mails de la base de datos
    for key in data:
        # si el mail es uno nuevo para nuetra base de datos unificada, lo inicializamos como un diccionario vacio sin información
        # la cual se la agregaremos despues
        # si el mail ya existe no es necesario, significa que lo vimos en una base de datos anterior

        if key not in self.union:
            self.union[key] = dict()

            # leemos todos los campos (las columnas) que tenemos del mail en la base de datos original que estamos procesando
        campos = data[key]

        # iteramos todos los campos del mail encontrado, y le asignamos sus valores en la base de datos unificada
        for campo in campos:
            # le asignamos a "clientes" que es la base de datos unificada el campo actual
            # que esta en data[mail], que tiene la información de la base de datos que estamos procesando del
            # campo correspondiente
            self.union[key][campo] = data[key][campo]

            # le agregamos al set de campos (columas) el campo encontrado
            # como es un set los repetidos no van a agregarse
            self.column.add(campo)


# Por ultimo escribimos el archivo final, colocando las claves de los elementos de la base unificada (es decir los mails)
# En la primera columna (por eso orient="index")

df = pd.DataFrame.from_dict(self.union, orient='index')

df.to_excel('listafinal.csv')