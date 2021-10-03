import pymysql #Importamos libreria
#Abrimos conexion con el servidor del LocalHost
conexion = pymysql.connect(host='localhost', user='root', passwd='usbw',  port=3307)

#Asignamos un cursor
cur = conexion.cursor()
#Indicamos la Base de Datos sobre la que trabajaremos
cur.execute("USE Planilla_Pago;")

#Se realiza la consulta a ambas tablas
cur.execute("SELECT \
                    datos_empleados.nombre AS nombre,\
                    pago_empleados.sueldo AS sueldo\
                FROM datos_empleados INNER JOIN pago_empleados ON datos_empleados.id_empleado = pago_empleados.id_empleado;")
            #Se fusionan a travez del PK de la tabla Principal y la FK de la tabla secundaria
            #Ahora tenemos una Base de Datos relacional...


#Muestra resultados
myresult = cur.fetchall()

for x in myresult:
    print(x)
    
conexion.close() #Cerramos conexión
