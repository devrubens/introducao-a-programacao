'''

Escreva um programa que imprima a tabuada de adição de um número informado pelo
usuário.

'''

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    for i in range(1, 11):
        print("{} + {} = {}".format(num, i, num + i))
