def greetings():
    print("Hello World!")
def equals(a,b):
    global alo 
    alo = "Buenas tardes"
    return a+b

def resta(a,b):
    return a-b

def multi(a,b):
    return a*b

def print_array(array):
    

    for x in array:
        print("Hola, me llamo ",x)

if __name__=='__main__':

    greetings()
   # equals(5,5)
    res = resta(2,4)
    suma = equals(2,4)
    multip = multi(2,4)

    print("La resta es igual a {}".format(res))
    print("La suma es igual a {}".format(suma))
    print("La multiplicacion es igual a {}".format(multip))
    print(alo)
    array = ["Jesus","Manolo","Husky"]
    print_array(array)