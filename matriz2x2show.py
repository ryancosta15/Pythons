from tkinter import N


a11=int(input("Digite a11:"))
a12=int(input("Digite a12:"))
a21=int(input("Digite a21:"))
a22=int(input("Digite a22:"))
print("Sua matriz deve se parecer com isso:")
print (" ",a11,a12,"\n ",a21,a22)
det2x2=a11*a22-a12*a21
print("E seu determinate se parece com isso:")
print ("|",a11,a12,"|\n|",a21,a22,"|")
print(det2x2)