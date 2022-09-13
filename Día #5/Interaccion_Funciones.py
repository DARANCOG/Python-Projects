from random import *

# Lista inicial
palitos = ['-', '__', '___', '____']


# Mezclar Palos
def mezclar(lista):
    shuffle(lista)
    return lista


print(mezclar(palitos))


# Pedirle intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un numero del 1 al 4: ')

    return int(intento)


# Comprobar Intento
def chequear_intento(lista, intento):
    if lista[intento - 1] == '-':
        print("Penitencia")
    else:
        print('No es el palo pequeño')
    print(f'Te ha tocado{lista[intento - 1]}')


palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados, seleccion)


# Ejercicio N°1


def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return (dado1, dado2)


def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif suma_dados > 6 and suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# Ejercicio N°2

lista_numeros = [1, 2, 15, 7, 2, 8]


def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()
    lista.pop(-1)
    return lista


def promedio(lista2):
    SumNum = 0
    for Num in lista2:
        SumNum = SumNum + Num
    promed = SumNum / len(lista2)
    return promed


# Ejercicio N°3

lista_numeros2 = [1, 2, 3, 4, 5, 6]


def lanzar_moneda():
    moneda = ['Cara', 'Cruz']
    shuffle(moneda)
    lanzamiento = moneda[0]
    return lanzamiento


def probar_suerte(lanzamiento, lista):
    if lanzamiento == 'Cara':
        print(f'La lista se autodestruira')
        return []
    elif lanzamiento == 'Cruz':
        print(f'La lista fue salvada')
        return lista
