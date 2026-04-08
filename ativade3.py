
# hospital atende pacientes conforme uma lista de chegada, porém, deve-se implementar
# uma mudança para o hospital atender os pacientes por ordem de prioridade, baseado
# na gravidade do problema do paciente (sem perder nenhum paciente da lista)

# REGRAS
# Um paciente prioritário deve, obrigatoriamente, ser atendido antes do paciente simples, mesmo que ele 
# esteja chegado depois


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
    

    def inserir_paciente(self, valor):
        novo = No(valor)
        

        if self.tamanho == 0:
            self.fim = novo
            self.inicio = novo
            self.tamanho += 1
            return
        
        

def atender(self):
    
    if self.tamanho == 0:
        return None
    


def exibir():
    pass

def buscar_nome():
    pass

# programa principal

def main():

    aux = 1
    print("--- Sistema ---")
    print("Digite '1' para INSERIR PACIENTE")
    print("Digite '2' para ATENDER PACIENTE (O primeiro da fila)")
    print("Digite '3' para EXIBIR A LISTA DE PACIENTES")
    print("Digite '4' para BUSCAR UM PACIENTE")
    print("Digite '5' para SAIR")


    while aux != 5:
        aux = int(input('Digite a ação: '))

        match aux:
            case 1:
                nome_paciente = input('Digite o nome do paciente: ')
                prioridade = bool(input('Digite a situação do paciente (Digite 1 para PRIORIDADE e 0 para SIMPLES): '))

                if prioridade == 0 or prioridade == 1:
                    Lista.inserir_paciente(nome_paciente, bool(prioridade))
                    print("Paciente inserido.")
                    
            case 2:
                if Lista.tamanho != 0:
                    paciente = Lista.atender()
                    print("Paciente atendido.")
            
            case 3:  
                Lista.exibir()

            case 4: 
                nome_paciente = input('Digite o nome do paciente: ')

            case 5:
                break  
    

if __name__ == '__main__':
    main()
    
