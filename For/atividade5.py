"""

5. Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar
em 10, o valor inicial e final devem ser informados também pelo usuário, conforme
exemplo abaixo:

"""

# Variáveis
numero = int(input("Digite um número: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))
tabuada = []

# Processamento
for i in range(inicio, fim + 1):
    tabuada.append(numero * i)

# Saída de dados
print(tabuada)
