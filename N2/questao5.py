cont = 1
casa1 = 1
casa2 = 1 * 2
print(casa1,"grãos")
print(casa2,"grãos")
while cont <= 64:
    casa3 = casa2 * 2
    print(casa3,"grãos")
    casa1 = casa2
    casa2 = casa3
    cont = cont +1