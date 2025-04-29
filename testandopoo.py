class Materia(object):
    n1 = 0
    n2 = 0
    n3 = 0
    def __init__(self, nome = ""):
        self.nome = nome
    def nota(self, q, n1, n2 = 0, n3=0):
        self.q = q
        min = 6
        if q == 1:
            self.n1 = n1
            x = min *3 -n1
            print("faltam {x} pontos para você passar")
            n2, n3 = x/2
            print("Você deve tirar {n2} para passar")
discreta = "matéria"
