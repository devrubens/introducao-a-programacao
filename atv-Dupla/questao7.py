"""

07. Fazer um programa que leia a hora, minuto e segundo e converter tudo para segundos.

"""

hora = int(input("Horas: "))
minuto = int(input("Minutos: "))
segundo = int(input("Segundos: "))

cont = 0
while cont <= 2:
  hora = hora * 3600
  minuto = minuto * 60
  segundo = segundo

  print(hora,"/",minuto,"/",segundo)
  total = hora + minuto + segundo
  print("Segundos no total: {} segundos ".format(total))

cont= cont + 1