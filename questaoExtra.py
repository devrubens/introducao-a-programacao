'''
Em um cinema as cadeiras são numeradas sequencialmente, começando no canto esquerdo
próximo à tela. Essas cadeiras estão organizadas em 40 fileiras de 20 cadeiras. Faça um algoritmo
que informe em que fileira se encontra determinada cadeira, e sua posição em relação ao início da
fileira.
'''

cadeira = int(input("Digite o número da cadeira: "))
fileira = cadeira // 20
posicao = cadeira % 20


if fileira >= 41:
    print ("não tem essa cadeira no cinema")
else:
    print("A cadeira está na fileira", fileira, "e está na posição", posicao, "da fileira")

