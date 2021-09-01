#Josué Amílcar López Benítez (SMIS935820)

#===============================================================
#Ejercicio #1
class empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def datos(self):
        print("\nSus datos generales son:",
              "\n - Usuario:", self.nombre,
              "\n - Sueldo: $" + str(self.sueldo), "\n")

    def impuesto(self):
        if self.sueldo > 3000:
            print("Ya que su sueldo sobrepasa los $3000, el usuario", self.nombre.upper(), "debe pagar impuesto ")
        else:
            print("Ya que su sueldo es menor a $3000, el usuario", self.nombre.upper(), "no debe pagar impuesto")


a = input("Ingrese su nombre: ")
b = float(input("Ingrese su sueldo: "))
print("--------------------------------------------------------------------------")

v = empleado(a, b)
v.datos()
v.impuesto()

#===============================================================
#Ejercicio #2
class Cuenta:
    def __init__(self, detalle):
        self.detalle = detalle
        self.saldo = 0

    def Apertura(self):
        self.saldo = self.saldo + self.detalle
        print("Su cuenta se ha inicializado con: $" + str(self.detalle))

    def Debito(self):
        if self.saldo < self.detalle:
            print("No cuenta con fondos suficientes para retirar la cantidad de dinero solicitado")

        else:
            if self.detalle >500:
               print("No puede retirar más de $500 de su cuenta") 
            else:
                self.saldo = self.saldo - self.detalle
                print("Ha retirado $" + str(self.detalle), "por lo tanto, su nuevo saldo es de: $" + str(self.saldo))

    def Cargo(self):
        self.saldo = self.saldo + self.detalle
        print("Ha abonado $" + str(self.detalle), "así que su cuenta tiene un saldo de $" + str(self.saldo))


repet = True
nombre = input(("¿Cuál es su nombre? "))
print("\n Bienvenido", nombre, "¿Que desea realizar? ")

cuenta = Cuenta(0)
cuenta_creada = False

while repet == True:
    print("--------------------------------------------------------------------------")
    print("\n1.- Apertura de cuenta",
          "\n2.- Retirar Saldo",
          "\n3.- Abonar a cuenta",
          "\n0.- Terminar programa")
    n = int(input("\n Ingrese la opción a realizar: "))

    if n == 1 :
        if cuenta_creada ==False:
            det = float(input("Ingrese el monto con el que desea crear su cuenta: "))
            cuenta.detalle=det
            cuenta.Apertura()
            cuenta_creada = True
        else:
            print(nombre, "ya ha creado una cuenta... Por favor elija otra de nuestras opciones")
        
    if n == 2 :
        if cuenta_creada == True:   
            det = float(input("Ingrese el monto a retirar de su cuenta: "))#Lo hice así para no perder "continuidad" 
            cuenta.detalle=det
            cuenta.Debito()
        else:
            print("Debe crear una cuenta primero...")

    if n == 3:
        if cuenta_creada == True:
            det = float(input("Ingrese la cantidad que desea abonar a su cuenta: "))
            cuenta.detalle=det
            cuenta.Cargo()
        else:
            print("Debe crear una cuenta primero...")
            
    if n == 0:
        print("\n Muchas gracias por utilizar nuestro sistema :)")
        repet = False


#===============================================================
#Ejercicio #3
class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        #Solo pondre 5 materias...
        self.lenguaje = 0
        self.matematica = 0
        self.ciencia = 0
        self.sociales = 0
        self.programacion = 0

    def PedirNotas(self):
        print("\nIngrese las notas finales obtenidas por:", self.nombre)
        print("--------------------------------------------------------------------------\n")
        self.lenguaje = float(input(" - Lenguaje y literatura: "))
        self.matematica = float(input(" - Matemática Básica II: "))
        self.ciencia = float(input(" - Ciencias Naturales: "))
        self.sociales = float(input(" - Estudios Sociales: "))
        self.programacion = float(input(" - Principios de programación: "))

    def Validar_Horas_Sociales(self):
        aprobadas = 0
        HS = 0
        
        if self.lenguaje > 6:
            aprobadas += 1
            
        if self.matematica > 6:
            aprobadas += 1
        
        if self.ciencia > 6:
            aprobadas += 1
        
        if self.sociales > 6:
            aprobadas += 1
            
        if self.programacion > 6:
            aprobadas += 1
        
        HS = aprobadas * 20
        
        if aprobadas < 4:
            #Basandome en que solo necesita un 80% de materias aprobadas y no la totalidad de ellas
            print("\n" + self.nombre, "ha conseguido un " + str(HS) + "% de asignaturas aprobadas, por lo tanto,",
                  "\nnecesita reponer", (4 - aprobadas), "materias, para poder realizar su servicio social")
        else:
            print("\n" + self.nombre, "ha conseguido un " + str(HS) + "% de asignaturas aprobadas.",
                  "\nPor lo tanto, puede realizar su servicio social")

        print("--------------------------------------------------------------------------")



a = input("Ingrese el nombre del alumno a evaluar: ")
v = Estudiante(a)
v.PedirNotas()
v.Validar_Horas_Sociales()
