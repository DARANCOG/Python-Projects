if 9 < 8:
    print('es correcto')
else:
    print('no es correcto')

mascota = 'perro'
if mascota == 'gato':
    print('tienes un gato')
elif mascota == 'perro':
    print('tienes un perro')
else:
    print('¿que animal tienes?')

edad = input(f'digite su edad: ')
calificacion = input(f'digite su calificacion: ')

if int(edad) >= 18:
    print('Usted es mayor de edad')
    if int(calificacion) >= 7:
        print('Usted aprobo')
    else:
        print('Usted Reprobo')
else:
    print('Usted es menor de edad')

# Ejercicio #1
num1 = input("Ingresa un número:")
num2 = input("Ingresa otro número:")

if num1 > num2:
    print(f'{num1}' + ' es mayor que ' + f'{num2}')
elif num2 > num1:
    print(f'{num2}' + ' es mayor que ' + f'{num1}')
else:
    print(f'{num1}' + ' y ' + f'{num2}' + ' son iguales ')

# Ejercicio #2
habla_ingles = False
sabe_python = False

if habla_ingles == True and sabe_python == True:
    print('Cumples con los requisitos para postularte')
elif habla_ingles == False and sabe_python == True:
    print('Para postularte, necesitas tener conocimientos de inglés')
elif habla_ingles == True and sabe_python == False:
    print('Para postularte, necesitas saber programar en Python')
else:
    print('Para postularte, necesitas saber programar en Python y tener conocimientos de inglés')

# Ejercicio #3
edad = 16
tiene_licencia = False

if edad >= 18 and tiene_licencia == True:
    print("Puedes conducir")

elif edad >= 18 and tiene_licencia == False:
    print("No puedes conducir. Necesitas contar con una licencia")

else:
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

