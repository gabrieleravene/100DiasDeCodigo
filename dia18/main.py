# sistema de gestão de cinema

# O programa possui funcionalidade :
# 1 - Cadastrar usuário
# 2 - Cadastrar filme
# 3 - Cadastrar sessão
# 4 - Usuário comprar ingresso para filme

import sqlite3
from datetime import datetime

def criar_banco_de_dados():
    try:
        with sqlite3.connect("cinema.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                data_nascimento DATE) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS filmes (
                id_filme INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                isan TEXT,
                diretor TEXT,
                duracao INTEGER,
                data_lancamento DATE) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS compras (
                id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INT,
                id_filme INT,
                usuario TEXT,
                filme TEXT,
                quantidade INT,
                valor FLOAT,
                data DATE,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)
                ) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS sessao (
                id_sessao INTEGER PRIMARY KEY AUTOINCREMENT,
                id_filme INT,
                data DATE,
                hora TEXT,
                cadeiras INT,
                FOREIGN KEY (id_filme) REFERENCES filmes(id_filme)) """)        
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados: {erro}")
 
class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Filme:
    def __init__(self, titulo, isan, diretor, duracao, data_lancamento):
        self.titulo = titulo
        self.isan = isan
        self.diretor = diretor
        self.duracao = duracao
        self.data_lancamento = data_lancamento
        
class Compra:
    def __init__(self, usuario, filme, quantidade=None, total=None):
        self.usuario = usuario
        self.filme = filme
        self.quantidade = quantidade
        self.total = total
        
class Sessao:
    def __init__(self, filme, data, hora, cadeiras=100):
        self.filme = filme
        self.data = data
        self.hora = hora
        self.cadeiras = cadeiras
        
class Cinema:
    pass

    def cadastrar_usuario(self, nome, cpf, data_nascimento):
        try:
            with sqlite3.connect("cinema.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT * FROM usuarios WHERE cpf = ? ", (cpf,))
                usuario = cursor.fetchone()
                
                if usuario:
                    print("Usuário já cadastrado.")
                    return
                
                cursor.execute(" INSERT INTO usuarios (nome, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome, cpf, data_nascimento))
                
                conexao.commit()
                
                print("Usuário cadastrado com sucesso.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastra usuário: {erro}")
            
    def cadastrar_filme(self, titulo, isan, diretor, duracao, data_lancamento):
        try:
            with sqlite3.connect("cinema.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT * FROM filmes WHERE isan = ? ", (isan,))
                filme = cursor.fetchone()
                
                if filme:
                    print("Filme já cadastrado.")
                    return
                
            cursor.execute(" INSERT INTO filmes (titulo, isan, diretor, duracao, data_lancamento) VALUES (?, ?, ?, ?, ?) ", (titulo, isan, diretor, duracao, data_lancamento))
                
            conexao.commit()
                
            print("Filme cadastrado com sucesso.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar filme: {erro}")
            
    def comprar_ingresso(self, cpf, isan, quantidade, valor_unitario):
        try:
            with sqlite3.connect("cinema.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT id_usuario, nome FROM usuarios WHERE cpf = ? ", (cpf,))
                usuario = cursor.fetchone()
                
                if not usuario:
                    print("Usuário não possui cadastro.")
                    return
            
                id_usuario, nome_usuario = usuario
                
                cursor.execute(" SELECT id_filme, titulo FROM filmes WHERE isan = ? ", (isan,))
                filme = cursor.fetchone()
                
                if not filme:
                    print("Filme não disponível.")
                    return
                
                id_filme, titulo_filme = filme
                
                cursor.execute(" SELECT id_sessao, cadeiras FROM sessao WHERE id_filme = ? AND cadeiras >= ? ", (id_filme, quantidade))
                sessao = cursor.fetchone()
                
                if not sessao:
                    print("Não há sessões disponíveis com cadeiras suficientes.")
                    return
                
                id_sessao, cadeiras_disponveis = sessao
                
                total = quantidade * valor_unitario
                
                data_hoje = datetime.now().strftime("%Y-%m-%d")
                cursor.execute(" INSERT INTO compras (id_usuario, id_filme, usuario, filme, quantidade, valor, data)  VALUES (?, ?, ?, ?, ?, ?, ?)", (id_usuario, id_filme, nome_usuario, titulo_filme, quantidade, total, data_hoje))
                
                cadeiras_restantes = cadeiras_disponveis - quantidade
                cursor.execute("UPDATE sessao SET cadeiras = ? WHERE id_sessao =  ?", (cadeiras_restantes, id_sessao))
                
                conexao.commit()
                
                print(f"Ingressos comprados com sucesso. Total: R${total:.2f}")
                    
            
        except sqlite3.Error as erro:
            print(f"Erro ao realizar compra: {erro}")
            
    def cadastrar_sessao(self, id_filme, data, hora, cadeiras=100):
        try:
            with sqlite3.connect("cinema.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT * FROM sessao WHERE id_filme = ? AND data = ? AND hora = ? ", (id_filme, data, hora))
                sessao = cursor.fetchone()
                
                if sessao:
                    print("Sessão já cadastrada.")
                    return
                
                cursor.execute(" INSERT INTO sessao (id_filme, data, hora, cadeiras) VALUES (?, ?, ?, ?) ", (id_filme, data, hora, cadeiras))
                
                conexao.commit()
                
                print("Sessão cadastrada com sucesso.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar sessão: {erro}")

if __name__ == "__main__":
    criar_banco_de_dados()
    cinema = Cinema()
    
    while True:
        print(""" Sistema de gestão de cinema:
              1 - Cadastrar usuário
              2 - Cadastrar filme
              3 - Comprar ingresso
              4 - Cadastrar sessão
              5 - Encerrar programa """)
        
        opcao = input("Opção desejada: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            
            cinema.cadastrar_usuario(nome, cpf, data_nascimento)
            
        elif opcao == '2':
            try:
               titulo = input("Título: ")
               isan = input("ISAN: ")
               diretor = input("Diretor: ")
               duracao = int(input('Duração (total em minutos): '))
               data_lancamento = input("Data de lançamento: ")
            
               cinema.cadastrar_filme(titulo, isan, diretor, duracao, data_lancamento)
               
            except ValueError:
                print("Digite um valor numérico no campo de duração.")
            
        elif opcao == '3':
            try:
               cpf = input("Digite o CPF: ")
               isan = input("Digite o ISAN: ")
               quantidade = int(input("Digite a quantidade: "))
               valor_unitario = float(input("Digite o valor unitário: ")) 
               
               cinema.comprar_ingresso(cpf, isan, quantidade, valor_unitario)
               
            except ValueError:
                print("Digite valor numérico válido.")
                
        elif opcao == '4':
            try:
               id_filme = int(input("ID do filme: "))
               data = input("Data: ")
               hora = input("Hora: ")
               
               cinema.cadastrar_sessao(id_filme, data, hora)
               
            except ValueError:
                print("id_filme só aceita valores numéricos. Digite um valor válido.")
            
        elif opcao == '5':
            print("Encerrando programa...")
            break
            
        else:
            print("Opção inválida.")