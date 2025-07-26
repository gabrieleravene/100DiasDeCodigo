# sistema de gestão escolar

# O programa possui as funcionalidades:
# Criar uma turma
# Cadastrar aluno
# Cadastrar professor

class Escola:
    def __init__(self):
        self.alunos = []
        self.turmas = []
        self.professores = []
        
    def criar_sala(self, serie, identificador):
        for turma in self.turmas:
            if turma.serie == serie and turma.identificador == identificador:
                print("Essa turma já existe!")
                
        nova_turma = Turma(serie, identificador)
        self.turmas.append(nova_turma)
        return nova_turma
        
    def matricular_aluno(self, nome, cpf, data_nascimento):
        for aluno in self.alunos:
            if aluno.cpf == cpf:
                print("Aluno já está matriculado.")
                return None
            
        novo_aluno = Aluno(nome, cpf, data_nascimento)
        self.alunos.append(novo_aluno)
        print(f"Novo aluno cadastrado com sucesso!")
        print(novo_aluno)
        return novo_aluno
    
    def cadastrar_professor(self, nome, cpf, data_nascimento, disciplina):
        for professor in self.professores:
            if professor.cpf == cpf:
                print("Professor já cadastrado.")
                return None
        
        novo_professor = Professor(nome, cpf, data_nascimento, disciplina)
        self.professores.append(novo_professor)
        print("Novo professor cadastrado com sucesso!")
        print(novo_professor)
        return novo_professor

class Aluno:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.boletim = []
        self.historico = []
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}"
        
class Professor:
    def __init__(self, nome, cpf, data_nascimento, disciplina):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.disciplina = disciplina
        self.salas = []
        
    def __str__(self):
        return f"Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Disciplina: {self.disciplina}"    
        
class Turma:
    def __init__(self, serie, identificador):
        self.serie = serie
        self.identificador = identificador
        self.alunos = []
        
if __name__ == "__main__":
    escola = Escola()
    
    while True:
        print(""" SISTEMA DE GESTÃO ESCOLAR
          1 - Criar turma
          2 - Cadastar aluno
          3 - Cadastrar professor
          4 - Encerrar programa
          """)
    
        opcao = input("Digite a opção desejada: ")
    
        if opcao == '1':
            serie = input("Série: ")
            identificador = input("Identificador: ")
            escola.criar_sala(serie, identificador)
        
        elif opcao == '2':
            nome = input("Nome do aluno: ")
            cpf = input("CPF do aluno: ")
            data_nascimento = input("Data de nascimento: ")
            escola.matricular_aluno(nome, cpf, data_nascimento)
        
        elif opcao == '3':
            nome = input("Nome do professor: ")
            cpf = input("CPF do professor: ")
            data_nascimento = input("Data de nascimento: ")
            disciplina = input("Disciplina: ")
            escola.cadastrar_professor(nome, cpf, data_nascimento, disciplina)
        
        elif opcao == '4':
            print("Encerrando programa...")
            break
        
        else:
            print("Opção inválida.")