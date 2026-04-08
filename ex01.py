class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
        
class Lista:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0
        
    def inserir_inicio(self, valor):
        novo = No(valor)
        
        if self.tamanho == 0:            
            self.fim = novo            
        else:
            novo.dir = self.inicio
            self.inicio.esq = novo
            
        self.inicio = novo
        self.tamanho += 1
        
    def inserir_final(self, valor):
        novo = No(valor)
        
        if self.tamanho == 0:            
            self.inicio = novo          
        else:
            self.fim.dir = novo
            novo.esq = self.fim
           
        self.fim = novo        
        self.tamanho += 1       

#A)
    def inserir_dado(self, valor):
        novo = No(valor)
        
        if self.tamanho == 0:
            self.inicio = novo
            self.fim = novo
        else:
            novo.esq = self.fim
            self.fim.dir = novo
            self.fim = novo

        self.tamanho += 1

#B)
    def inserir_posicao(self, posicao, valor):
        
        if posicao <= 1:
            self.inserir_inicio(valor)
            
        elif posicao > self.tamanho:
            self.inserir_final(valor)
            
        else:
            novo = No(valor)
            
            aux = self.inicio
            contador = 1
            
            while contador < posicao - 1:
                aux = aux.dir
                contador += 1
            
            novo.dir = aux.dir
            novo.esq = aux
            
            aux.dir.esq = novo
            aux.dir = novo
            
            self.tamanho += 1

#C)
    def imprimir(self):
        aux = self.inicio
        while aux:
            print(aux.dado, end="  ")
            aux = aux.dir
        print()
    
    def pesquisar(self, valor):
        aux = self.inicio
        while aux:
            if aux.dado == valor:
                return aux
            aux = aux.dir
        return None
    
#D)
    def remover(self, valor):
        aux = self.pesquisar(valor)
        
        if aux is not None:
            if self.tamanho == 1:
                self.inicio = None
                self.fim = None                
            elif aux == self.inicio:
                aux.dir.esq = None
                self.inicio = aux.dir
                aux.dir = None                
            elif aux == self.fim:
                aux.esq.dir = None
                self.fim = aux.esq
                aux.esq = None
            else:
                aux.esq.dir = aux.dir
                aux.dir.esq = aux.esq
                aux.esq = None
                aux.dir = None

            aux = None
            self.tamanho -= 1

lista = Lista()

print("A):")
lista.inserir_dado(10)
lista.inserir_dado(20)
lista.inserir_dado(30)
lista.imprimir()   

print("\nB):")
lista.inserir_posicao(1, 5)   
lista.imprimir()               

lista.inserir_posicao(3, 15)   
lista.imprimir()               

lista.inserir_posicao(10, 40)  
lista.imprimir()               

print("\nD):")
lista.remover(5)   
lista.imprimir()    

lista.remover(30)  
lista.imprimir()    

lista.remover(40)   
lista.imprimir()    

print("\nC):")
lista.imprimir()    