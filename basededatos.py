import psycopg2

conn = psycopg2.connect(host="localhost", database="hola", user="postgres", password="admin")

#conn = psycopg2.connect("dbname=hola, user=postgres, password=admin")

cur = conn.cursor()

cur.execute("SELECT * FROM usuarios")

records = cur.fetchall()