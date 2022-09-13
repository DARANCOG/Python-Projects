def chek_3num(valor):
    return valor in range(100, 1000)


numero = chek_3num(900)
print(numero)


def chek(val):
    lista = []
    for n in val:
        if n in range(100, 1000):
            lista.append(n)
        else:
            pass
    return lista


resultado = chek([100, 200, 1000])
print(resultado)


# Ejercicio N°1
def todos_positivos(val):
    for n in val:
        if n in range(-1000000, -1):
            return False
        else:
            pass
    return True


lista_numeros = todos_positivos([1, 4, 20, 10, -8])
print(lista_numeros)
# Ejercicio N°2


lista_numeros = [1, 50, 500, 5000, 750, 600]


def suma_menores(lista_numeros3):
    suma = 0
    for numero2 in lista_numeros3:
        if numero2 in range(1, 1000):
            suma += numero2
        else:
            pass
    return suma


# Ejercicio N°3


lista_numeros2 = [1, 50, 502, 755, 34]


def cantidad_pares(lista_numeros4):
    lista = 0
    for n in lista_numeros4:
        if n % 2 == 0:
            lista += 1
        else:
            pass
    return lista
