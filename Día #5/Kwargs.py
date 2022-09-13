def suma(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total


suma(x=2, y=3, z=4)


def prueba(num1, num2, *arg, **wkargs):
    print(f'el num1 es = {num1}')
    print(f'el num2 es = {num2}')

    for n in arg:
        print(n)

    for clave, valor in wkargs.items():
        print(f'{clave} = {valor}')


prueba(15, 12, 100, 200, 300, 400, y='uno', x='dos', z='tres')


# Ejercicio N°1
def cantidad_atributos(**kwargs):
    return len(kwargs)


# Ejercicio N°2
def lista_atributos(**kwargs):
    lista = []
    for valor in kwargs.values():
        lista.append(valor)
    return lista


# Ejercicio N°3

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}:')

    for clave, valor in kwargs.items():
        print(f'{clave}: {valor}')
