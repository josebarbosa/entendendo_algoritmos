# Exercício 4.3 encontre o valor mais alto em uma lista
def mais_alto_lista(lista):
    maximo = lista.pop(0)
    for i in range(0, len(lista)):
        if(lista[i] > maximo):
            maximo = lista[i]
    return maximo
            

lista=[0, 1, 2, 21, 12, 3, 4, 5, 6, 5]
print(mais_alto_lista(lista))