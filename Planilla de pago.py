#Josue Amilcar Lopez Benitez -| SMIS935820 |-

import pymysql #Importando Libreria
#Conexion basica a Localhost
conexion = pymysql.connect(host='localhost', user='root', passwd='usbw',  port=3307)

#Asignacion de cursor
cur = conexion.cursor()

#Creacion de Base de Datos
cur.execute("CREATE DATABASE IF NOT EXISTS Planilla_Pago;")

#Indicamos la Base de Datos sobre la que trabajaremos
cur.execute("USE Planilla_Pago;")

cur.execute("SHOW DATABASES")

#Mostramos la bases de datos que tenemos... Solo como referencia
for db in cur: 
    print(db)

print("-------------------------------------------------------------\n")

#Creamos la primera tabla
try:
    cur.execute("""CREATE TABLE datos_empleados(
                id_empleado INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                nombre VARCHAR(30) NOT NULL,
                apellido VARCHAR(30)NOT NULL,
                direccion VARCHAR(150) NOT NULL);""")

    #Al ser su ID autoincrementable, podemos omitirlo cuando insertemos valores

    print("Se ha creado la tabla datos_empleados.\n")

except pymysql.OperationalError:
    print("Upss... Ha ocurrido un error.\n")


#Creamos la segunda tabla
try:
    cur.execute("""CREATE TABLE pago_empleados(
                id_pago INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,
                horas INTEGER NOT NULL,
                sueldo FLOAT NOT NULL,
                id_empleado INTEGER NOT NULL);""")

    #Al ser su ID autoincrementable, podemos omitirlo cuando insertemos valores
    #id_empleado hace referrencia auna Foreign Key que implementaremos luego
    print("Se ha creado la tabla pago_empleados.\n")

except pymysql.OperationalError:
    print("Upss... Ha ocurrido un error.\n")

print("-------------------------------------------------------------\n")

#Asignamos la FK para la tabla pago_empleados
try:
    cur.execute("ALTER TABLE pago_empleados \
                ADD CONSTRAINT fkId_empleado FOREIGN KEY(id_empleado)\
                REFERENCES datos_empleados(id_empleado);")

    #Ahora podemos poseer una BD un tanto relacional 
    print("Se asigno la FK a la tabla pago_empleados.\n")
except:
    print("No se pudo asignar la FK a la tabla...\n")
print("-------------------------------------------------------------\n")


#Ingresando registros a la tabla datos_empleados
try:
    cur.execute("""INSERT INTO datos_empleados(nombre, apellido, direccion)\
                  VALUES
                    ('Amilcar', 'Lopez','San Vicente,San Vicente, ES'),
                    ('Rosa', 'Calix','San Miguel,San Miguel, ES'),
                    ('Mariana', 'Campos','Guatajiagua,Morazan, ES'),
                    ('Jaquelin', 'Bonilla','San Miguel,San Miguel, ES'),
                    ('Dayana', 'Vasquez','Guatajiagua,Morazan, ES');
                """)

    #Omitimos el id_empleado ya que se va incrementando automaticamente
    print("Se han insertado los registros de forma correcta.\n")
    
except:
    print("Ha ocurrido un error... Intentelo mas tarde.\n")
print("-------------------------------------------------------------\n")


#Ingresando registros a la tabla pago_empleados
try:
    #Cada hora se pagara a $18.75 jajajaj
    cur.execute("""INSERT INTO pago_empleados(horas, sueldo, id_empleado)\
                  VALUES
                    (8,150, 1),
                    (18,337.75, 2),
                    (3,187.50, 3),
                    (18,337.75, 4),
                    (19,356.25, 5);
                """)
    
    #Omitimos el id_pago ya que se va incrementando automaticamente
    #Si le asignamos manualmente el valor que hara de FK entre las tablas 
    print("Se han insertado los registros de forma correcta.\n")
    
except:
    print("Ha ocurrido un error... Intentelo mas tarde.\n")
print("-------------------------------------------------------------\n")

conexion.close() #Cerramos conexión


