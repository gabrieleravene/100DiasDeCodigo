# sistema de gestão de insumos laboratorias com banco de dados

# O programa possui as funcionalidades de:
# 1 - Cadastrar produto
# 2 - Cadastrar analista para gerenciar insumos
# 2 - Dar baixa em produto

import sqlite3
from datetime import datetime

def criar_banco_de_dados():
    try:
        with sqlite3.connect("insumoslaboratoriais.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS insumos (
                id_insumo INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT,
                tipo TEXT,
                lote TEXT,
                data_fabricacao DATE,
                data_validade DATE,
                quantidade INT
            )
            """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS analistas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                cpf TEXT,
                data_nasciment DATE,
                registro TEXT) """)
            
            conexao.commit()
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados: {erro}.")
        
class Laboratorio:
    pass

    def cadastrar_analista(self, nome, cpf, data_nasciment, registro):
        """ Cadastra analista para gerenciar insumos """
        try:
            with sqlite3.connect("insumoslaboratoriais.db") as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    " INSERT INTO analistas (nome, cpf, data_nasciment, registro) VALUES (?, ?, ?, ?)", (nome, cpf, data_nasciment, registro)
                )
                conexao.commit()
                print("Analista cadastrado com sucesso.")
                return True
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar analista: {erro}.")
            return False
        
    def cadastrar_insumos(self, produto, tipo, lote, data_fabricacao, data_validade, quantidade):
        """ Cadastra insumo no estoque """
        try:
            with sqlite3.connect("insumoslaboratoriais.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" INSERT INTO insumos (produto, tipo, lote, data_fabricacao, data_validade, quantidade) VALUES (?, ?, ?, ?, ?, ?) ", (produto, tipo, lote, data_fabricacao, data_validade, quantidade))
                
                print("Insumo cadastrado com sucesso.")
                
                conexao.commit()
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar insumo: {erro}")
            
    def baixar_insumo(self, id_insumo, qtde):
        """ Realiza baixa em produto no estoque """
        try:
            with sqlite3.connect("insumoslaboratoriais.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(" SELECT * FROM insumos WHERE id_insumo = ? ", (id_insumo,))
                insumo_procurado = cursor.fetchone()
                
                if insumo_procurado:
                    print(insumo_procurado)
                    
                    prosseguir = input("Prosseguir? (s/n)")
                    
                    if prosseguir == 's':
                       cursor.execute(" UPDATE insumos SET quantidade = ? WHERE id_insumo = ? ", (qtde, id_insumo))
                       print("Alteração realizada com sucesso.")
                       conexao.commit()
                    else:
                        print("Operação cancelada.")
                    
                else:
                    print("Insumo não encontrado.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao dar baixa em insumo: {erro}")
        
class Analista:
    def __init__(self, nome, cpf, data_nascimento, registro):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.registro = registro
        
class Insumo:
    def __init__(self, produto, tipo, lote, data_fabricacao, data_validade, quantidade):
        self.produto = produto
        self.tipo = tipo
        self.lote = lote
        self.data_fabricacao = data_fabricacao
        self.data_validade = data_validade
        self.quantidade = quantidade
        
    def __str__(self):
        return f"Produtto: {self.produto}, Tipo: {self.tipo}, Lote: {self.lote}, Data de fabricação: {self.data_fabricacao}, Data de validade: {self.data_validade}, Quantidade: {self.quantidade}"
        
if __name__ == "__main__":
    criar_banco_de_dados()
    laboratorio = Laboratorio()
    
    while True:
        print(""" SISTEMA DE GESTÃO DE INSUMOS LABORATORIAIS
              ================== MENU ====================== 
              1 - Cadastrar insumo
              2 - Cadastrar analista
              3 - Dar baixa em insumo 
              4 - Encerrar programa """)
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            produto = input("Produto: ")
            tipo = input("Tipo: ")
            lote = input("Lote: ")
            data_fabricacao = input("Data de fabricação (formato AAAA-MM-DD): ")
            data_validade = input("Data de validade (AAAA-MM-DD): ")
            quantidade = int(input("Quantidade: "))
            laboratorio.cadastrar_insumos(produto, tipo, lote, data_fabricacao, data_validade, quantidade)
            
        elif opcao == '2':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nasciment = input("Data nascimento (no formato AAAA-MM-DD): ")
            registro = input("Registro: ")
            laboratorio.cadastrar_analista(nome, cpf, data_nasciment, registro)
            
        elif opcao == "3":
            try:
               id_insumo = int(input("Digite o ID do produto: "))
               qtde = int(input("Digite quantidade a ser baixa: "))
               laboratorio.baixar_insumo(id_insumo, qtde)
            except ValueError:
                print("Valor inválido.")
                
        elif opcao == "4":
            print("Encerrando programa...")
            break
            
        else:
            print("Opção inválida.")