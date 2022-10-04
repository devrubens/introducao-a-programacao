'''
Ler três números e escrever a diferença entre o maior e o menor valor lido.
'''
valor1 = float(input('Primeiro numero: '))
valor2  = float(input('Segundo numero : '))
valor3 = float(input('Terceiro numero: '))

maior = valor1

if (valor2 > maior):
    maior = valor2
if (valor3 > maior):
    maior = valor3

menor = valor1

if (valor2 < menor):
    menor = valor2
if (valor3 < menor):
    menor = valor3

print('A diferença entre o maior e o menor valor é: ', maior - menor)