nome = 'João Araujo Ribeiro'

lista = nome.split(' ')

print (lista)

lista[1] = lista[1][0] +'.'

print (lista)

lista[0],lista[1],lista[2] = lista[2],lista[0],lista[1]

lista[0] += ','

print (lista)

nome = ' '.join(lista)

print (nome)