'''
CONJUNTOS

Un conjunto es una colección desordenada de valores no repetidos.
Los conjuntos de Python son análogos a los conjuntos matemáticos.
El tipo de datos que representa a los conjuntos se llama set.
El tipo set es mutable: una vez que se ha creado un conjunto, puede ser modificado

'''

#Crear un conjunto
vocales = {'a', 'e', 'i', 'o', 'u'}
print(vocales)


#No hay valores repetidos y los elementos no quedan en el mismo orden en el que fueron agregados


#Dato set
print(type(vocales))

#Los sets no tienen orden, no pueden ser modificados,  no pueden tener elementos repetidos pero si se les puede
#agregar elementos
#Una vez que se crea un conjunto(set), no puede ser modificado.
colores = {'rojo', 'azul', 'verde', 'amarillo', 'rojo', 'azul'}
print(colores)


#Acceder a los elementos de un conjunto
#No se pueden acceder mediante un index
#Se pueden recorrer mediante un loop foor
paises = { 'México', 'Rusia', 'China', 'EUA', 'Argentina'}

# for x in paises:
#     print(x)



#Añadir elementos a un conjunto - métod add
paises.add('Venezuela')
# for x in paises:
#     print(x)


#Añadir los elementos de un conjunto a otro - método update
vocales.update(paises)
for x in vocales:
    print(x)

#Eliminar elementos de un conjunto método remove() o  dicard() - no lanza error, a veces
vocales.remove('Rusia')
print(vocales)


#Vaciar un conjunto - clear
colores.clear()
print(colores)

#Eliminar un conjunto - del
del colores
#print(colores)


'''
¿cómo podemos crear un conjunto vacio?
s = { } 
NO- Eso es LA declaración de un diccionario vacio
'''

#Conjunto vacio 
ConjuntoVacio = set()
print(ConjuntoVacio)



'''
Operaciones con conjuntos
'''

'''
La unión se realiza con el caracter | y retorna un conjunto que contiene los elementos que se
encuentran en al menos uno de los dos conjuntos involucrados en la operación.
'''

A = {1, 2, 3}
B = {4, 5, 6}

union = A | B


print(union)

'''
La intersección opera de forma análoga, pero con el operador &, y retorna un nuevo conjunto con los
elementos que se encuentran en ambos
'''

C = {1, 2, 3, 4, 5}
D = {4, 5, 6, 7, 8}

interseccion = C & D

print(interseccion)

'''
La diferencia, por último, retorna un nuevo conjunto que contiene los 
elementos de a que no están en b.
'''


e = {1 , 2, 3, 4}
f = {2, 3}

diferencia_e_f = e -f
print(diferencia_e_f)

diferencia_f_e = f -e
print(diferencia_f_e)


'''
Dos conjuntos son iguales si y solo si contienen 
los mismos elementos (a esto se lo conoce como principio de extensionalidad):
'''

g = {'a', 'b', 'c'}
h = {'c', 'b', 'a'}

if g == h:
    print("Los conjuntos son iguales")
else:
    print("Los conjuntos son diferentes")

'''
Se dice que B es un subconjunto de A cuando todos los elementos de aquél pertenecen 
también a éste. Python puede determinar esta relación vía el método issubset().
'''

I = {1 , 2, 3, 4}
J = {2, 3}

if J.issubset(I):
    print("El conjunto J es subconjunto del conjunto I")
else:
    print("El conjunto J NO es subconjunto del conjunto I")