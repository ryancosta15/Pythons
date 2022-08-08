import math
a=int(input("Digite o termo com x² "))
b=int(input("Digite o termo com x "))
c=int(input("Digite o termo independente "))
Δ=b**2-4*a*c
x1=int(-b+(math.sqrt(Δ)))/2*a
x2=int(-b-(math.sqrt(Δ)))/2*a
txt="Os resultados desta equação são"
print (str(txt), x1, "&",x2)