'''

Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

'''


# Entrada

data = input('Digite a data de nascimento: ')

# Processamento

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Saída

print('Você nasceu em: ', dia, 'de', meses[mes - 1], 'de', ano)
