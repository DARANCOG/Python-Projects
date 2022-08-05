from random import *
aleatorio = randint(1,50)
aleatorio2 = uniform(1,5)
aleatorio3 = round(uniform(1,5),1)
aleatorio4 = random()
print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)

colores = ['azul','rojo','verde','amarillo']
aleatorio5 = choice(colores)
print(aleatorio5)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

# Ejercicio N°1
from random import *
aleatorio = randint(1,10)

# Ejercicio N°2
from random import *
aleatorio8 = random()
print(aleatorio8)

# Ejercicio N°3
from random import *
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)