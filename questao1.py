'''
Ler duas notas, calcular a média e escrever se foi aprovado ou reprovado, a média para
promoção é de no mínimo 5,0.
'''

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 5:
    print("Aprovado")
else:
    print("Reprovado")