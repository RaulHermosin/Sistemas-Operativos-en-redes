import psycopg2
import requests
import json
try:

    parametros = {
        "host": "LocalHost",
        "port": "5432",
        "user": "postgres",
        "password": "admin",
     "database": "hola"
}

    conn = psycopg2.connect(**parametros)

    cursor = conn.cursor()
    ''' 
    postgreSQL_select_Query = "select * from conexion"

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()

    print("Print each row and it's columns values")
    for row in mobile_records:
        print("id = ", row[0], )
        print("nombre = ", row[1])
        print("edad  = ", row[2], "\n")
    '''
    dominio = "google.com"

    url = f"https://www.virustotal.com/api/v3/domains/{dominio}/comments"

    payload = {}
    headers = {
  'x-apikey': '3b5bc08c2ae2da7e8289d6535a63487c1f8f0f198ce67458813ca968fdfb0f82'
}

    response = requests.request("GET", url, headers=headers, data=payload)
    response = json.loads(response.text)

    print("Insert into table dominios: ", dominio, " hay ", response['meta']['count'])

    
            # Supongamos que tu tabla en la base de datos tiene columnas 'campo1', 'campo2', etc.
    query = f"INSERT INTO conexion (id, cantidad) VALUES (%s, {response['meta']['count']}, ...);"
    #datos_registro = (registro['id'], registro['cantidad'])  # Ajusta según la estructura de tus datos
    datosregistros = (dominio, response['meta']['count'])
         # Ejecuta la consulta
    cursor.execute(query, datosregistros)

# Confirmar los cambios y cerrar la conexión
    conn.commit()
    cursor.close()
    conn.close()









except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cursor.close()
        conn.close()
        print("PostgreSQL connection is closed")

        dominio = "google.com"

