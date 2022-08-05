lista = (22,42,53,13,65,12,98,54,21,45,89,76,3,234,232,4,556,54,23456,78,432,34567,43,34567,789,98765,23456,)
print(max(lista))
print(min(lista))

nombres = ('luisa','nestor','alfonso','hector')
print(max(nombres))
print(min(nombres))

nombre = ('luIs')
print(min(nombre.lower()))
print(max(nombre.lower()))

dic = {'c1':22,'c2':33}
print(min(dic))
print(min(dic.values()))


# Ejercicio N°1
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(55**12)

# Ejercicio N°2
lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = max(lista_numeros) - min(lista_numeros)

# Ejercicio N°3
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)