#Exercício 4.1: Escreva o código de uma função soma, vista anteriormente (recursiva)
def soma(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista.pop(0) + soma(lista)
        
lista = [2,4,6]
print(soma(lista))
