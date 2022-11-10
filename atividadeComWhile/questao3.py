'''

Escreva um programa que forneça um algoritmo de troca de senhas. Ele deve pedir a
senha antiga, pedir a senha nova duas vezes e confirmar a senha nova. O algoritmo
também deve verificar se a senha nova é diferente da antiga.

'''

senhaAntiga = "123"
cont = True

while loop == True:
    senhaNova = input("Digite sua nova senha: ")
    senhaNova2 = input("Digite sua nova senha novamente: ")
    if senhaNova == senhaNova2:
        if senhaNova != senhaAntiga:
            print("Senha alterada com sucesso!")
            loop = False
        else:
            print("A senha nova não pode ser igual a antiga!")
    else:
        print("As senhas não são iguais!")