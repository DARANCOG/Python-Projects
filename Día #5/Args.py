def suma(*args):
    sumatoria = 0
    for arg in args:
        sumatoria += arg
    print(sumatoria)


suma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Ejercicio N°1
def suma_cuadrados(*args):
    suma1 = 0
    for n in args:
        suma1 = suma1 + n ** 2
    return suma1


# Ejercicio N°2
def suma_absolutos(*args):
    suma3 = 0
    for arg in args:
        suma3 += abs(arg)

    return suma3


# Ejercicio N°3

def numeros_persona(nombre, *suma_numeros):
    return f'{nombre}, la suma de tus números es {sum(suma_numeros)}'
