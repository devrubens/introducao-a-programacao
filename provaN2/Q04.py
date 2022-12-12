'''

Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor
de contadores(1-6) e uma função para gerar números aleatórios, simulando os lançamentos dos dados.

'''

# Entrada

import random

lancamentos = []

for i in range(100):
    lancamentos.append(random.randint(1, 6))

# Processamento

contadores = [0, 0, 0, 0, 0, 0]

for i in range(len(lancamentos)):
    contadores[lancamentos[i] - 1] += 1

# Saída

for i in range(len(contadores)):
    print('Número: ', i + 1, 'Quantidade: ', contadores[i])
    