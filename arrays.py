#Busqueda con while

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


#Busqueda con for


'''

nom = ["Macia", "Guillem", "Yago", "Rosa", "Victor"]

var_a_encontrado = "Rosa"

encontrado = False
contador = 0
def busqueda_for(nom):
    global encontrado, contador  

    for indice, nombre in enumerate(nom):
        if nombre == var_a_encontrado:
            encontrado = True
            contador = indice
            break
    print(nom[contador])

    

busqueda_for(nom)


'''



#Recorrido con while


'''
nom = ["Macia", "Guillem", "Yago", "Rosa", "Victor"]

contador = 0
def recorrido_while(nom):
    global contador
    while contador < len(nom):
        print(nom[contador])
        contador += 1

recorrido_while(nom)
'''



#Recorrido con for


'''
nom = ["Macia", "Guillem", "Yago", "Rosa", "Victor"]

contador = 0

def recorrido_for(nom):
    global contador
    for i in nom:
        print(i)

recorrido_for(nom)
'''
        