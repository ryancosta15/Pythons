#Este código desenvolvido por Ryan Costa mostra a relação de seu nascimento com o seu ano de alistamento militar
#imports
from datetime import date
from time import sleep

#variáveis
anonasc=int(input("Digite em que ano você nasceu:"))
anoatual=date.today().year
idade= 2022-anonasc

#condicional
if anonasc==int:
    if idade==18:
        print("Vai se alistar!!!")
    elif idade<18:
        print("Você só vai se alistar daqui a {} ano(s)".format(18-idade))
        sleep(1)
        print("O exercito te espera em {}".format(anoatual+(18-idade)))
    elif idade>18:
        print("Você se alistou faz {} anos(s)".format(idade-18))
        sleep(1)
        print("O ano de {} deve ter sido difícil!".format(anoatual-(idade-18)))