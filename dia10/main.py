# sistema de gestão laboratorial

# O programa possui as funcionalidades de:
# 1 - Cadastrar paciente
# 2 - Cadastrar exame
# 3 - Cadastrar analista
# 4 - adicionar laudo
# 5 - Exibir lista de pacientes
# 6 - Exibir lista de analistas
# 7 - Exibir lista de exames

class Laboratorio:
    def __init__(self):
        self.exames = []
        self.pacientes = []
        self.analistas = []
        
    def cadastrar_paciente(self, nome, cpf, data_nascimento):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                print("Paciente já cadastado.")
                return None # encerra o loop
        
        prontuario = len(self.pacientes) + 1    
        novo_cadastro = Paciente(nome, cpf, data_nascimento, prontuario)
        self.pacientes.append(novo_cadastro)
        print("Cadastro concluído com sucesso.")
        print(novo_cadastro)
        return novo_cadastro
        
    def cadastrar_analista(self, nome, cpf, data_nascimento, registro):
        for analista in self.analistas:
            if analista.cpf == cpf:
                print("Analista já cadastrado.")
                
        novo_cadastro = Analista(nome, cpf, data_nascimento, registro)
        self.analistas.append(novo_cadastro)
        print("Cadastro realizado com sucesso.")
        print(novo_cadastro)
        return novo_cadastro
    
    def cadastrar_exame(self, nome, paciente, data):
        solicitacao = len(self.exames) + 1
        novo_exame = Exame(nome, paciente, data, solicitacao)
        self.exames.append(novo_exame)
        print(novo_exame)
        
    def exibir_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)
            
    def exibir_analistas(self):
        for analista in self.analistas:
            print(analista)
            
    def exibir_exames(self):
        for exame in self.exames:
            print(exame)
            
    def adicionar_laudo(self, solicitacao):
        for exame in self.exames:
            if exame.solicitacao == solicitacao:
                if exame.laudo:
                    print("Este exame já possui um laudo.")
                    return
                exame.laudo = input("Resultado: ")
                print("Laudo adicionado com sucesso.")
                return
        print("Exame não encontrado.")
        
class Analista:
    def __init__(self, nome, cpf, data_nascimento, registro):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.registro = registro
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Registro: {self.registro}"
    
class Paciente:
    def __init__(self, nome, cpf, data_nascimento, prontuario=None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.prontuario = prontuario
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Prontuário: {self.prontuario}"
    
class Exame:
    def __init__(self, nome, paciente, data, solicitacao=None):
        self.nome = nome
        self.paciente = paciente
        self.data = data
        self.solicitacao = solicitacao
        self.laudo = ""
        
    def __str__(self):
        return f"Nome: {self.nome}, Paciente: {self.paciente}, Data: {self.data}, Laudo: {self.laudo}"

if __name__ == "__main__":
    laboratorio = Laboratorio()
    
    while True:
        print(""" SISTEMA DE GESTÃO LABORATORIAL:
              1 - Cadastrar paciente
              2 - Cadastrar exame
              3 - Cadastrar analista
              4 - Visualizar lista de pacientes
              5 - Visualizar lista de exames
              6 - Visualizar lista de analistas
              7 - Adicionar laudo
              8 - Encerrar programa
              """)
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            laboratorio.cadastrar_paciente(nome, cpf, data_nascimento)
            
        elif opcao == "2":
            nome = input("Exame: ")
            paciente = input("Paciente: ")
            data = input("Data: ")
            laboratorio.cadastrar_exame(nome, paciente, data)
                
        elif opcao == "3":
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            registro = input("Registro: ")
            laboratorio.cadastrar_analista(nome, cpf, data_nascimento, registro)
            
        elif opcao == "4":
            laboratorio.exibir_pacientes()
            
        elif opcao == "5":
            laboratorio.exibir_exames()
            
        elif opcao == "6":
            laboratorio.exibir_analistas()
            
        elif opcao == "7":
            solicitacao = int(input("Digite o número da solicitação: "))
            laboratorio.adicionar_laudo(solicitacao)
            
        elif opcao == "8":
            print("Encerrando programa...")
            break
        
        else:
            print("Opção inválida.")