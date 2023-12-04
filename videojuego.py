import random
class TratamientoFichero():

    def __init__(self, nombre_fichero):
        self.nombre_fichero = nombre_fichero

    def write_file(self, line_to_write):
        f = open(self.nombre_fichero, "a")
        f.write(line_to_write)
        f.write("\n")
        f.close()
        
    def read_file(self):
        f = open(self.nombre_fichero, "r")
        print(f.read())
        f.close()



class Partida:
    def __init__(self):
        self.resultado = random.randint(1, 10)
        self.acertar = False

  


    def jugar_partida(self):
        print("La partida ha comenzado")
        print("Escoja un número del 1 al 10")
        self.intentos = 0
        self.puntos = 10
        while  True: 
            self.seleccion = int(input())
            if self.resultado == self.seleccion:
                self.puntos_ganados = self.puntos - self.intentos
                print("¡Enhorabuena! Has acertado el número")
                print("El número era :", self.resultado)
                print("Has tenido ", self.intentos ," fallos")
                print("Has conseguido un total de ", self.puntos_ganados, " puntos")
                print("Porfavor, diganos tu nombre")
                self.nombre_jugador = input()
                

                break

            else:
                print("Has fallado, vuelve a intentarlo")
                self.intentos = self.intentos + 1



            

    def ranking(self):
        self.read_file
        


class Menu:
    def __init__(self):
        self.opcion_elegida = None
        self.juego = Partida()


    def mostrar_menu(self):
        print("1) Iniciar Partida")
        print("2) Ranking")
        print("3) Salir")
        self.seleccionar()

    def seleccionar(self):
        
        seleccion = input()
        if seleccion == "1":
           self.juego.jugar_partida()
            


if __name__=='__main__':
    M1 = Menu()
    f = TratamientoFichero("ranking.txt")
    f.write_file("¡", Partida.nombre_jugador, " ha obtenido ", Partida.puntos_ganados, " puntos!")
    M1.mostrar_menu()