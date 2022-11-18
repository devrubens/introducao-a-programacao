"""

4. Numa eleição existem três candidatos. Faça um programa que peça o número total de
eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada
candidato.

"""

# Variáveis
eleitores = int(input("Digite o número de eleitores: "))
candidatos = ["A", "B", "C"]

# Processamento
votos = [0, 0, 0]
for i in range(eleitores):
    voto = input("Digite o voto do eleitor: ")
    if voto == candidatos[0]:
        votos[0] += 1
    elif voto == candidatos[1]:
        votos[1] += 1
    elif voto == candidatos[2]:
        votos[2] += 1

# Saída de dados
print("Votos do candidato A: ", votos[0])
print("Votos do candidato B: ", votos[1])
print("Votos do candidato C: ", votos[2])
