#este código foi feito por Ryan Costa com o intuito de classificar os usuários pelo imc deles

#importações
from math import pow
from time import sleep

#variáveis
peso=float(input("Digite seu peso em kg:"))
altura=float(input("Digite sua altura em metros:"))
imc=peso/pow(altura, 2)

#condicional
if imc<18.5:
    clas="MAGREZA"
elif 18.5<=imc<25:
    clas="IDEAL"
elif 25<=imc<30:
    clas="SOBREPESO"
elif 30<=imc<40:
    clas="OBESIDADE"
else:
    clas="OBESIDADE MÓRBIDA"

#exibição de resultado
print("Seu imc é {:.2f}".format(imc))
sleep(0.5)
print("Isto te leva para a classificação...")
sleep(0.7)
print("-"*len(clas))
print("{}".format(clas))
print("-"*len(clas))