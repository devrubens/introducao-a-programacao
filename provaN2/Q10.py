'''

Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de
caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

'''


def positivoOuNegativo(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'



print(positivoOuNegativo(1))
print(positivoOuNegativo(0))
print(positivoOuNegativo(-1))
