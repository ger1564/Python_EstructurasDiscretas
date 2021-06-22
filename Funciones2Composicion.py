from matplotlib import pyplot
import math as mt



'''
Sea f(x) = raiz(x)  y g(x) = x + 1 
'''

'''
Encontrar la gráfica de (f o g)(x) =  raiz(x+1)
Encontrar la gráfica de (g o f)(x) =  raiz(x) + 1
'''

#Función f(x)
def f(x):
    return mt.sqrt(x)

#Función g(x)
def g(x):
    return x + 1

#Función (f o g)(x) =  raiz(x+1)
def fog(x):
    return mt.sqrt(x + 1)

#Función (g o f)(x) =  raiz(x) + 1
def gof(x):
    return mt.sqrt(x) + 1



#Graficar la función
# Valores del eje X que toma el gráfico.
x = range(0, 50)
pyplot.title("ff")
pyplot.plot(x, [f(i) for i in x], label = "f(x)", color = "orange")
pyplot.plot(x, [g(i) for i in x], label = "g(x)", color = "red")
pyplot.plot(x, [fog(i) for i in x], label = "(f o g)(x)", color = "blue")
pyplot.plot(x, [gof(i) for i in x], label = "(g o f)(x)", color = "green")

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
pyplot.title("Composición de funciones", fontsize = 18, color = "blue")
pyplot.xlabel("Eje x")
pyplot.ylabel("Eje y")
pyplot.grid(color = 'gray', linestyle = 'dashed')
# Limitar los valores de los ejes.
pyplot.xlim(-5, 20)
pyplot.ylim(-5, 20)
pyplot.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

# Mostrar el gráfico
pyplot.show()