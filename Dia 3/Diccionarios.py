cliente = {'nombre':'Dario','apellido':'Castiblanco','peso':88,'altura':1.70}
consulta = cliente['altura']
print(consulta)

diccionario = {'c1':55,'c2':[10,5,3],'c3':{'s1':100,'s2':200}}
print(diccionario['c2'][0])
print(diccionario['c3'])

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
Mayus = dic['c2'][1].upper()
print(Mayus)

print(dic['c2'][1].upper())

diccio = {1:'a', 2:'c'}
diccio[2] = 'b'
diccio[3] = 'c'
print(diccio)

print(diccio.keys())
print(diccio.values())
print(diccio.items())