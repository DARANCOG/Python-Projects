# Ejercicio 1
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]

for saludo in alumnos_clase:
    print(f'Hola {saludo}')

# Ejercicio 2
lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]
numero = 0
for suma in lista_numeros:
    numero = numero + suma

suma_numeros = numero

# Ejercicio 3

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for num in lista_numeros:
    if num % 2 == 0:
        suma_pares = suma_pares + num
    else:
        suma_impares = suma_impares + num