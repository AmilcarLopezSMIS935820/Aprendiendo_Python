#Josué Amílcar López Benítez (SMIS935820)
import time
class Bicicleta:   
    def __init__(self, modelo, precio, aceleracion):
        self.modelo = modelo
        self.precio = precio
        self.aceleracion = aceleracion
        self.velocidad = 0
        
    def Acelerar(self):
        print("Usted ha acelerado")
        self.velocidad = self.velocidad + self.aceleracion
        print('-----------------------------------------------------------------')

    def Frenar(self):
        print("Usted ha frenado")
        i = self.velocidad - 1
        if i <= 0:
            i=0
        self.velocidad = i
        print('-----------------------------------------------------------------')

    def Consultar_Velocidad(self):
        print("La velocidad Actual es de:", self.velocidad, "Km/h")
        print('-----------------------------------------------------------------')

    def finalizar(self):
        print('\n-----------------------------------------------------------------')
        print("\n Los detalles de su equipo son:",
              "\n - Modelo:", self.modelo,
              "\n - Precio:", self.precio,
              "\n - La velocidad Final es:", self.velocidad, "Km/h")


p1= Bicicleta("Mountain Bike Nordic x1.0 R29", "$59.47", 3) #El impulso de aceleración será de 3Km/h 


print("-------------------------- Simulador de Ciclismo --------------------------")

timer = 1
while (timer != 0 ): #Queria probar a hacer un cronometro...
    timer = timer-1
    time.sleep(1)
    #print(timer) #Esta línea seria por si desea que se muestre el contador del cronometro…

    if timer ==0:
        print("\n1.- Acelerar")
        print("2.- Frenar")
        print("3.- Consultar velocidad Actual")
        print("0.- Terminar programa")
        n = int(input("\nIngrese la opción a realizar: "))

        if n==1:
            p1.Acelerar()
            timer = 3
            
        if n==2:
            if p1.velocidad==0:
                print("Aun no ha arrancado :)")
                print('-----------------------------------------------------------------')
                timer=1
            else:
                p1.Frenar()
                timer = 3

        if n==3:
            p1.Consultar_Velocidad()
            timer = 3

        if n==0:
            p1.finalizar()
        
        if n<0 or n>3:
            print("Ups... Ha ocurrido un error…")
            print('-----------------------------------------------------------------')
            timer = 3


