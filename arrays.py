'''
nom = ["Macia", "Guillem", "Yago", "Rosa", "Victor"]

var_a_encontrado = "Guillem"

contador = 0
encontrado = False

def busqueda_while (nom):
    global contador, encontrado
    while contador < len(nom):
        if nom[contador] == var_a_encontrado:
            encontrado = True
            break
        contador = contador + 1
        print(nom[contador])

busqueda_while(nom)
'''

nom = ["Macia", "Guillem", "Yago", "Rosa", "Victor"]

var_a_encontrado = "Rosa"

encontrado = False
contador = 0
def busqueda_for(nom):
    global encontrado, contador  

    for contador, nombre in enumerate(nom):
        if nombre == var_a_encontrado:
            encontrado = True
            break
        contador = contador + 1
        print(nom[contador])

busqueda_for(nom)