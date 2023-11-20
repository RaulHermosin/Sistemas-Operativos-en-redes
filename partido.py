import random

class Equipo:
    def __init__(self, nombre_club):
        self.nombre_club = nombre_club

    def ocasion_gol(self):
        #gol = 1
        #no_gol = 0
        a = random.randint(0,1)
        if a == 1:
            return 1
        
        else:
            return 0 
        
        
class Partido:
    def __init__(self, equipo1, equipo2, nocasiones):
        self.equipo1 = equipo1
        self.equipo2 = equipo2
        self.nocasiones = nocasiones
        self.golese1 = 0
        self.golese2 = 0

    def jugar_partido(self):

        i = 0 

        while i < self.nocasiones:
            b = random.randint(0, 1)
            if b == 0:
                self.golese1 += self.equipo1.ocasion_gol()
            else:
                self.golese2 += self.equipo2.ocasion_gol()

            print(self.golese1 ," - ",self.golese2)
            i = i + 1
      


if __name__=='__main__':
    E1=Equipo("Valencia")
    E2=Equipo("Villareal")
    P1 = Partido(E1, E2, 10)
    P1.jugar_partido()