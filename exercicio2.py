from re import L


def soma_elementos(l):
    soma = i = 0
    for i in l:
        soma += i
    return soma

print(soma_elementos([1,2,3]))