#finished
from pydoc import doc
from re import I, S
def estudo():
    C=0
    pronto=False
    while pronto!=True:
        C=C+1
        print (str("estudando..."))
        print ("Fiz a lista pela",C,"ª vez")
        pronto=str(input("Já estou pronto?[S/N]"))
        if pronto=="S":
            pronto=True
            print("Posso descansar")
            return C                      
        elif pronto=="N":
            pronto=False
def prova():
    print("------------")
    print("DIA DA PROVA")
    print("------------")
    print("Lendo a prova...")
    print("Resolvendo questões")
    print("Entregando para o professor...")

DIADORESULTADO="----------------\nDIA DO RESULTADO\n----------------"
print("Amanhã terei prova")
estudar=str(input("Devo Estudar?[S/N]"))
if estudar=="S"or estudar=="s":
    vzs=estudo()
    prova()
    if vzs>=4:
        print(DIADORESULTADO)
        print("Fui bem na prova!")
        print("Minha nota foi 10")
    elif vzs<4:
        print(DIADORESULTADO)
        print ("Devia ter estudado mais :(")
        print ("Minha nota foi 5")
elif estudar=="N"or estudar=="n":
    print ("Vou dormir")
    prova()
    print(DIADORESULTADO)
    print ("Devia ter estudado :(")
    print ("Minha nota foi 0")