"""

01. A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que
gere a série até que o valor seja maior que 500.

"""

Fibonacci = 0
Fibonacci1 = 1

while Fibonacci <= 500:
    Fibonacci = Fibonacci + Fibonacci1
    Fibonacci1 = Fibonacci - Fibonacci1
    print(Fibonacci)