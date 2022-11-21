'''

Escreva um programa que peça para o usuário entrar com um número enquanto ele
desejar e ao final mostre a quantos desses números eram pares.

'''
sair = 1
con = 0
cont_pares = 0

while sair != 0:
    num = int(input("Digite um número: "))
    con = con + 1

    if num % 2 == 0:
        cont_pares = cont_pares + 1
    
    if num == 0:
        sair = 0
        print("Você digitou {} números".format(con))
        print("Desses, {} eram pares".format(cont_pares))
