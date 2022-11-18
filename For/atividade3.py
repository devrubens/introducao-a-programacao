"""

3. Faça um outro programa que gere a série até que o valor seja maior que 500.

"""

# Variáveis
fibonacci = [1, 1]

# Processamento
while fibonacci[-1] < 500:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
    
# Saída de dados
print(fibonacci)
