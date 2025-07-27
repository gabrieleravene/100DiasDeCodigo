# sistema de gestão laboratorial

# O programa possui as funcionalidades de:
# 1 - Cadastrar paciente
# 2 - Cadastrar exame
# Cadastrar analista

class Laboratorio:
    def __init__(self):
        self.exames = []
        self.pacientes = []
        self.analistas = []
        
    def cadastrar_paciente(self, nome, cpf, data_nascimento):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                print("Paciente já cadastrado.")
                return None
        
        prontuario = len(self.pacientes) + 1
        novo_paciente = Paciente(nome, cpf, data_nascimento, prontuario)
        self.pacientes.append(novo_paciente)
        print(f"Novo paciente cadastrado com sucesso! {novo_paciente}")
        return novo_paciente
    
    def cadastrar_analista(self, nome, cpf, data_nascimento, registro):
        for analista in self.analistas:
            if analista.cpf == cpf:
                print("Analista já cadastrado.")
                return None
            
        novo_analista = Analista(nome, cpf, data_nascimento, registro)
        self.analistas.append(novo_analista)
        print(f"Novo analista cadastrado com sucesso! {novo_analista}")
        return novo_analista
    
    def cadastrar_exame(self, nome, paciente, data):
        novo_exame = Exame(nome, paciente, data)
        self.exames.append(novo_exame)
        print(f"Novo exame cadastrado com sucesso. Exame: {novo_exame}")
        return novo_exame
     
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
    def __init__(self, nome, paciente, data):
        self.nome = nome
        self.paciente = paciente
        self.data = data
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
              4 - Encerrar programa
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
            nome = input("Exame: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            registro = input("Registro: ")
            laboratorio.cadastrar_analista(nome, cpf, data_nascimento, registro)
            
        elif opcao == "4":
            print("Encerrando programa...")
            break
        
        else:
            print("Opção inválida.")