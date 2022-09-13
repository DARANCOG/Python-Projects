# Programar un Juego de adivina el numero con 8 intentos

from random import *
nombre = input(f'Ingrese su nombre: ')
print(f'Se ha escogido un numero aleatorio del "1 al 100" tiene "8" intentos para adivinarlo')
numero = randint(1,100)
N = 0

veces = 1
while veces < 9:
    veces += 1
    N = int(input(f'Ingrese un numero del 1 al 100: '))
    if N < 1:
        print(f'{nombre} El numero es menor a 1 "Digitar unicamente numeros del 1 al 100"')
    elif N > 100:
        print(f'{nombre} El numero es mayor a 1 "Digitar unicamente numeros del 1 al 100"')
    elif N < numero:
        print(f'{nombre} pista "El numero aleatorio es mayor al numero seleccionado"')
    elif N > numero:
        print(f'{nombre} Pista "El numero aleatorio es menor al numero seleccionado"')
    else:
        print(f'{nombre} El numero es el correcto "Felicidades has acertado el numero en el intento "{veces}"!"')
        break
if numero != N:
    print(f'Lo siento no has acertado el numero, el numero era "{numero}"')