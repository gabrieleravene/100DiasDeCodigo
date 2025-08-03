# sistema de gestão biblioteca

# o sistema possui as funcionalidades:
# 1 - cadastrar um livro 
# 2- cadastrar leitor
# 3 - emprestar livro
# 4 - devolver livro

import sqlite3
from datetime import datetime

def criar_banco_de_dados():
    try:
        with sqlite3.connect("biblioteca.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS livros (
                id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                ano DATE,
                quantidade INT,
                isbn TEXT) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS leitores (
                id_leitor INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                data_nascimento DATE
                ) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS emprestimos (
                id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_leitor INTEGER,
                id_livro INTEGER,
                livro_titulo TEXT,
                livro_isbn TEXT,
                quantidade INT,
                data_emprestimo DATE,
                data_devolucao DATE,
                FOREIGN KEY (id_leitor) REFERENCES leitores(id_leitor),
                FOREIGN KEY (id_livro REFERENCES livros(id_livro)) """)
            
            conexao.commit()
            print("Banco de dados criado com sucesso.")
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados:  {erro}")
        
class Biblioteca:
    pass

    def cadastrar_livro(self, titulo, autor, ano, isbn, quantidade=None):
        try:
            with sqlite3.connect("biblioteca.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute (" SELECT * from livros (titulo, autor, ano isbn, quantidade) WHERE isbn = ? ", (isbn,))
                livro_procurado = cursor.fetchone()
                
                if livro_procurado:
                    print("Livro já cadastrado!")
                else:
                    cursor.execute(" INSERT INTO livros (titulo, autor, ano, isbn, quantidade) VALUES (?, ?, ?, ?, ?) ", (titulo, autor, isbn, quantidade))
                    
                    conexao.commmit()
                    
                    print("Livro cadastrado com sucesso!")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar livro: {erro}")
            
    def cadastrar_leitor(self, nome, cpf, data_nascimento):
            try:
                with sqlite3.connect("biblioteca.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute(" SELECT * FROM leitores (nome, cpf, data_nascimento) WHERE cpf = ?", (cpf,))
                    cpf_procurado = cursor.fetchone()
                    
                    if cpf_procurado:
                        print("Usuário já cadastrado.")
                        
                    else:
                        cursor.execute(" INSERT INTO leitores (nome, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome, cpf, data_nascimento))
                        
                        conexao.commit()
                        
                        print("Usuário cadastrado com sucesso!")
                
            except sqlite3.Error as erro:
                print(f"Erro ao cadastrar usuário: {erro}")

class Livro:
    def __init__(self, titulo, autor, ano, isbn, quantidade=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.quantidade = quantidade
        self.isbn = isbn # número único que identifica cada livro
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Quantidade: {self.quantidade}"
    
class Leitor:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
if __name__ == "__main__":
    criar_banco_de_dados()
    
    while True:
        print("""SISTEMA DE GESTÃO LABORATORIAL
              1 - Cadastrar livro
              2 - Cadastrar leitor
              3 - Emprestar livro
              4 - Devolver livro
              5 - Encerrar programa
              """)