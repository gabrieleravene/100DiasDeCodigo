# Gerenciador de consultas médicas

class Consultorio:
    def __init__(self):
        self.medicos = []
        self.pacientes = []
        self.consultas = []
        
    def cadastrar_paciente(self, nome, cpf, data_nascimento):
        """ Cadastra paciente no consultório """
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                print(f"{paciente.nome} já está cadastrado.")
                return None
        paciente = Paciente(nome, cpf, data_nascimento)
        self.pacientes.append(paciente)
        print(f"Paciente cadastrado com sucesso.")
        return paciente
        
    def cadastrar_medico(self, nome, cpf, crm, especialidade):
        """ Cadastra médico no consultório """
        for medico in self.medicos:
            if medico.crm == crm:
                print(f"Médico já cadastrado.")
                return None
        medico = Medico(nome, crm, cpf, especialidade)
        self.medicos.append(medico)
        print("Médico cadastrado com sucesso.")
        return medico
        
    def adicionar_consulta(self, paciente_cpf, medico_crm, data, horario):
        """ Cadastra uma consulta """
        paciente_encontrado = None
        medico_encontrado = None
        
        for paciente in self.pacientes:
            if paciente.cpf == paciente_cpf:
                paciente_encontrado = paciente
                break
            
        if paciente_encontrado is None:
            print("Paciente não cadastrado.")
            return None
          
        for medico in self.medicos:
            if medico.crm == medico_crm:
                medico_encontrado = medico
                break
            
        if medico_encontrado is None:
            print("Médico não cadastrado.")
            return None
        
        if paciente_encontrado not in medico_encontrado.pacientes:
            medico_encontrado.pacientes.append(paciente_encontrado)
                
        consulta = Consulta(paciente_cpf, medico_crm, data, horario)
        self.consultas.append(consulta)
        print(f"Consulta de {paciente_encontrado.nome} cadastrada com sucesso.")
        print(consulta)
        return consulta
        
class Paciente:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.historico = []
        
class Consulta:
    def __init__(self, paciente_cpf, medico_crm, data, horario):
        self.paciente_cpf = paciente_cpf
        self.medico_crm = medico_crm
        self.data = data
        self.horario = horario
            
    def __str__(self):
        """ Formata objeto consulta para ser exibido na tela """
        return f"Consulta - CPF do Paciente: {self.paciente_cpf}, Médico CRM: {self.medico_crm}, Data: {self.data}, Horário: {self.horario}"
        
class Medico:
    def __init__(self, nome, crm, cpf, especialidade):
        self.nome = nome
        self.cpf = cpf
        self.crm = crm
        self.especialidade = especialidade
        self.pacientes = []
        
    def adicionar_prontuario(self, cpf_paciente):
        """ Adiciona prontuario de um paciente """
        for paciente in self.pacientes:
            if paciente.cpf == cpf_paciente:
                prontuario = Prontuario(paciente, self)
                return prontuario
        print("Paciente não encontrado.")
        return None
                
    def __str__(self):
        """ Formata objeto médico para ser exibido na tela """
        return f"Médico - Nome: {self.nome}, CRM: {self.crm}, Especialidade: {self.especialidade}"
        
class Prontuario:
    def __init__(self, paciente, medico):
        self.paciente = paciente
        self.medico = medico
        self.hipotese_diagnostica = ""
        self.diagnostico = ""
        self.exames = []
        self.consultas = []