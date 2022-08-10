bin=int(input("Digite o número em binário para ser convertido para a base decimal: "))
n=len(str(bin))
value=bin
dec=0
i=0
if n==str(bin).count("0")+str(bin).count("1"):
        while n>=0<=8:
                resto=int(bin) % 10
                dec=dec+(resto*(2**i))
                n=n-1
                i=i+1
                bin=bin//10
        print("O número {} em decimal é {}".format(value, dec))
else:
        print("O número {} não está em binário".format(bin))
