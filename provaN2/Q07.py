'''

Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
• quantos espaços em branco existem na frase.
• quantas vezes aparecem as vogais a, e, i, o, u.

'''

# Entrada

frase = input('Digite uma frase: ')

# Processamento

espacos = 0
vogais = [0, 0, 0, 0, 0]

for i in range(len(frase)):
    if frase[i] == ' ':
        espacos += 1
    elif frase[i] == 'a' or frase[i] == 'A':
        vogais[0] += 1
    elif frase[i] == 'e' or frase[i] == 'E':
        vogais[1] += 1
    elif frase[i] == 'i' or frase[i] == 'I':
        vogais[2] += 1
    elif frase[i] == 'o' or frase[i] == 'O':
        vogais[3] += 1
    elif frase[i] == 'u' or frase[i] == 'U':
        vogais[4] += 1

# Saída

print('Quantidade de espaços em branco: ', espacos)
print('Quantidade de vogais a: ', vogais[0])
print('Quantidade de vogais e: ', vogais[1])
print('Quantidade de vogais i: ', vogais[2])
print('Quantidade de vogais o: ', vogais[3])
print('Quantidade de vogais u: ', vogais[4])
