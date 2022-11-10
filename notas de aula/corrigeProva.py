questaoUm = ("b")
questaoDois = ("a")
questaoTres = ("d")

contador = 1

print("Responda as questões com a, b, c ou d")

while contador <= 3:
    questaoUm = input("Digite a letra da questão 1: ")
    if questaoUm == "b":
        print("Resposta correta")
        contador = contador + 1
    else:
        print("Resposta incorreta")
        contador = contador + 1
    questaoDois = input("Digite a letra da questão 2: ")
    if questaoDois == "a":
        print("Resposta correta")
        contador = contador + 1
    else:
        print("Resposta incorreta")
        contador = contador + 1
    questaoTres = input("Digite a letra da questão 3: ")
    if questaoTres == "d":
        print("Resposta correta")
        contador = contador + 1
    else:
        print("Resposta incorreta")
        contador = contador + 1
    print("Fim do programa!")