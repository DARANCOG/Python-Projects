# Ejercicio N°1
lista = ['a','b','c']
indice = 0

for item in lista:
    print(item,indice)
    indice += 1

# Ejercicio N°2

lista2 = ['a','b','c']
for l,item in enumerate(lista2):
    print(item,l)

# Ejericio N°3
lista3 = ['a','b','c']
mi_tuples = list(enumerate(lista3))
print(mi_tuples [1][0])

# Ejercicio N°4
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

# Ejercicio N°5
lista_indices=(list(enumerate("Python")))
print(lista_indices)

# Ejercicio N°6
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre[0] == 'M':
        print(indice)
    else:
        continue
