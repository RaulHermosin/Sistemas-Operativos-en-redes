import random

class Coche():
    def __init__(self, marca, modelo , caballos):
        self.marca = marca
        self.caballos = caballos
        self.modelo = modelo

#class Carrera():
 #   def __init__(self):

  #  def empieza_carrera(self):
   #     random.randint(coches)


if __name__ == '__main__':
    c1 = Coche("Honda", "Civic", "120hp")
    c2 = Coche("Ferrari", "Huracán", "200hp")
    c3 = Coche("Mazda", "MX5", "180hp")

    coches = [c1, c2, c3]
    ganador = random.choice([c1, c2, c3])
    #c = Carrera(coches)
    #c.empieza_carrera()
    #c.muestra_resultado()
    print(ganador)