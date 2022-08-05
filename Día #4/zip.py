nombres = ('esteban','juan','francisco','luis')
edades = (23,4,10)
ciudades = ('lima','peru','madrid','mexico')
combinados = list(zip(nombres,edades,ciudades))
for nombre, edad, ciudad in combinados:
    print(f'nombre {nombre} edad {edad} y vive en {ciudad}')

# Ejercicio N°1
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinados = list(zip(capitales,paises))
for capital, pais in combinados :
    print(f'La capital de {pais} es {capital}')
# Ejercicio N°2
marcas = ('mercedes','apple','bose')
productos = ('autos','celulares','parlantes')
mi_zip = list(zip(marcas,productos))
print (mi_zip)
# Ejercicio N°3
Español = ('uno','dos','tres','cuatro','cinco')
Portugues = ('um','dois','três','quatro','cinco')
Ingles = ('one','two','three','four','five')
numeros = list(zip(Español,Portugues,Ingles))
print(numeros)

