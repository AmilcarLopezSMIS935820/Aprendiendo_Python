#Josué Amílcar López Benítez (SMIS935820)

#Ejercicio #1
class EnteroaRomano:
    def __init__(self, numero): #Se crea constructor
      self.numero = numero;
      self.romano = self.convertir_a_romano() #Pasa a la función de conversión
   
    def convertir_a_romano(self): #Esta parte la vi en un libro, pero estaba en JAVA, tuve que cambiarlo un poco...
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        simbolo = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        romano = []
        i = 12
        valor = self.numero

        while valor:
            div = valor // num[i]
            valor %= num[i]
            while div:
                romano.append(simbolo[i]) # Nota personal: append() me permite agregar nuevos elementos a una lista...
                div -= 1
            i -= 1

        return "".join(romano) #Le da formato a la salida, en este caso queda en blanco... 


print("---------- Este programa convierte un número Entero a número Romano ---------- \n")

v1 = int(input("Ingrese un número entero: "))  #Ingreso de dato

while v1<1 or v1>3999: #Se limita el alcance ya que tuve problemas para sobrepasar la conversión luego de los 4000
    print("No se soportan números menores de 1 o mayores de 3999")
    print("=========================================================================== \n")
    v1 = int(input("Ingrese un numero entero: ")) #Vuelve a introducirse un dato

numero = EnteroaRomano(v1) #Salio del bucle y empieza a ir a la clase
print("El resultado de la conversión de Entero a Romano es: ", numero.romano)

print("\n \n")



#Ejercicio #2
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


print("--------------- Este programa calcula el área de un rectángulo --------------- \n")

base = float(input("1.- Ingrese el valor de la base del rectángulo: "))
altura = float(input("2.- Ingrese el valor de la altura del rectángulo: "))
rectangulo = Rectangulo(base, altura)
print("")
print("El área del rectángulo es de: ", rectangulo.area(), "unidades cuadradas")

print("\n\n")



#Ejercicio 3

class Coche:
    def __init__(self, n, color, marca, modelo, puertas, placa):
        self.n = n
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.puertas = puertas
        self.placa = placa
        

    def datos(self):
        print("Datos del coche de pruebas:", #Primera parte
            "\n - Color:",  self.color,
            "\n - Marca:",  self.marca,
            "\n - Modelo:", self.modelo,
            "\n - N° Puertas:",  self.puertas,
            "\n - N° Placa:", self.placa)
        print("============================================================================== \n")


class PruebaCoche(Coche): #Segunda parte

    def variedad(self):
        print("Estos son los datos del coche #" + self.n,
              "\n - Color:",  self.color,
              "\n - Marca:",  self.marca,
              "\n - Modelo:", self.modelo,
              "\n - N° Puertas:",  self.puertas,
              "\n - N° Placa:", self.placa, "\n")


print("------------------ Este programa instancia varios coches ------------------- \n")

#He generado las placas de un generador web
CarroInicial = Coche("(Coche de prueba)", "Naranja", "Nissan", "Tzuru", "4 puertas", "6449-RFQ")

VarCarro1 = PruebaCoche("01", "Blanco", "Nissan", "GT-R", "2 puertas", "0085-IIG")
VarCarro2 = PruebaCoche("02", "Negro", "Toyota", "Hilux", "4 puertas", "5830-KXR")
VarCarro3 = PruebaCoche("03", "Gris", "Isuzu", "Vehicross", "4 puertas", "5683-AZA")
VarCarro4 = PruebaCoche("04", "Rojo", "Lamborghini", "Aventador", "2 puertas", "3206-HLO")
VarCarro5 = PruebaCoche("05", "Azul", "Audi", "Audi R8", "2 puertas", "188-FSM")


#Cambio de color
VarCarro1.color=("Azul Marino")
VarCarro2.color=("Rojo Carmesí")
VarCarro3.color=("Verde Musgo")
VarCarro4.color=("Blanco Perla")
VarCarro5.color=("Plateado")

CarroInicial.datos()
VarCarro1.variedad()
VarCarro2.variedad()
VarCarro3.variedad()
VarCarro4.variedad()
VarCarro5.variedad()

print("\n")



#Ejercicio 4
import datetime

class carnet():
    def __init__(self, nombre, apellido, año):
        self.nombre = nombre
        self.apellido = apellido
        self.año = año

    def crear_carnet(self):
        p1 = self.nombre[:1]
        p2 = self.apellido[:1]
        p3 = str(self.año)
        print("Su carnet estudiantil quedaría: " + p1.upper() + p2.upper() + p3) #Producto final...


print("------ Bienvenido al sistema encargado de crear tu Carnet Estudiantil ------ \n")

v1 = str(input("1.- Ingrese uno de sus nombres: "))
v2 = str(input("2.- Ingrese uno de sus apellidos: "))
print("")

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")

v3 = str(year) #He automatizado la entrada del año con la librería "datetime"

envio = carnet(v1, v2, v3)
envio.crear_carnet()
