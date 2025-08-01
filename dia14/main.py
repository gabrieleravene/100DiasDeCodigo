# sistema de gestão de insumos laboratorias com banco de dados

# O programa possui as funcionalidades de:
# 1 - Cadastrar produto
# 2 - Dar baixa em produto

from datetime import datetime
import sqlite3

def criar_banco_de_dados():
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS insumos (
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
                produto TEXT,
                tipo TEXT,
                lote TEXT,
                data_fabricacao DATE,
                data_validade DATE,
                quantidade INT) """)
            
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados: {erro}.")
        
class Laboratorio:
    def __init__(self):
        self.analistas = []
        self.insumos = []
        
class Insumo:
    def __init__(self, produto, tipo, lote, data_fabricacao, data_validade, quantidade):
        self.produto = produto
        self.tipo = tipo
        self.lote = lote
        self.data_fabricacao = data_fabricacao
        self.data_validade = data_validade
        self.quantidade = quantidade
        
def cadastrar_insumo(produto, tipo, lote, data_fabricacao, data_validade, quantidade):
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute("""INSERT INTO insumos (produto, tipo, lote, data_fabricacao, data_validade, quantidade) VALUES (?, ?, ?, ?, ?, ?)""", (produto, tipo, lote, data_fabricacao, data_validade, quantidade))
            
            print("Produto cadastrado com sucesso.")
            
            conexao.commit()
        
    except sqlite3.Error as erro:
        print(f"Erro ao cadastrar insumo: {erro}.")
        
def baixar_insumo(id_produto, qtde):
    try:
        with sqlite3.connect("insumos.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" SELECT * FROM insumos WHERE id_produto = ? """, (id_produto,))
            insumo_procurado = cursor.fetchone()
            if insumo_procurado:
                cursor.execute(""" UPDATE insumos SET quantidade = ? WHERE id_produto = ? """, (qtde, id_produto))
                print("Dados alterados com sucesso.")
            else:
                print("Insumo não encontrado.")
            
        conexao.commit()
        
    except sqlite3.Error as erro:
        print(f"Erro ao dar baixo em insumo: {erro}.")
        
if __name__ == "__main__":
    criar_banco_de_dados()
    
    while True:
        print(""" SISTEMA DE GESTÃO DE INSUMOS LABORATORIAS
                  ================ MENU =================== 
                  1 - Cadastrar insumo
                  2 - Dar baixa em insumo 
                  3 - Encerrar o programa """)
        
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == "1":
            produto = input("Digite o nome do produto: ")
            tipo = input("Digite o tipo do produto: ")
            lote = input("Digite o lote do produto: ")
            data_fabricacao = input("Digite a data de fabricação do produto (no formato AAAA-MM-DD): ")
            data_validade = input("Digite a data de validadde do produto (no formato AAAA-MM-DD): ")
            quantidade = int(input("Digite a quantidade: "))
            
            cadastrar_insumo(produto, tipo, lote, data_fabricacao, data_validade, quantidade)

        elif opcao == "2":
            try:
               id_produto = input("Digite o código do produto: ")
               qtde = int(input("Digite a quantidade a dar baixa: "))
               baixar_insumo(id_produto, qtde)
            except ValueError:
                print("Valor inválido.")
                
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida.")