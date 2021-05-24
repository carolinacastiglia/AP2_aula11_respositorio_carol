from No import No

class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        if self.inicio:
            aux = self.inicio

            while(aux.proximo):
                aux = aux.proximo
            aux.proximo = No(valor)

            self.fim = aux.proximo
            no = aux.proximo
            no.anterior = aux

        else:
            self.inicio = No(valor)

    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia!!")
        
        else:
            aux = self.inicio

            while(aux):
                ant = None
                prox = None

                if aux.anterior:
                    ant = aux.anterior
                if aux.proximo:
                    prox = aux.proximo

                if(ant and prox):
                    print(aux.dado, "- Anterior:", ant.dado, "Próximo:", prox.dado, "\n")

                elif(ant and prox == None):
                    print(aux.dado, "- Anterior:", ant.dado, "Próximo:", None, "\n")

                else:
                   print(aux.dado, "- Anterior:", None, "Próximo:", prox.dado, "\n")
                aux = aux.proximo
            print("-------------------------------")


    def imprimirDoFim(self):
        if self.inicio == None:
            print("Lista vazia!!")

        else:
            aux = self.fim

            while(aux):
                print(aux.dado,"\n")
                aux = aux.anterior

            print("-------------------------------")