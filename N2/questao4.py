"""

04. Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa
inicial, em gramas, fazer um programa em Python que determine o tempo necessário para que essa
massa se torne menor que 0,5 grama. Escreva a massa inicial, a massa final e o tempo calculado em
segundos.

"""

massa_inicial = float(input("Digite a massa inicial em gramas: "))
massa_final = massa_inicial / 2
tempo = 50

while massa_final > 0.5:
    massa_final /= 2
    tempo += 50

print(f"Massa Inicial: {massa_inicial:.2f}g")
print(f"Massa Final: {massa_final:.2f}g")
print(f"Tempo: {tempo} segundos")
