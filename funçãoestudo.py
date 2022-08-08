from pydoc import doc
from re import I, S
def estudo():
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
    print("Lendo a prova...")
    print("Resolvendo questões")
    print("Entregando para o professor...")

print("Amanhã terei prova")
estudar=str(input("Devo Estudar?[S/N]"))
if estudar=="S":
    estudo()
    print(estudo)
    prova()
    if estudo>=4:
        print("Fui bem na prova!")
        print("Minha nota foi 10")
    elif estudo<4:
        print ("Devia ter estudado mais :(")
        print ("Minha nota foi 5")
elif estudar=="N":
    print ("Vou dormir")
    prova()
    print ("Devia ter estudado :(")
    print ("Minha nota foi 0")