'''

03. Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
    • Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    • Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
        A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
        percentual do ano anterior. Faça um programa que determine o salário atual desse
        funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
        salário inicial do funcionário.

'''

salario = float(input("Informe o salário: "))
ano = 1995
aumento = salario * 0.015
atual = 2022
while ano < atual:
    salario = salario + aumento 
    if ano >= 1997:
        salario = salario + aumento 
        aumento = aumento + aumento
        
    
    ano = ano +1
    print("Ano:{0} R$ {1} ".format(ano,salario))