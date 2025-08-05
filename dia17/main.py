# sistema de gestão biblioteca

# o sistema possui as funcionalidades:
# 1 - cadastrar um livro 
# 2- cadastrar leitor
# 3 - emprestar livro

import sqlite3
from datetime import datetime, timedelta

def criar_banco_de_dados():
    try:
        with sqlite3.connect("biblio.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS livros (
                id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT,
                autor TEXT,
                ano DATE,
                isbn TEXT,
                quantidade INT
                ) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS leitores (
                id_leitor INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                data_nascimento DATE
                ) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS emprestimos (
                id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo_livro,
                nome_leitor,
                id_livro INT,
                id_leitor INT, 
                data_emprestimo DATE,
                data_devolucao DATE,
                quantidade INT,
                FOREIGN KEY (id_leitor) REFERENCES leitores(id_leitor),
                FOREIGN KEY (id_livro) REFERENCES livros(id_livro)) """)
            
            conexao.commit()
            
            print("Banco de dados criado com sucesso.")
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados:  {erro}")
        
class Biblioteca:
    pass

    def cadastrar_livro(self, titulo, autor, ano, isbn, quantidade=None):
        try:
            with sqlite3.connect("biblio.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute (" SELECT * from livros WHERE isbn = ? ", (isbn,))
                livro_procurado = cursor.fetchone()
                
                if livro_procurado:
                    print("Livro já cadastrado!")
                else:
                    cursor.execute(" INSERT INTO livros (titulo, autor, ano, isbn, quantidade) VALUES (?, ?, ?, ?, ?) ", (titulo, autor, ano, isbn, quantidade))
                    
                    conexao.commit()
                    
                    print("Livro cadastrado com sucesso!")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar livro: {erro}")
            
    def cadastrar_leitor(self, nome, cpf, data_nascimento):
            try:
                with sqlite3.connect("biblio.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute(" SELECT * FROM leitores WHERE cpf = ?", (cpf,))
                    cpf_procurado = cursor.fetchone()
                    
                    if cpf_procurado:
                        print("Usuário já cadastrado.")
                        
                    else:
                        cursor.execute(" INSERT INTO leitores (nome, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome, cpf, data_nascimento))
                        
                        conexao.commit()
                        
                        print("Usuário cadastrado com sucesso!")
                
            except sqlite3.Error as erro:
                print(f"Erro ao cadastrar usuário: {erro}")
                
    def emprestar_livro(self, cpf, isbn, titulo_livro, nome_leitor, quantidade):
        try:
            with sqlite3.connect("biblio.db") as conexao:
                cursor = conexao.cursor()
                
                data_emprestimo = datetime.now().date().isoformat()
                
                data_devolucao = (datetime.now().date() + timedelta(days=7)).isoformat()
                
                cursor.execute(" SELECT * FROM leitores WHERE cpf = ? ", (cpf,))
                leitor = cursor.fetchone()
                if leitor:
                    id_leitor = leitor[0]
                    cursor.execute(" SELECT * FROM livros WHERE isbn = ? ", (isbn,))
                    livro = cursor.fetchone()
                    if livro:
                        id_livro = livro[0]
                        quantidade_disponivel = livro[5]
                        
                        if quantidade_disponivel < quantidade:
                            print(f"Quantidade insuficiente! Disponível: {quantidade_disponivel}")
                            return
                        
                        cursor.execute(" INSERT INTO emprestimos (titulo_livro, nome_leitor, id_livro, id_leitor, data_emprestimo, data_devolucao, quantidade) VALUES (?, ?, ?, ?, ?, ?, ?)", (titulo_livro, nome_leitor, id_livro, id_leitor, data_emprestimo, data_devolucao, quantidade))
                        
                        nova_quantidade = quantidade_disponivel - quantidade
                        cursor.execute(" UPDATE livros SET quantidade = ? WHERE isbn = ? ", (nova_quantidade, isbn))
                        
                        conexao.commit()
                        
                        print("Empréstimo realizado com sucesso.")
                        
                    else:
                        print("Livro não encontrado.")
                        return
                else:
                    print("Usuário não cadastrado.")
                    return
                        
        except sqlite3.Error as erro:
            print(f"Erro ao criar banco de dados: {erro}")

class Livro:
    def __init__(self, titulo, autor, ano, isbn, quantidade=None):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.isbn = isbn # número único que identifica cada livro
        self.quantidade = quantidade
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Quantidade: {self.quantidade}"
    
class Leitor:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
class Emprestimo:
    def __init__(self, titulo_livro, nome_leitor, data_emprestimo, data_devolucao, quantidade=None):
        self.titulo_livro = titulo_livro
        self.nome_leitor = nome_leitor
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.quantidade = quantidade
        
        
if __name__ == "__main__":
    criar_banco_de_dados()
    biblioteca = Biblioteca()
    
    while True:
        print("""SISTEMA DE GESTÃO LABORATORIAL
              1 - Cadastrar livro
              2 - Cadastrar leitor
              3 - Emprestar livro
              4 - Encerrar programa
              """)
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            try:
               titulo = input("Título do livro: ")
               autor = input("Autor: ")
               ano = input("Ano: ")
               isbn = input("ISBN: ")
               quantidade = int(input("Quantidade: "))
               biblioteca.cadastrar_livro(titulo, autor, ano, isbn, quantidade)
            except ValueError:
                print("Valor inválido. Digite um valor de quantidade numérica válida.")
                
        elif opcao == '2':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            biblioteca.cadastrar_leitor(nome, cpf, data_nascimento)
            
        elif opcao == '3':
            try:
               cpf = input("CPF do leitor: ")
               isbn = input("ISBN do livro: ")
               titulo_livro = input("Título do livro: ")
               nome_leitor = input("Nome do leitor: ")
               quantidade = int(input("Quantidade: "))

               biblioteca.emprestar_livro(
                   cpf=cpf,
                   isbn=isbn,
                   titulo_livro=titulo_livro,
                   nome_leitor=nome_leitor,
                   quantidade=quantidade)
               
            except ValueError:
                print("Valor de quantidade inválido. Digite um valor numérico válido.") 
            
        elif opcao == '4':
            print("Encerrando programa...")
            break
        
        else:
            print("Opção inválida.")