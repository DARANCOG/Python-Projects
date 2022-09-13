def multiplicar(num1, num2):
    return num1 * num2


multiplicacion = multiplicar(5, 50)
print(multiplicacion)


# Ejercicio N°1
def potencia(num1, num2):
    return num1 ** num2


# Ejercicio N°2
def usd_a_eur(num1):
    return num1 * 0.90


dolares = usd_a_eur(10)


# Ejercicio N°3
def invertir_palabra(palabra):
    return ''.join(reversed(palabra.upper()))


palabra = invertir_palabra('Curso')

print(palabra)
