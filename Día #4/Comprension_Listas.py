palabra2 = 'python'
lista2 =[]
for letra2 in palabra2:
    lista2.append(letra2)
print(lista2)

palabra = 'python'
lista = [letra for letra in palabra]
print(lista)

lista3 = [n for n in range(0,21,2) if n * 2 > 10]
print(lista3)

lista4 = [n if n * 2 > 10 else ' no' for n in range (0,21,2)]
print(lista4)

pies = [10,20,30,40,50]
metros = [pie* 3.281 for pie in pies]
print(metros)

# Ejercicio N°1
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrados = [numero**2 for numero in valores]
print(valores_cuadrados)

# Ejercicio N°2
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [ n for n in valores if n % 2 == 0]
print(valores_pares)

# Ejercicio N°3
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(f-32)*(5/9) for f in temperatura_fahrenheit]