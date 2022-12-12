'''

Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.


'''

# Entrada

lista = []

for i in range(10):
    lista.append(float(input('Digite um número: ')))

# Processamento

lista.reverse()

# Saída

print(lista)
