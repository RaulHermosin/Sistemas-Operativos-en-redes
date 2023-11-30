import random

class Partida:
    def __init__(self):
        self.resultado = random.randint(1, 10)





    def jugar_partida(self):
        print("La partida ha comenzado")
        print("Escoja un número del 1 al 10")
        self.seleccion = input(self)
        if self.seleccion == self.resultado:
            print("¡Enhorabuena! Has acertado el número")

        else:
            print("Has fallado, vuelve a intentarlo")
            
        


class Menu:
    def __init__(self):
        self.opcion_elegida = None
        self.juego = Partida()


    def mostrar_menu(self):
        print("1) Iniciar Partida")
        print("2) Ranking")
        print("3) Salir")

    def seleccionar(self):
        seleccion = input()
        if seleccion == "1":
           self.juego.jugar_partida()
            


if __name__=='__main__':
    M1 = Menu()
    M1.seleccionar()