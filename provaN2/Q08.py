'''

Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
Digite uma letra: A
-> Você errou pela 1a vez. Tente de novo!
Digite uma letra: O
A palavra é: _ _ _ _ O
Digite uma letra: E
A palavra é: _ E _ _ O
Digite uma letra: S
-> Você errou pela 2a vez. Tente de novo!

'''


palavras = open('palavras.txt', 'r')
palavras = palavras.read().split('\n')

import random
palavra = palavras[random.randint(0, len(palavras) - 1)]

letras = []
for i in range(len(palavra)):
    letras.append('_')


erros = 0

while erros < 6:
    letra = input('Digite uma letra: ')
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras[i] = letra
    else:
        erros += 1
        print('-> Você errou pela', erros, 'a vez. Tente de novo!')

    print('A palavra é: ', end='')
    for i in range(len(letras)):
        print(letras[i], end=' ')
    print()

    if '_' not in letras:
        print('Você ganhou!')
        break

if erros == 6:
    print('Você perdeu!')


