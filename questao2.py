'''
Dados três valores A, B e C de uma equação do segundo grau (Ax2+Bx+C=0), faça um
programa em Python para calcular o valor das raízes, se para os valores fornecidos for
possível determinar raízes reais.
'''

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: "))

delta = (valorB ** 2) - (4 * valorA * valorC)

if delta < 0:
    print("Não existe raiz real")
else:
    raiz1 = (-valorB + delta ** (1/2)) / (2 * valorA)
    raiz2 = (-valorB - delta ** (1/2)) / (2 * valorA)

    print("Raiz 1: ", raiz1)
    print("Raiz 2: ", raiz2)
