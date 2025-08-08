# sistema de gestão de cinema - integrando as classes

# O sistema possui as funcionalidades de:
# 1 - Cadastrar um usuário
# 2 - Cadastrar um filme
# 3 - Cadastrar uma sessão
# 4 - Usuário comprar ingresso

import sqlite3
from datetime import datetime

def criar_banco_de_dados():
    try:
        with sqlite3.connect("cine.db") as conexao:
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
                id_sessao INT,
                cpf TEXT,
                isan TEXT,
                quantidade INT,
                valor_unitario FLOAT,
                valor_total FLOAT,
                data DATE,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                FOREIGN KEY (id_filme) REFERENCES filmes(id_filme),
                FOREIGN KEY (id_sessao) REFERENCES sessao(id_sessao)
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
    def __init__(self, cpf, isan, data, quantidade=None, valor_unitario=None, valor_total=None):
        self.cpf = cpf
        self.isan = isan
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total
        self.data = data
        
class Sessao:
    def __init__(self, id_sessao, id_filme, data, hora, cadeiras=100):
        self.id_sessao = id_sessao
        self.id_filme = id_filme
        self.data = data
        self.hora = hora
        self.cadeiras = cadeiras
        
class Cinema:
    pass

    def cadastrar_usuario(self, nome, cpf, data_nascimento):
        try:
            cpf_limpo = ''.join(filter(str.isdigit, cpf))
            
            with sqlite3.connect("cine.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT id_usuario, nome, cpf, data_nascimento FROM usuarios WHERE cpf = ? ", (cpf,))
                dados = cursor.fetchone()
                
                if dados:
                    print("Usuário já cadastrado.")
                    return
                
                cursor.execute(" INSERT INTO usuarios (nome, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome, cpf_limpo, data_nascimento))
                
                conexao.commit()
                
                print("Usuário cadastrado com sucesso.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar usuário: {erro}")
            
    def cadastrar_filme(self, titulo, isan, diretor, duracao, data_lancamento):
        try:
            with sqlite3.connect("cine.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT id_filme, titulo, diretor, duracao, data_lancamento FROM filmes WHERE isan = ? ", (isan,))
                dados = cursor.fetchone()
                
                if dados:
                    print("Filme já cadastrado.")
                    return
                    
                cursor.execute(" INSERT INTO filmes (titulo, isan, diretor, duracao, data_lancamento) VALUES (?, ?, ?, ?, ?) ", (titulo, isan, diretor, duracao, data_lancamento))
                
                id_filme = cursor.lastrowid
                
                conexao.commit()
                
                print(f"Filme cadastrado com sucesso: {id_filme}")
                    
        except sqlite3.Error as erro:
            print(f"Erro ao cadastar filme: {erro}")
                
    def cadastrar_sessao(self, id_filme, data, hora, cadeiras=100):
            try:
                with sqlite3.connect("cine.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute("SELECT * FROM sessao WHERE id_filme = ? AND data = ? AND hora = ?", (id_filme, data, hora))
                    sessao = cursor.fetchone()
                    
                    if sessao:
                       print("Sessão já cadastrada.")
                       return
                   
                    cursor.execute(" INSERT INTO sessao (id_filme, data, hora, cadeiras) VALUES (?, ?, ?, ?) ", (id_filme, data, hora, cadeiras))
                    
                    id_sessao = cursor.lastrowid
                    
                    conexao.commit()
                    
                    print(f"Sessão cadastrada com sucesso: {id_sessao}")
                
            except sqlite3.Error as erro:
                print(f"Erro ao cadastrar sessão: {erro}")
                
    def comprar_ingresso(self, cpf, id_sessao, isan, quantidade, valor_unitario):
        try:
            with sqlite3.connect("cine.db") as conexao:
                cursor = conexao.cursor()
                
                # verificar se usuário possui cadastro
                
                cpf_limpo = ''.join(filter(str.isdigit, cpf))
                
                cursor.execute(" SELECT * FROM usuarios WHERE cpf = ? ", (cpf_limpo,))
                usuario = cursor.fetchone()
                
                if not usuario:
                    print("Usuário não cadastrado.")
                    return
                
                id_usuario = usuario[0]
                
                # verifica se filme esta cadastrado no sistema
                
                cursor.execute(" SELECT id_filme, titulo, diretor, duracao, data_lancamento FROM filmes where isan = ? ", (isan,))
                filme_dados = cursor.fetchone()
                
                if not filme_dados:
                    print("Filme não cadastrado.")
                    return
                    
                id_filme = filme_dados[0]
                
                # verifica se sessão esta cadastrada
                
                cursor.execute(" SELECT id_filme, cadeiras FROM sessao WHERE id_sessao = ?", (id_sessao,))
                dados_sessao = cursor.fetchone()
                
                if not dados_sessao:
                    print("Sessão não encontrada.")
                    return
                
                id_filme_sessao, cadeiras_disponiveis = dados_sessao
                
                # verifica se a sessão pertence ao filme informado
                
                if id_filme_sessao != id_filme:
                    print("A sessao não pertence ao filme informado.")
                    return
                
                # verifica se há cadeiras disponíveis na sessão
                
                if cadeiras_disponiveis < quantidade:
                    print("Sessão sem cadeiras disponíveis.")
                    return
                
                valor_total = quantidade * valor_unitario
                
                data = datetime.now().strftime("%Y-%m-%d")
                
                cursor.execute(" INSERT INTO compras (id_usuario, id_filme, id_sessao, cpf, isan, quantidade, valor_unitario, valor_total, data) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (id_usuario, id_filme, id_sessao, cpf, isan, quantidade, valor_unitario, valor_total, data))
                
                atualizar_sessao = cadeiras_disponiveis - quantidade
                cursor.execute(" UPDATE sessao SET cadeiras = ? WHERE id_sessao = ? ", (atualizar_sessao, id_sessao))
                
                conexao.commit()
                
                print(f"Compra realizada com sucesso. Total: {valor_total:.2f}")
        
        except sqlite3.Error as erro:
            print(f"Erro ao comprar ingresso: {erro}")
            
if __name__ == "__main__":
    criar_banco_de_dados()
    cinema = Cinema()
    
    while True:
        print(""" Sistema de gestão de cinema:
              1 - Cadastrar usuário
              2 - Cadastrar filme
              3 - Cadastrar sessão
              4 - Comprar ingresso
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
               id_filme = int(input("ID do filme: "))
               data = input("Data: ")
               hora = input("Hora: ")
               
               cinema.cadastrar_sessao(id_filme, data, hora)
               
            except ValueError:
                print("id_filme só aceita valores numéricos. Digite um valor válido.")
                
        elif opcao == '4':
            try:
                cpf = input("CPF do usuário: ")
                isan = input("ISAN do filme: ")
                id_sessao = int(input("ID da sessão: "))
                quantidade = int(input("Quantidade de de ingressos: "))
                valor_unitario = float(input("Valor unitário: "))
                
                cinema.comprar_ingresso(cpf, id_sessao, isan, quantidade, valor_unitario)
                
            except ValueError:
                print("Valor inválido.")
            
        elif opcao == '5':
            print("Encerrando programa...")
            break
            
        else:
            print("Opção inválida.")