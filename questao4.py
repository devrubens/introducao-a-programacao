'''
Fazer um programa em Python para ler duas notas (sistema do IFCE), Calcular a média
(ponderada), dizer se foi aprovado por média (7,0), caso contrário, calcular qual a nota que o
aluno precisa fazer na final para ser aprovado por média final (5,0).
'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = ((nota1 * 2) + (nota2 * 3))/5

if media >= 7:
    print("Aprovado por média")
elif media >= 3:
    notaFinal = 10 - media
    print("Você precisa tirar", notaFinal, "na final para ser aprovado por média final")
else:
    print("Reprovado")