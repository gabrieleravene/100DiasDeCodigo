# sistema de gestão laboratorial

# O programa possui as funcionalidades de:
# 1 - Cadastrar paciente
# 2 - Cadastrar exame
# 3 - Cadastrar analista
# 4 - adicionar laudo
# 5 - Exibir lista de pacientes
# 6 - Exibir lista de analistas
# 7 - Exibir lista de exames

from datetime import datetime

class Laboratorio:
    def __init__(self):
        self.exames = []
        self.pacientes = []
        self.analistas = []
        
    def cadastrar_analista(self, nome, cpf, data_nascimento, registro):
        for analista in self.analistas:
            if analista.cpf == cpf:
                print("Analista já cadastrado.")
                return None
            
        novo_analista = Analista(nome, cpf, data_nascimento, registro)
        self.analistas.append(novo_analista)
        print(f"Cadastro de {novo_analista.nome} realizado com sucesso. \n"
              f"{novo_analista}")
        return novo_analista
    
    def cadastrar_paciente(self, nome, cpf, data_nascimento):
        for paciente in self.pacientes:
            if paciente.cpf == cpf:
                print("Paciente já cadastrado.")
                return None
        
        prontuario = len(self.pacientes) + 1    
        novo_cadastro = Paciente(nome, cpf, data_nascimento, prontuario)
        self.pacientes.append(novo_cadastro)
        print(f"Cadastro de {novo_cadastro.nome} realizado com sucesso! \n"
              f"{novo_cadastro}")
        return novo_cadastro
    
    def cadastrar_exame(self, nome, paciente, data_str):
        data = datetime.strptime(data_str, "%d/%m/%Y")
        solicitacao = len(self.exames) + 1
        novo_exame = Exame(nome, paciente, data, solicitacao)
        self.exames.append(novo_exame)
        print("Exame cadastrado com sucesso!"
              f"{novo_exame}")
        
    def adicionar_laudo(self, solicitacao):
        for exame in self.exames:
            if exame.solicitacao == solicitacao:
                if exame.laudo and exame.assinatura:
                    print("Este exame já foi assinado.")
                    return
                exame.laudo = input("Resultado: ")
                exame.assinatura = input("Assinatura: ")
                print("Exame assinado com sucesso.")
                return
        print("Solicitação não encontrada.")
        
    def exibir_pacientes(self):
        for paciente in self.pacientes:
            print(paciente)
            
    def exibir_analistas(self):
        for analista in self.analistas:
            print(analista)
            
    def exibir_exames(self):
        for exame in self.exames:
            print(exame)
            
class Analista:
    def __init__(self, nome, cpf, data_nascimento, registro):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.registro = registro
        
    def __str__(self):
        return (
            f"Nome: {self.nome} \n" 
            f"CPF: {self.cpf} \n" 
            f"Data de nascimento: {self.data_nascimento} \n" 
            f"Registro: {self.registro}"
        )
class Paciente:
    def __init__(self, nome, cpf, data_nascimento, prontuario=None):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.prontuario = prontuario
        
    def __str__(self):
        return (
            f"Nome: {self.nome} \n" 
            f"CPF: {self.cpf} \n" 
            f"Data de nascimento: {self.data_nascimento} \n"
            f"Prontuário: {self.prontuario}"
        )
    
class Exame:
    def __init__(self, nome, paciente, data=None, solicitacao=None, assinatura=None):
        self.nome = nome
        self.paciente = paciente
        self.data = data
        self.solicitacao = solicitacao
        self.laudo = ""
        self.assinatura = assinatura
        
    def __str__(self):
        texto = (
            f"Nome: {self.nome} \n" 
            f"Paciente: {self.paciente.nome} (Prontuário: {self.paciente.prontuario}) \n" 
            f"Data: {self.data.strftime('%d/%m/%Y') if self.data else 'Não informada'} \n" 
            f"Laudo: {self.laudo}"
            )
        if self.laudo and self.assinatura:
            texto += (f"Laudo: {self.laudo} \n"
                     f"Assinado por: {self.assinatura}")
        return texto
            
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
            cpf = input("CPF do paciente: ")
            data = input("Data: (formato DD/MM/AAAA)")
            
            paciente_obj = None
            for paciente in laboratorio.pacientes:
                if paciente.cpf == cpf:
                    paciente_obj = paciente
                    break
            
            if paciente_obj:
               laboratorio.cadastrar_exame(nome, paciente_obj, data)
            else:
                print("Paciente não encontrado.")
                
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