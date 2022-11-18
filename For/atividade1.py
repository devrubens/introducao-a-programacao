"""

1. Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
pares e a quantidade de impares.

"""

# Variáveis
numeros = []
pares = []
impares = []

# Entrada de dados
for i in range(10):
    numeros.append(int(input("Digite um número: ")))

# Processamento
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

# Saída de dados
print("Números pares: ", pares)
print("Números ímpares: ", impares)
