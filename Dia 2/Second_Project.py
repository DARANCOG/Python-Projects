#comisiones del 13%, ayudar a calcular las comisiones, nombre y ventas = a nombre y comisiones

nombre = input("Digite Su Nombre ")
ventas = input("Digite el valor en COP de sus ventas totales ")
total = round((int(ventas)*13/100))
print(nombre + " " + "el total de su comision es: $" + f"{total}")

