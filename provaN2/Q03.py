'''

Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média
anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )

'''


temperaturas = []

for i in range(12):
    temperaturas.append(float(input('Digite a temperatura do mês: ')))


media = sum(temperaturas) / len(temperaturas)
print('Média: ', media)


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(len(temperaturas)):
    if temperaturas[i] > media:
        print('Mês: ', meses[i], 'Temperatura: ', temperaturas[i])
