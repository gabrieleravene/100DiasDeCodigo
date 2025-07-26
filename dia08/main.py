# sistema de gestão laboratorial

# O programa possui as funcionalidades de:
# 1 - Cadastrar paciente
# 2 - Cadastrar exame

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
        
        novo_paciente = Paciente(nome, cpf, data_nascimento)
        self.pacientes.append(novo_paciente)
        print("Noov paciente cadastrado com sucesso.")
        return novo_paciente
        
    def cadastrar_exame(self, nome, paciente, data):
        novo_exame = Exame(nome, paciente, data)
        self.exames.append(novo_exame)
        print("Novo exame cadastrado com sucesso.")
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
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.nascimento}, Prontuário: {self.prontuario}"
        
class Exame:
    def __init__(self, nome, paciente, data):
        self.nome = nome
        self.paciente = paciente
        self.data = data
        self.laudo = ""
        
    def __str__(self):
        return f"Nome: {self.nome}, Paciente: {self.exame}, Data: {self.data}, Laudo: {self.laudo}"