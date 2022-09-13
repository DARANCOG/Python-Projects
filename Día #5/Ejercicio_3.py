"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""

def funcion(*args):
    numero = 0
    for n in args:
        if numero + 1 == len(args):
            return False
        elif args[numero] == 0 and args[numero + 1] == 0:
            return True
        else:
            numero += 1
    return False


print(funcion(1,2,3,4,0,0,6))