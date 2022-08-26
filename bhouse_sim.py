preço=(float(input("Qual o valor da casa? R$"))) 
anos=(int(input("Em quantos anos você vai pagar? ")))
parcela=preço/(anos*12)
salário=float(input("Qual o seu salário?R$"))
print("Para pagar R${:.2f} em {} anos você gastará R${:.2f} por mês".format(preço,anos,parcela))
ttporcent=float(3*salário/10)
gastoano=ttporcent*12
faltano=preço/gastoano
if ttporcent>=parcela:
    print("Utilizando 30%"," do seu salário({:.2f}) você consegue pagar a casa no tempo desejado".format(ttporcent))
else:
    print("Você só pode pagar R${:.2f} por mês! Você só vai conseguir pagar em {:.0f} anos".format(ttporcent, faltano))