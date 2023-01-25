def muda_valor(param):
    param += 'x'
    print('Dentro da função:', param)
lista = ['a','b','c']
palavra = 'abc'
muda_valor(lista)
muda_valor(palavra)
print(lista)
print(palavra)