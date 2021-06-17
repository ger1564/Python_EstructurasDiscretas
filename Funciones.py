from matplotlib import pyplot
import math as mt


'''

pip install matplotlib

Librería para crear gráficos en Python
'''

'''FUNCIONES'''

'''
Suponga que a cada elemento de un conjunto A se asigna un único elemento de un conjunto B; la colección de estas
asignaciones se denomina función de A en B. El conjunto A se denomina dominio de la función, y el conjunto B se
denomina conjunto objetivo o codominio.

                        f: A -> B
'''

#Funciones en Python

#Definicón de una función
def Saludo():
    print("Hola Estructuras Discretas")
    print("Grupo 07")


#Llamado de una función
#Saludo()

'''
Argumentos [Parámetros] de una función
Es la información que puede ser pasada a una función [Dominio]
Puedes pasar tantos argumentos como necesites a la función

'''

#Argumentos o paramétros
def Nombre(Nombre, ApellidoPaterno, ApellidoMaterno):
    #print(Nombre+" "+ApellidoPaterno+" "+ApellidoMaterno)
    print(Nombre)
    print(ApellidoPaterno)
    print(ApellidoMaterno)


#Nombre("José","Arroyo","Quiroz")


'''
Número de argumentos variables
'''

#Argumentos variables
def Paises(*pais):
    print("El país es: "+pais[1])
	
#Paises("China", "Rusia", "México", "Perú", "Argentina")	
	
#Argumentos por default

def Ubicacion(ciudad = "CDMX"):
    print("La ciudad donde vive el usuario es: "+ciudad)

#Ubicacion()

'''
Retorno de valores
'''

# def Suma(a, b):
#     resultado = a + b
#     return resultado

# print(Suma(5, 15))


'''
Regresar varios valores
'''


# def Calculadora(x, y):
#     suma = x + y
#     resta = x - y
#     multiplicacion = x * y
#     division = x / y

#     return suma, resta, multiplicacion, division


# suma, resta, multiplicacion, division = Calculadora(10, 5)

# print(suma)
# print(resta)
# print(multiplicacion)
# print(division)

#------------------------------------------------------

# Función lineal.   f(x) = 4x +1
#Preguntar por el rango y el dominio

# def f1(x):
#     return 4*x + 1

# #f1(2) = 9
# print (f1(2))

# #f1(-1) = -3
# print (f1(-1))

# #Graficar la función
# # Valores del eje X que toma el gráfico.
# x = range(-100, 100)
# pyplot.plot(x, [f1(i) for i in x], 'g*')

# # Establecer el color de los ejes.
# pyplot.axhline(0, color="black")
# pyplot.axvline(0, color="black")
# pyplot.title("Función Lineal", fontsize = 18, color = "blue")
# pyplot.xlabel("Eje x")
# pyplot.ylabel("Eje y")
# pyplot.grid(color = 'gray', linestyle = 'dashed')
# # Limitar los valores de los ejes.
# pyplot.xlim(-100, 100)
# pyplot.ylim(-100, 100)


# # Mostrar el gráfico
# pyplot.show()


#------------------------------------------------------


# # # Función cuadrática.  
def f2(x):
    return 2*(x**2) + 5*x - 2

#Graficar la función
# Valores del eje X que toma el gráfico.
x = range(-10, 10)
pyplot.plot(x, [f2(i) for i in x])

# # Establecer el color de los ejes.
# pyplot.axhline(0, color="black")
# pyplot.axvline(0, color="black")
# pyplot.title("Función Cuadrática", fontsize = 18, color = "blue")
# pyplot.xlabel("Eje x")
# pyplot.ylabel("Eje y")
# pyplot.grid(color = 'gray', linestyle = 'dashed')
# # Limitar los valores de los ejes.
# pyplot.xlim(-50, 50)
# pyplot.ylim(-15, 100)


# pyplot.text(10,65,'f2(x)', color = "red")

# # Mostrar el gráfico
# pyplot.show()

#------------------------------------------------------
#Función trigonometrica

def f3(x):
    return mt.sin(x)

#Graficar la función
# Valores del eje X que toma el gráfico.
x = range(-10, 10)
pyplot.plot(x, [f3(i) for i in x])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.title("Función sen(x)", fontsize = 18, color = "blue")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = 'gray', linestyle = 'dashed')
# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)


pyplot.text(10,65,'f3(x)', color = "red")

# Mostrar el gráfico
pyplot.show()

