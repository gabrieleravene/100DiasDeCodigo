# gerenciador de consultas médicas

# O programa realiza as operações:
# Cadastrar paciente
# Cadastrar médico
# Cadastrar consulta

from datetime import datetime

class Consultorio:
    def __init__(self):
        self.pacientes = []
        self.medicos = []
        self.consultas = []
        
    def cadastrar_paciente(self, nome, cpf, data_nascimento, endereco):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                print("Paciente já está cadastrado.")
                return None
        novo_cadastro = Paciente(nome, cpf, data_nascimento, endereco)
        self.pacientes.append(novo_cadastro)
        print(novo_cadastro)
        return novo_cadastro
    
    def cadastrar_medico(self, nome, cpf, crm, especialidade):
        for medico in self.medicos:
            if medico.cpf == cpf:
                print("Médico já cadastrado.")
                return None
        novo_medico = Medico(nome, cpf, crm, especialidade)
        self.medicos.append(novo_medico)
        print(novo_medico)
        return novo_medico
    
    def cadastrar_consulta(self, paciente_cpf, medico_crm, data_horario):
        paciente = next((p for p in self.pacientes if p.cpf == paciente_cpf), None)
        if not paciente:
            print("Paciente não encontrado.")
            return None
        
        medico = next((m for m in self.medicos if m.crm == medico_crm), None)
        if not medico:
            print("Médico não encontrado.")
            return None
        
        for consulta in self.consultas:
            if consulta.medico.crm == medico_crm and consulta.data_horario == data_horario:
                print("Já existe uma consulta agendada com este médico neste horário.")
                return
        
        nova_consulta = Consulta(paciente, medico, data_horario)
        self.consultas.append(nova_consulta)
        print("Consulta cadastrada com sucesso.")
        print(nova_consulta)
        return nova_consulta
                
class Paciente:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Endereço: {self.endereco} "
        
class Medico:
    def __init__(self, nome, cpf, crm, especialidade):
        self.nome = nome
        self.cpf = cpf
        self.crm = crm
        self.especialidade = especialidade
        self.pacientes = []
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, CRM: {self.crm}, Especialidade: {self.especialidade}"

class Consulta:
    def __init__(self, paciente, medico, data_horario):
        self.paciente = paciente
        self.medico = medico
        self.data_horario = data_horario
        
    def __str__(self):
        return f"Consulta - Paciente: {self.paciente.nome}, Médico: {self.medico.nome}, Data e horário: {self.data_horario}"

if __name__ == "__main__":
    consultorio = Consultorio()
    
    while True:
        print(""" Gerenciador de consultas médicas:
              1 - Cadastrar paciente
              2 - Cadastrar médico
              3 - Cadastrar consulta
              4 - Encerrar o programa
              """)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input('Nome: ')
            cpf = input('CPF: ')
            data_nascimento = input('Data de nascimento: ')
            endereco = input('Endereço: ')
            consultorio.cadastrar_paciente(nome, cpf, data_nascimento, endereco)
            
        elif opcao == '2':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            crm = input("CRM: ")
            especialidade = input("Especialidade: ")
            consultorio.cadastrar_medico(nome, cpf, crm, especialidade)
            
        elif opcao == '3':
            paciente_cpf = input("CPF do paciente: ")
            medico_crm = input("CRM do médico: ")
            data_str = input("Data:  ")
            horario_str = input("Horário: ")
            
            data_horario_str = f"{data_str} {horario_str}"
            
            try:
                data_horario = datetime.strptime(data_horario_str, "%d/%m/%Y %H:%M")
            except ValueError:
                print("Data ou horário em formato inválido.")
            else:
                consultorio.cadastrar_consulta(paciente_cpf, medico_crm, data_horario)
        
        elif opcao == '4':
            print("Encerrando programa...")
            break
        
        else:
            print("Opção inválida.")