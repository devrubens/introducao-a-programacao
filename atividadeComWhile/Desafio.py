'''

Faça um algoritmo que verifique se os dois valores que o analista de mercado digitou
realmente estão de acordo com a lógica de compra e venda de ações citadas (quais são essas ações citadas?). No
entanto, para este desafio, vocês só podem usar um único operador relacional, o ==.
Fica vedado o uso dos demais, ou seja, não se pode usar os operadores <, >, <= , >= e
nem o !=.

'''

num = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

while num == num2:
    print("os valores são iguais e de acordo com a proposta")
    break
else:
    print("os valores são diferentes e não de acordo com a proposta")

