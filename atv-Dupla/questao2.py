'''

02. Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números
primos existentes entre 1 e um número inteiro informado pelo usuário.

'''
final = int(input("Numero: "))
comeco = 1

for i in range(comeco, final+1): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i)

