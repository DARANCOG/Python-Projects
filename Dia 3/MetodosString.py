texto = "aprendiendo python"
resultado = texto.upper()
print(resultado)

texto = "APRENDIENDO PYHTON"
resultado = texto.lower()
print(resultado)

texto = "Aprendiendo python en pycharm"
resultado = texto.split()
print(resultado)

a = "Aprendiendo"
b = "Python"
c = "en"
d = "pycharm"
e = " ".join([a,b,c,d])
print (e)

texto = "Aprendiendo python en pycharm"
resultado = texto.find("o")
print(resultado)

texto = "Aprendiendo python en pycharm"
resultado = texto.replace("e","x")
print(resultado)

texto = "Si la implementación es difícil de explicar, puede que sea una mala idea."

resultado = texto.replace("difícil","fácil")
print(resultado)


poema = """azxfasf
zxczxcz
zczxczxc"""