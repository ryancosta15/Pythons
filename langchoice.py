from random import choice
from time import sleep
pergunta="Que linguagem devo estudar hoje?"
def head(): 
	print("-"*len(pergunta)+4*"-")
	print("☆ {} ☆".format(pergunta))
	print("-"*len(pergunta)+4*"-")
	sleep(2)
def sorteio():
	result=choice(lista)
	print("Você deve aprender...")
	sleep(2)
	print("-"*len(result)+4*"-")
	print("☆ {} ☆".format(result))
	print("-"*len(result)+4*"-")
head()
tipo=str(input("Quero melhorar meu bakckend ou frontend?[B/F]")).upper().strip()
while tipo!="B" and tipo!="F":
	print("Você deve digitar B ou F")
	tipo=str(input("Quero melhorar meu bakckend ou frontend?[B/F]")).upper().strip()
if tipo=="B":
	lista=["Ruby", "Python", "PHP", "node", "Java"]
	sorteio()
elif tipo=="F":
	lista=["HTML", "CSS", "JS"]
	sorteio()