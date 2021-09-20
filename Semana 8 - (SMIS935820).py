#Josué Amílcar López Benítez (SMIS935820)

#======================= Conversor de unidades =======================
from tkinter import *
from tkinter import ttk

#Función principal-------------------------------------------
def seleccion():
    sl1 = str(comboEntrada.get()) #Retoma el valor del combobox de entrada
    sl2 = str(comboSalida.get())#Retoma el valor del combobox de entrada
    entrada = float(entrada_valor.get()) #Retoma la entrada

    #Por si ambos combobox tienen el mismo tipo
    if sl1 == sl2:
        v2.set(entrada)

    #Conversion de Kilometros a otras unidades ------------------ 
    if sl1=="Kilometros" and sl2=="Millas":
        v2.set(round((entrada*0.621371),6))
        
    elif sl1=="Kilometros" and sl2=="Pulgadas":
        v2.set(round((entrada*39370.1),2))

    elif sl1=="Kilometros" and sl2=="Centimetros":
        v2.set(round((entrada*100000),2))

    elif sl1=="Kilometros" and sl2=="Metros":
        v2.set(round((entrada*1000),2))


    #Conversion de Millas a otras unidades ------------------ 
    if sl1=="Millas" and sl2=="Kilometros":
        v2.set(round((entrada*1.60934),5))
        
    elif sl1=="Millas" and sl2=="Pulgadas":
        v2.set(round((entrada*63360),2))

    elif sl1=="Millas" and sl2=="Centimetros":
        v2.set(round((entrada*160934),2))

    elif sl1=="Millas" and sl2=="Metros":
        v2.set(round((entrada*1609.34),2))

        
    #Conversion de Pulgadas a otras unidades ------------------ 
    if sl1=="Pulgadas" and sl2=="Kilometros":
        v2.set(round((entrada*0.0000254),8))
        
    elif sl1=="Pulgadas" and sl2=="Millas":
        v2.set(round((entrada*0.0000157828),8))

    elif sl1=="Pulgadas" and sl2=="Centimetros":
        v2.set(round((entrada*2.54),4))

    elif sl1=="Pulgadas" and sl2=="Metros":
        v2.set(round((entrada*0.0254),6))


    #Conversion de Centimetros a otras unidades ------------------ 
    if sl1=="Centimetros" and sl2=="Kilometros":
        v2.set(round((entrada*0.00001),8))
        
    elif sl1=="Centimetros" and sl2=="Millas":
        v2.set(round((entrada*0.0000062137),8))

    elif sl1=="Centimetros" and sl2=="Pulgadas":
        v2.set(round((entrada*0.393701),6))

    elif sl1=="Centimetros" and sl2=="Metros":
        v2.set(round((entrada*0.01),2))


    #Conversion de Metros a otras unidades ------------------ 
    if sl1=="Metros" and sl2=="Kilometros":
        v2.set(round((entrada*0.001),8))
        
    elif sl1=="Metros" and sl2=="Millas":
        v2.set(round((entrada*0.00062137),9))

    elif sl1=="Metros" and sl2=="Pulgadas":
        v2.set(round((entrada*39.3701),2))

    elif sl1=="Metros" and sl2=="Centimetros":
        v2.set(round((entrada*100),2))
        
#Función para reiniciar entradas y salidas -------------------------------
def limpiar():
    v1.set("")
    v2.set("")
    entrada_valor.focus()


#Configuración basica -------------------------------
app = Tk()
app.title("Conversor de unidades")
app.geometry('500x250')
app.config(bd=30, bg="white")

#Variables iniciales -------------------------------
v1 = StringVar()
v2 = StringVar()

#Combobox para definir el tipo de entrada -------------------------------
labelEntrada = Label(app, text = "Entrada", bg="white", font=("Helvetica", 10), padx=5).grid(column=0, row=0)

comboEntrada = ttk.Combobox(app,
                            values=["Pulgadas", "Centimetros", "Metros", "Kilometros", "Millas"], state="readonly", width=17, justify=CENTER)


comboEntrada.grid(column=1, row=0)
comboEntrada.current(0)

#Combobox para definir el tipo de salida -------------------------------
separador = Label(app, width=5, bg="white").grid(column= 2, row=0)

labelSalida = Label(app, text = "Salida",bg="white", font=("Helvetica", 10), padx=5).grid(column=3, row=0)

comboSalida = ttk.Combobox(app, 
                            values=["Pulgadas", "Centimetros", "Metros", "Kilometros", "Millas"], state="readonly", width=17, justify=CENTER)


comboSalida.grid(column=4, row=0)
comboEntrada.current(1)
comboSalida.current(2)

#Entrada de dato a convertir -------------------------------
valor = Label(app, text="Valor:", bg="white", font=("Helvetica", 10)).grid(pady=35, column=0,row=2)
entrada_valor = Entry(app,justify=CENTER,
                      width=17,
                      textvariable= v1,
                      bg="#E3F4F9",
                      font=('Helvetica', 10))

entrada_valor.focus()
entrada_valor.grid(pady=25, column=1, row=2)

#Separador -------------------------------
separador2 = Label(app, width=7, bg="white").grid(column= 2, row=2)

#Salida para dato convertido -------------------------------
resultado = Label(app, text="Resultado:", bg="white", font=("Helvetica", 10)).grid(pady=35, column=3,row=2)
salida_resultado = Entry(app,justify=CENTER,
                         width=17,
                         textvariable= v2,
                         disabledbackground="#E3F4F9",
                         font=('Helvetica', 10),state='disabled').grid(pady=25, column=4, row=2)


#Area de botones -------------------------------
btnlimpiar = Button(app, text="Limpiar", width=15, height=1,bg='#E5440C', fg='#ffffff',
                    font=('Helvetica', 10, 'bold'), command=limpiar).grid(pady=25, row=3, column=0, columnspan=2)

btnconvertir = Button(app, text="Convertir", width=15, height=1,bg='#0B9AC8', fg='#ffffff',
                    font=('Helvetica', 10, 'bold'), command=seleccion).grid(pady=25, row=3, column=3, columnspan=2)



app.mainloop()


#======================= Juego del 7 afortunado =======================
from tkinter import *
import random
from tkinter import messagebox as mb
from PIL import ImageTk, Image

class juego:
    def __init__(self):
        #Configuración basica-------------------------------------------
        self.ventana = Tk()
        self.ventana.title("Jackpot UGB")
        self.ventana.geometry("290x430")
        self.ventana.config(bd=30, bg="#020A44")

        #Configuración de la imagen HD que se muestra en la aplicación------------------------
        img = ImageTk.PhotoImage(Image.open(r"C:\Users\pc\Desktop\Semana 8\hd2.png"))
        imglabel = Label(self.ventana, image=img, width=200, height=200, bg="#020A44").grid(row=1, column=0, columnspan=3)
        
        #Estructura base del programa-------------------------------------------
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.v3 = IntVar()        

        
        self.n1 = Entry(self.ventana,justify=CENTER,
                            width=4,
                            disabledbackground="#E3F4F9",
                            textvariable=self.v1,
                            font=('Helvetica', 12, 'bold'), state='disabled').grid(ipady=15, pady=25, padx=1, row=2, column=0)

        
        self.n2 = Entry(self.ventana,justify=CENTER,
                            width=4,
                            disabledbackground="#E3F4F9",
                            textvariable=self.v2,
                            font=('Helvetica', 12, 'bold'), state='disabled').grid(ipady=15, pady=25, padx=1, row=2, column=1)
        
        self.n3 = Entry(self.ventana,justify=CENTER,
                            width=4,
                            disabledbackground="#E3F4F9",
                            textvariable=self.v3,
                            font=('Helvetica', 12, 'bold'), state='disabled').grid(ipady=15, pady=25, row=2, column=2)

    #Area de boton-------------------------------------------
        self.boton1 = Button(self.ventana, text="Jugar", width=25, height=2,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.iniciar).grid(padx=10, pady=5, row=4, column=0, columnspan=3)

        self.ventana.mainloop()
        
    #Función inicial-------------------------------------------
    def iniciar(self):
        n1 = random.randint(1, 7)
        n2 = random.randint(1, 7)
        n3 = random.randint(1, 7)
        self.v1.set(str(n1))
        self.v2.set(str(n2))
        self.v3.set(str(n3))
        self.evaluar()

    #Función para evaluar-------------------------------------------
    def evaluar(self):
        a = int(self.v1.get())
        b = int(self.v2.get())
        c = int(self.v3.get())
        
        if a == 7 and b == 7 and c == 7:
            mb.showinfo("Oooh Yeah", "Felicidades... ¡¡Ha ganado!!")
            self.reinicio()
        else:
            mb.showerror("¡Oh no!", "Ha perdido... Intentelo más tarde")
            self.reinicio()

            
    #Función para reiniciar valores-------------------------------------------
    def reinicio(self):
        self.v1.set("0")
        self.v2.set("0")
        self.v3.set("0")
        
aplicacion = juego()


#============================== MRU ==============================
from tkinter import *
from tkinter import messagebox as mb

class MRU:
    def __init__(self):
        #Configuración basica-------------------------------------------
        self.ventana = Tk()
        self.ventana.title("Tiempo con MRU")
        self.ventana.geometry("260x330")
        self.ventana.config(bd=25, bg="White")

        
        #Estructura base del programa-------------------------------------------
        self.valid = True 
        self.dato1 = StringVar()
        self.dato2 = StringVar()

        self.label1 = Label(text="Ingrese la distancia en m:", bg="white", font=('Helvetica', 10)).pack()
        self.distancia = Entry(self.ventana,justify=CENTER,
                            width=30,
                            bg="#E3F4F9",
                            textvariable=self.dato1,
                            font=('Helvetica', 10))
        
        self.enfocar() #Sirve para enfocar y empaquetar la primera caja de entrada de datos
        
        self.label2 = Label(text="\nIngrese la velocidad en mph:", bg="white", font=('Helvetica', 10)).pack()
        self.velocidad = Entry(self.ventana,justify=CENTER,
                            width=30,
                            bg="#E3F4F9",
                            textvariable=self.dato2,
                            font=('Helvetica', 10)).pack(pady=15, ipady=2)

        

        #Area de boton-------------------------------------------
        self.boton1 = Button(self.ventana, text="Calcular", width=30, height=1,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.calcular).pack(pady=15)


        self.ventana.mainloop()

        
    #Calcular-------------------------------------------
    def calcular(self):
        self.validar()
        if self.valid==True:
            n1 = float(self.dato1.get())
            n2 = float(self.dato2.get()) * 0.4470400 #Nos dan mph y los convertimos a m/s
            
            #Aplicamos la formula t=d/v y dividimos ese resultado entre 60 para obtener una salida en Minutos
            minutos=round(((n1/n2)/60),2)#Utilizamos round() para redondear la salida a dos numeros luego del punto decimal
            mb.showinfo("Respuesta :)", "El automovil tardará " + str(minutos) + " minutos en" +
                        "\nviajar desde el punto A al punto B")
            self.borrar()
               
            
    #Borrar-------------------------------------------    
    def borrar(self):
        self.dato1.set("")
        self.dato2.set("")
        self.enfocar()

    #Validar-------------------------------------------
    def validar(self):
        if self.dato1.get() == "" or self.dato2.get() == "":
            self.valid = False
            mb.showerror("Cuidado","No puede dejar los campos vacíos")
            self.borrar()
            
        else:
            self.valid = True
            
    #Enfocar-------------------------------------------
    def enfocar(self):
        self.distancia.focus()
        self.distancia.pack(pady=15, ipady=2)

aplicacion = MRU()



#====================== Piedra, Papel, Tijera ======================
from tkinter import *
import random
from PIL import ImageTk, Image

#Valores que podria elegir la PC ---------- 
opciones=["piedra", "papel", "tijeras"]

#Cambio de valores para la variable opcion_usuario
def cambio1():
    opcion_usuario.set("piedra")
    print("Usted Eligio:", opcion_usuario.get())
    juego()
    
def cambio2():
    opcion_usuario.set("papel")
    print("Usted Eligio:", opcion_usuario.get())
    juego()

def cambio3():
    opcion_usuario.set("tijeras")
    print("Usted Eligio:", opcion_usuario.get())
    juego()

#Funcion principal del juego (evalua las opciones entre PC y Usuario)
def juego():
    v1 = opcion_usuario.get()
    v2 = random.choice(opciones)
    print("La PC ha elegido:", v2)
    
    if v1 == v2:
        print("Hay un empate \n")
        
    if v1=="piedra" and v2=="tijeras":
        print("Has ganado con " + v1,  "\n")
        
    elif v1=="papel" and v2 == "piedra":
        print("Has ganado con " + v1,  "\n")

    elif v1=="tijeras" and v2 == "papel":
        print("Has ganado con " + v1,  "\n")

    elif v1=="piedra" and v2=="papel":
        print("Gano PC con " + v2,  "\n")
        
    elif v1=="papel" and v2 == "tijeras":
        print("Gano PC con " + v2,  "\n")

    elif v1=="tijeras" and v2 == "piedra":
        print("Gano PC con " + v2,  "\n")


#Configuración basica-------------------------------------------
ventana = Tk()
ventana.title("Jueguemos un juego")
ventana.geometry("280x325")
ventana.config(bd=20, bg="white")

#Estructura base del programa-------------------------------------------
opcion_usuario = StringVar()

boton1 = Button(ventana, text="Piedra", width=15, height=3,
                bg='#D32307', fg='#ffffff', font=('Helvetica', 12, 'bold'), command=cambio1).pack(pady=10)

boton2 = Button(ventana, text="Papel", width=15, height=3,
                bg='#E06620', fg='#ffffff', font=('Helvetica', 12, 'bold'), command=cambio2).pack(pady=10)

boton3 = Button(ventana, text="Tijera", width=15, height=3,
                bg='#07C7D3', fg='#ffffff', font=('Helvetica', 12, 'bold'), command=cambio3).pack(pady=10)


ventana.mainloop()
