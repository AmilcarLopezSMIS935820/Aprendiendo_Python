#Josué Amílcar López Benítez (SMIS935820)

#Primer ejercicio

nombre = input("¿Cuál es su nombre? ")
cont = len(nombre)
while cont == 0:
    print("No puede dejar este espacio vacío \n")
    nombre = input("¿Cuál es su nombre? ")
    cont = len(nombre)

print("El nombre " + nombre.upper() + " tiene " + str(cont) + " letras")    

print("----------------------------------------------------------- \n")


#segundo ejercicio Amilcar

v = True
while v:
    try:
        n1 = float(input("Ingrese el primer número: "))
        n2 = float(input("Ingrese el segundo número: "))
        Ta = n1 + n2
        print("El resultado de la suma de los dos primeros números es: %i" % Ta + "\n")
        n3 = float(input("Ingrese el tercer número: "))
        Tt = Ta * n3
        print("El resultado de la multiplicación es: " + str(Tt))        
        v = False
    except:
        print("Introduzca solo valores numéricos \n")

print("----------------------------------------------------------- \n")


#Tercer Ejercicio
def FaC(c):
    return (c-32) * (5/9)

v = True

while v:
    try:
        c = float(input("Ingrese la temperatura en grados Fahrenheit: "))
        v = False
    except:
        print("Introduzca un valor numérico :p \n")

Tt = round(FaC(c),2)
print ("La temperatura equivalente en grados Celsius es de:", Tt , "°C")

print("----------------------------------------------------------- \n")


#Cuarto Ejercicio
i=0
while i<3:
      usuario=input("Ingrese su nombre de usuario: ")
      i=i +1
      if str(usuario)=="UGB":
            clave=input("ingrese su contraseña: ")
            if str(clave)=="UGB":
                  print("\n ******** Bienvenido UGB ********") #No se me ocurrio otro mensaje mejor...
                  break
            else:
                  print("Advertencia: Contraseña incorrecta \n")
                  if    i==3:
                        print("*** Ups... Ha ocurrido un error, inténtelo más tarde ***")
                        break
      else:
            print("Advertencia: Usuario incorrecto \n")
            if    i==3:
                  print("*** Ups... Ha ocurrido un error, inténtelo más tarde ***")

print("----------------------------------------------------------- \n")

#Quinto Ejercicio
v = True
while v:
    try:
        v1 = float(input("Ingrese el primer número: "))
        v2 = float(input("Ingrese el segundo número: "))
        print("El número mayor es: " + str(max(v1, v2)))
        v = False
    except:
        print("Introduzca un valor numérico  \n")
