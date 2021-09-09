#Inicio del código
print("-"*60)
print("Empezando a trabajar con Python")
#Ingresamos el nombre de la persona que escribió el código
print("Realizado por: Daniel Ortiz")
print()

#Escribimos cada dato
#Usamos un print con paréntesis vacíos para añadir un espacio entre líneas
print("Consultando los tipos de valores:")
print()

print("El tipo de dato de 875 es: ")
print(type(875))
print()

print("El tipo de dato de 4.89 es: ")
print(type(4.89))
print()

print("El tipo de dato del texto: 'Now is better than never', es: ")
print(type('Now is better than never'))
print()

print("El tipo de dato de 1.32 es: ")
print(type(1.32))
print()

#Usamos isinstance para verificar si lo que ingresamos corresponde a cierto tipo o no
print("¿El valor 5 + 8i corresponde a un valor entero?")
print(isinstance(5+8j, int))
print()

print("¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(8.2, int))
print()

print("¿El texto: 'Readability counts', corresponde a un string?")
print(isinstance('Readability counts', str))
print()

#Terminamos el código
print("-"*60)
