#Josué Amílcar López Benítez (SMIS935820)
from tkinter import *
from tkinter import messagebox as mb

class Minicalculadora:
    def __init__(self):
        #Configuración basica-------------------------------------------
        self.ventana = Tk()
        self.ventana.title("MiniCalculadora")
        self.ventana.geometry("260x330")
        self.ventana.config(bd=20, bg="White")
        
        #Estructura base del programa-------------------------------------------
        self.valid = True 
        self.dato1 = StringVar()
        self.dato2 = StringVar()
        self.respuesta= StringVar()

        self.label1 = Label(text="Escribe el primer número:", bg="white", font=("", 10 , '')).pack()
        self.entry1 = Entry(self.ventana,justify=CENTER,
                            width=30,
                            bg="#E3F4F9",
                            textvariable=self.dato1,
                            font=('Helvetica', 10))
        
        self.enfocar() #Sirve para enfocar y empaquetar la primera caja de entrada de datos
        
        self.label2 = Label(text="\nEscribe el segundo número:", bg="white", font=("", 10 , '')).pack()
        self.entry2 = Entry(self.ventana,justify=CENTER,
                            width=30,
                            bg="#E3F4F9",
                            textvariable=self.dato2,
                            font=('Helvetica', 10)).pack()

        
        #separador
        self.separador = Label(bg="white").pack()

        #Area de botones-------------------------------------------
        self.boton1 = Button(self.ventana, text="Suma", width=25, height=1,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.sumar).pack(pady=1)

        self.boton2 = Button(self.ventana, text="Resta", width=25, height=1,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.restar).pack()

        self.boton3 = Button(self.ventana,text="Multiplicación",width=25,height=1,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.multiplicar).pack(pady=1)

        self.boton4 = Button(self.ventana, text="Dividisión", width=25, height=1,
                             bg='#0B9AC8', fg='#ffffff', font=('Helvetica', 10, 'bold'),
                             command=self.dividir).pack()

        self.cod = Label(text="\nSMIS935820", bg="white", justify=CENTER, fg='#A9A6F9', font=("", 10,'bold')).pack(pady=2)
        self.ventana.mainloop()

        
    #Suma-------------------------------------------
    def sumar(self):
        self.validar()
        if self.valid==True:
            n1 = float(self.dato1.get())
            n2 = float(self.dato2.get())
            self.respuesta.set(str(n1+n2))
            mb.showinfo("Respuesta", "El resultado de la suma es: " + str(self.respuesta.get()))
            self.borrar()
       
        
    #Resta-------------------------------------------
    def restar(self):
        self.validar()
        if self.valid==True:
            n1 = float(self.dato1.get())
            n2 = float(self.dato2.get())
            self.respuesta.set(str(n1-n2))
            mb.showinfo("Respuesta", "El resultado de la resta es: " + str(self.respuesta.get()))
            self.borrar()
            
    #Multiplicación-------------------------------------------
    def multiplicar(self):
        self.validar()
        if self.valid==True:
            n1 = float(self.dato1.get())
            n2 = float(self.dato2.get())
            self.respuesta.set(str(n1*n2))
            mb.showinfo("Respuesta", "El resultado de la multiplicación es: " + str(self.respuesta.get()))
            self.borrar()

    #División-------------------------------------------
    def dividir(self):
        self.validar()
        if self.valid==True:
            n1 = float(self.dato1.get())
            n2 = float(self.dato2.get())
            self.respuesta.set(str(n1/n2))
            mb.showinfo("Respuesta", "El resultado de la división es: " + str(self.respuesta.get()))
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
            self.respuesta.set("")
            
        else:
            self.valid = True
            
    #Enfocar-------------------------------------------
    def enfocar(self):
        self.entry1.focus()
        self.entry1.pack()

aplicacion = Minicalculadora()
