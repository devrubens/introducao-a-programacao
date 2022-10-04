'''
Fazer um programa em Python para ler três números, estes números podem ser o
comprimento dos lados de um triângulo. Dizer se estes números podem ser de um triângulo,
caso positivo, classificar em equilátero, isóscele ou escaleno.
'''

valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
valorC = float(input("Digite o valor de C: ")) 

if valorA < valorB + valorC and valorB < valorA + valorC and valorC < valorA + valorB:
    if valorA == valorB and valorB == valorC:
        print("Triângulo equilátero")
    elif valorA == valorB or valorB == valorC or valorA == valorC:
        print("Triângulo isóscele")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")
