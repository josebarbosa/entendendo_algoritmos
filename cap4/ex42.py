# Exercício 4.2: escreva uma função recursiva que conte o número de itens de uma lista
def conta_lista(lista):
    if len(lista) == 1:
        return 1
    else:
        lista.pop(0)
        return 1 + (conta_lista(lista))

lista = [2,4,6,8,10]
print(conta_lista(lista))