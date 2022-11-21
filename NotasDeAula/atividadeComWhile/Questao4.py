'''

Escreva um programa que inicialmente peça para o usuário entrar com um número.
Depois, peça para o usuário entrar com um número enquanto ele desejar e acumule
aqueles que são múltiplos do número inicial.

'''

num = int(input("Digite um número: "))
cont = int(input("Digite quantos números deseja digitar: "))
multiplos = 0

while cont != 0:
    num2 = int(input("Digite um número: "))
    if num2 % num == 0:
        multiplos = multiplos + 1
    cont = cont - 1
print("Você digitou {} múltiplos de {}".format(multiplos, num))