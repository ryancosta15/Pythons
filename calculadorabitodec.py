bin=int(input("Digite o número em binário "))
lenght=len(str(bin))
value=bin
dec=0
i=0
rest=bin%10
while lenght >= 0 <=8:
        dec=dec+(rest*(2**i))
        lenght=lenght-1
        i=i+1
        bin = bin//10
        print("O número", value ,"em decimal é",dec)