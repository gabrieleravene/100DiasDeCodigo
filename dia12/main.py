# sistema de gestão laboratorial com banco de dados

# O programa possui as funcionalidades de:
# 1 - Cadastrar paciente
# 2 - Cadastrar exame

from datetime import datetime
import sqlite3

def criar_banco_de_dados():
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    
    cursor.execute("""  
        CREATE TABLE IF NOT EXISTS pacientes (
            nome_paciente TEXT,
            cpf_paciente TEXT, 
            data_nascimento TEXT,
            prontuario INTEGER PRIMARY KEY AUTOINCREMENT
        )
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS analistas (
            nome_analista TEXT,
            cpf_analista TEXT,
            data_nascimento TEXT,
            registro TEXT,
            id_analista INTEGER PRIMARY KEY AUTOINCREMENT
        )
    """)
    
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS exames (
            nome_exame TEXT,
            prontuario_paciente TEXT,
            data TEXT,
            laudo TEXT,
            assinatura TEXT,
            solicitacao INTEGER PRIMARY KEY AUTOINCREMENT,
            FOREIGN KEY (prontuario_paciente) REFERENCES pacientes (prontuario)
        ) 
    """)
    
    conexao.commit()
    conexao.close()
    
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
            texto += (
                f"\nAssinado por: {self.assinatura}"
            )
        return texto

class Laboratorio:
    def __init__(self):
        self.exames = []
        self.pacientes = []
        self.analistas = []

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

def cadastrar_paciente(nome, cpf, data_nascimento):
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    cursor.execute(""" 
        INSERT INTO pacientes (nome_paciente, cpf_paciente, data_nascimento)
        VALUES (?, ?, ?)""",
        (nome, cpf, data_nascimento))
    conexao.commit()
    conexao.close()
    print("Paciente cadastrado com sucesso.")
        
def obter_prontuario_por_cpf(cpf):
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT prontuario FROM pacientes WHERE cpf_paciente = ?", (cpf,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado[0] if resultado else None
        
def cadastrar_exame(nome_exame, cpf_paciente, data):
    prontuario = obter_prontuario_por_cpf(cpf_paciente)
    if prontuario is None:
        print("Paciente não encontrado.")
        return
    conexao = sqlite3.connect("pacientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        INSERT INTO exames (nome_exame, prontuario_paciente, data, laudo, assinatura) 
        VALUES (?, ?, ?, '', '')""", 
        (nome_exame, prontuario, data))
    conexao.commit()
    conexao.close()
    print("Exame cadastrado com sucesso.")        

# Programa principal
if __name__ == "__main__":
    
    criar_banco_de_dados()
    laboratorio = Laboratorio()
    
    while True:
        print("""\nSISTEMA DE GESTÃO LABORATORIAL:
              1 - Cadastrar paciente
              2 - Cadastrar exame
              3 - Encerrar programa
              """)
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            cadastrar_paciente(nome, cpf, data_nascimento)
            
        elif opcao == "2":
            nome_exame = input("Exame: ")
            cpf = input("CPF do paciente: ")
            data = input("Data (formato DD/MM/AAAA): ").strip()
            cadastrar_exame(nome_exame, cpf, data)
            
        elif opcao == '3':
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.")