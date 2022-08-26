n1=int(input("Digite um número:"))
n2=int(input("Digite outro número:"))
if n1=="" or n2=="":
    print("Você não digitou os números corretamente") 
else:
    if n1>n2:
        print("{} é maior que {}".format(n1,n2))
    elif n1<n2:
        print("{} é menor que {}".format(n1,n2))
    elif n1==n2:
        print("{} é igual a {}".format(n1,n2))