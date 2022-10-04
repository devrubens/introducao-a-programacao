'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma
data válida.
'''

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia = int(data[0:2])

mes = int(data[3:5])

ano = int(data[6:10])

if dia > 31 or dia < 1:
    print("Dia inválido")
elif mes > 12 or mes < 1:
    print("Mês inválido")
elif ano >= 0:
    print("Ano inválido")
else:
    print("Data válida")
