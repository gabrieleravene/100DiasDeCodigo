# sistema de gestão escolar

class Aluno:
    def __init__(self, nome, cpf, ra):
        self.nome = nome
        self.cpf = cpf
        self.ra = ra
        self.boletim = []
        self.historico = []
        
class Professor:
    def __init__(self, nome, cpf, disciplina):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self.salas = []
        
class Sala:
    def __init__(self, serie, identificador):
        self.serie = serie
        self.identificador = identificador
        self.alunos = []