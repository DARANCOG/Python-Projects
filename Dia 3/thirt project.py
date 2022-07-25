# Primer Punto

def destildar(letraTildada):
    if letraTildada == "á":
        return "a"
    elif letraTildada == "é":
        return "e"
    elif letraTildada == "í":
        return "i"
    elif letraTildada == "ó":
        return "o"
    elif letraTildada == "ú":
        return "u"
    else:
        return letraTildada

#Primer punto

texto = input('digite un texto: ').lower()
letras = []

letras.append(input("Ingresa la primera letra: ").lower())
letras.append(input("Ingresa la segunda letra: ").lower())
letras.append(input("Ingresa la tercera letra: ").lower())

#letras = input('digite tres letras: ').lower()

# Destildar
textoLista = [destildar(letraxletra) for letraxletra in texto]
letrasLista = [destildar(letraxletra) for letraxletra in letras]

texto = [destildar(letraxletra) for letraxletra in texto]
letras = [destildar(letraxletra) for letraxletra in letras]

texto = "".join(texto)
letras= "".join(letras)

# Conteo

conteo = texto.count(letras[0])
conteo1 = texto.count(letras[1])
conteo2 = texto.count(letras[2])

print('la letra (',letras[0],') se repite', conteo, 'veces')
print('la letra (',letras[1],') se repite', conteo1, 'veces')
print('la letra (',letras[2],') se repite', conteo2, 'veces')


# Segundo Punto
palabras = len(texto.split())
print(f"El texto tiene {str(palabras)} palabras")

# Tercer Punto
print(f"la primera letra del texto es ({ texto[0] }) La ultima letra del texto es ({ texto[-1] })")

# Cuarto Punto

#textoinvertido = texto[::-1]


textoLista.reverse()
textoinvertido = ''.join(textoLista)
print(f"El texto invertido es ( {textoinvertido} )")

# Quinto Punto
# Diccionario y booleano

palabra = 'python' in texto
dic = {True: 'Si' , False: 'No'}
print(f"¿La palabra 'python' aparece en el texto?: ({dic[palabra]})")
