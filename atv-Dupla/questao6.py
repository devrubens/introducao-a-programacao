"""

06. Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.m.
Imprima no final a soma da série.

"""
resultado = 0
n = int(input("Digite um numero para inicio do calculo: "))
m = 1

for i in range(1, n + 1):
    print(f"{i}/{m}", end="")
    if i < n and n > 1:
        print(" + ", end="")
    else:
        print(".")
    resultado += i / m
    m += 2
print(f"Resultado da Soma: {resultado:.2f}")
