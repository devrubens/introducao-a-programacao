"""

2. A série de Fibonacci é formada pela seguinte sequência 1,1,2,3,5,8,13,21,34,55,... Faça
um programa capaz de gerar a série até o n-ésimo termo informado pelo usuário.

"""

# Variáveis
n = int(input("Digite o n-ésimo termo: "))
fibonacci = [1, 1]

# Processamento
for i in range(2, n):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

# Saída de dados
print(fibonacci)
