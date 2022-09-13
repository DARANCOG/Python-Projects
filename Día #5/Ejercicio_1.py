"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""


def devolver_distintos(int1, int2, int3):
    suma = int1 + int2 + int3
    lista =[int1 , int2, int3]

    if suma > 15:
        return f'el número mayor es {max(lista)}'
    elif suma < 10:
        return f'el número menor es {min(lista)}'
    else:
        lista.sort()
        return f'el número de valor intermedio es {lista[1]}'


print(devolver_distintos(1, 2, 7))
