listas = ["lista1.csv", "lista2.csv"]


clientes = dict()

for lista in listas:

    # leemos el contenido indexando por mail (es decir la clave de los diccionarios será el mail de los usuarios)
    archivo = pd.read_csv(lista, index_col=["Mail"])
    data = archivo.to_dict("index")

    # iteramos los mails de la base de datos
    for mail in data:
        if mail not in clientes:
            clientes[mail] = dict()
            # leemos todos los campos (las columnas) que tenemos del mail en la base de datos original que estamos procesando
        campos = data[mail]

        # iteramos todos los campos del mail encontrado, y le asignamos sus valores en la base de datos unificada
        for campo in campos:
            clientes[mail][campo] = data[mail][campo]

df = pd.DataFrame.from_dict(clientes, orient='index')

df.to_csv('listafinal.csv')