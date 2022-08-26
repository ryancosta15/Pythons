#Jogo feito por Ryan Costa com o intuito de simular um jogo de Pedra,papel e tesoura

#importações
from random import choice
from time import sleep

#exibição inicial
frase="Bem vindo ao JOKENPO SIMULATOR"
print("-"*len(frase))
print(frase)
print("-"*len(frase))
sleep (1)
print("""Jogadas:
[1]Pedra
[2]Papel
[3]Tesoura
""")

#funções para jogo
def inicio():
    usuario=int(input("Digite sua jogada:"))
    return usuario
def machine(): 
    jogadas=["PEDRA","PAPEL","TESOURA"]
    sorteio=choice(jogadas)
    return sorteio
sleep(0.5)
res1=inicio()
res2=0
playmach=machine()

#Convertendo nomes
if res1==1:
    play="PEDRA"
elif res1==2:
    play="PAPEL"
elif res1==3:
    play="TESOURA"
else:
    #repetição até um número jogável
    while res2!=1 and res2!=2 and res2!=3:
        print("Você não digitou nenhum número jogável")
        res2=int(input("Digite sua jogada:"))
    if res2==1:
        play="PEDRA"
    elif res2==2:
        play="PAPEL"
    elif res2==3:
        play="TESOURA"
#jogo
def jogo():
    print("Jogador:\"Eu jogo {}!\"".format(play))
    print("Computador:\"Eu jogo {}!\"".format(playmach))
jogo()
if play==playmach: #caso empate
    print("Empate")
    while play==playmach:
        res1=inicio()
        res2=0
        playmach=machine()
        sleep(0.5)
        #Convertendo nomes novamente
        if res1==1:
            play="PEDRA"
        elif res1==2:
            play="PAPEL"
        elif res1==3:
            play="TESOURA"
        else:
            #repetição até um número jogável novamente
            while res2!=1 and res2!=2 and res2!=3:
                print("Você não digitou nenhum número jogável")
                res2=int(input("Digite sua jogada:"))
            if res2==1:
                play="PEDRA"
            elif res2==2:
                play="PAPEL"
            elif res2==3:
                play="TESOURA"
        jogo()
    if play=="PEDRA" and playmach=="PAPEL": #pedra x papel
        print("A sua pedra foi embrulhada pelo papel adversário")#perde
        vitória=False
    elif play=="PEDRA" and playmach=="TESOURA": #pedra x tesoura
        print("A sua pedra esmagou a tesoura adversária")#ganha 
        vitória=True
    elif play=="PAPEL" and playmach=="PEDRA": #papel x pedra
        print("O seu papel embrulhou a pedra adversária")#ganha
        vitória=True
    elif play=="PAPEL" and playmach =="TESOURA": #papel x tesoura
        print("O seu papel foi cortado pela tesoura adversária")#perde
        vitória=False
    elif play=="TESOURA" and playmach=="PEDRA": #tesoura x pedra
        print("A sua tesoura foi esmagada pela pedra adversária")#perde
        vitória=False
    elif play=="TESOURA" and playmach=="PAPEL": #tesoura x papel
        print("A sua tesoura cortou o papel adversário")#ganha
        vitória=True
        #fim de jogo
elif play=="PEDRA" and playmach=="PAPEL": #pedra x papel
    print("A sua pedra foi embrulhada pelo papel adversário")#perde
    vitória=False
elif play=="PEDRA" and playmach=="TESOURA": #pedra x tesoura
    print("A sua pedra esmagou a tesoura adversária")#ganha
    vitória=True
elif play=="PAPEL" and playmach=="PEDRA": #papel x pedra
    print("O seu papel embrulhou a pedra adversária")#ganha
    vitória=True
elif play=="PAPEL" and playmach =="TESOURA": #papel x tesoura
    print("O seu papel foi cortado pela tesoura adversária")#perde
    vitória=False
elif play=="TESOURA" and playmach=="PEDRA": #tesoura x pedra
    print("A sua tesoura foi esmagada pela pedra adversária")#perde
    vitória=False
elif play=="TESOURA" and playmach=="PAPEL": #tesoura x papel
    print("A sua tesoura cortou o papel adversário")#ganha
    vitória=True

#resultado
sleep(0.7)
if vitória==True:
    print("-"*len("Você Venceu!"))
    print("Você Venceu!")
    print("-"*len("Você Venceu!"))
else:
    print("-"*len("Você Perdeu!"))
    print("Você Perdeu!")
    print("-"*len("Você Perdeu!"))    

#fim de jogo
sleep(1)
print("Fim de jogo")