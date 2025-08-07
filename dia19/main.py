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
                usuario TEXT,
                filme TEXT,
                quantidade INT,
                valor FLOAT,
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
        
    def exibir_dados(self):
        print(f"{self.nome} - CPF: {self.cpf} - Data de nascimento: {self.data_nascimento}")

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
            with sqlite3.connect("cine.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT id_usuario, nome, cpf, data_nascimeto FROM usuarios WHERE cpf = ? ", (cpf,))
                dados = cursor.fetchone()
                
                if dados:
                    print("Usuário já cadastrado.")
                    return
                
                cursor.execute(" INSERT INTO usuarios (nome, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome, cpf, data_nascimento))
                
                conexao.commmit()
                
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
                    
                cursor.execute(" INSERT INTO filmes (titulo, diretor, duracao, data_lancamento) VALUES (?, ?, ?, ?, ?) ", (titulo, isan, diretor, duracao, data_lancamento))
                
                conexao.commit()
                
                print(f"Filme cadastrado com sucesso!")
                    
        except sqlite3.Error as erro:
            print(f"Erro ao cadastar filme: {erro}")
                
    def cadastrar_sessao(self, id_filme, data, hora, cadeiras=100):
            try:
                with sqlite3.connect("cine.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute(" SELECT * FROM sessao WHERE id_filme = ? AND data = ? AND hora = ?)", (id_filme, data, hora))
                    sessao = cursor.fetchone()
                    
                    if sessao:
                       print("Sessão já cadastrada.")
                       return
                   
                    cursor.execute(" INSERT INTO sessao (id_filme, data, hora, cadeiras) VALUES (?, ?, ?, ?) ", (id_filme, data, hora, cadeiras))
                    
                    conexao.commit()
                    
                    print("Sessão cadastrada com sucesso!")
                
            except sqlite3.Error as erro:
                print(f"Erro ao cadastrar sessão: {erro}")
                
    def comprar_ingresso(self, usuario, filme, quantidade, valor, data):
        try:
            with sqlite3.connect("cine.db") as conexao:
                cursor = conexao.cursor()
                
                # verificar se ha cadeiras disponíves em sessão desejada
                cursor.execute("  ")
        
        except sqlite3.Error as erro:
            print(f"Erro ao comprar ingresso: {erro}")