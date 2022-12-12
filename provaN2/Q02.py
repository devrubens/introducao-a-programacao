'''

Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.


'''


lista = []

for i in range(10):
    lista.append(float(input('Digite um número: ')))


lista.reverse()


print(lista)
