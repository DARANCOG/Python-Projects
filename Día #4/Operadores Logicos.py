mi_bool = 5+5==18-8
print(mi_bool)

mi_bool2 = 'blanco'=='Blanco'.lower()
print(mi_bool2)

mi_bool3 = 100!=100
print(mi_bool3)

mi_bool4 = 4 < 5 and 5 > 6
print(mi_bool4)

mi_bool5 = 4 < 5 or 5 > 6
print(mi_bool5)

mi_bool6 = not 5 > 6
print(mi_bool4)

# Ejercicio #1
num1=36
num2=72/2
num3=48
mi_bool= num1>num2 and num1<num3

# Ejercicio #2
num1=36
num2=72/2
num3=48
mi_bool1=num1>num2 or num1<num3

# Ejercicio #3
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

palabra1 = 'éxito'
palabra2 = 'tecnología'

mi_bool3 = not (palabra1 in frase and palabra2 in frase)