import time
class Coche:
    def __init__(self, marca, motor, ruedas, puertas, velocidad_actual, velocidad_punta, arrancar):
        self.marca = marca
        self.motor = motor
        self.ruedas = ruedas
        self.puertas = puertas
        self.velocidad_actual = velocidad_actual
        self.velocidad_punta = velocidad_punta
        self.arrancar = arrancar
    
    def __str__(self):
        return f"{self.marca}, {self.motor}, {self.ruedas}, {self.puertas}, {self.velocidad_actual}"

    def arranca_automatico(self):
        while self.velocidad_actual<self.velocidad_punta:
           
            print(self.velocidad_actual)
            self.velocidad_actual = self.velocidad_actual + 5
            time.sleep(0.5)

    
if __name__=='__main__':
    C1 = Coche("Volkswagen", "V8", "Michelin", 5, 100, 200, "TUWIQIQIQIQIBRRRROMMMM....")
    #print(C1.marca)
    #print(C1.ruedas)
    #print(C1.motor)
    #print(C1.velocidad_actual)
    #print(C1)
    #print(C1.arrancar)
    C1.arranca_automatico()