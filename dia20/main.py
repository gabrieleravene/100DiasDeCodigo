# Sistema de gestão de farmácia

# O sistema possui funcionalidades de:

# 1 - cadastrar cliente
# 2 - cadastrar medicamento
# 3 - cliente realizar compra

import sqlite3
from datetime import datetime

def criar_banco_de_dados():
    try:
        with sqlite3.connect("farma.db") as conexao:
            cursor = conexao.cursor()
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_completo TEXT,
                cpf TEXT,
                data_nascimento DATE
                ) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS medicamentos (
                id_medicamento INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                codigo TEXT,
                classificacao TEXT,
                data_fab DATE,
                data_val DATE,
                lote TEXT,
                quantidade INT,
                dose INT) """)
            
            cursor.execute(""" CREATE TABLE IF NOT EXISTS compras (
                id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INT,
                id_medicamento INT,
                cpf_cliente TEXT,
                medicamento TEXT,
                valor_unitario FLOAT,
                quantidade FLOAT,
                valor_total FLOAT,
                data DATE,
                FOREIGN KEY (id_cliente) references clientes (id_cliente),
                FOREIGN KEY (id_medicamento) references medicamentos (id_medicamento)) """)
            
            conexao.commit()
        
    except sqlite3.Error as erro:
        print(f"Erro ao criar banco de dados: {erro}")
        

class Cliente:
    def __init__(self, nome_completo, cpf, data_nascimento):
        self.nome = nome_completo
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        
class Medicamento:
    def __init__(self, nome, data_fab, data_val, lote, classificacao, quantidade=None, dose=None):
        self.nome = nome
        self.data_fab = data_fab
        self.data_val = data_val
        self.lote = lote
        self.classificacao = classificacao
        self.quantidade = quantidade
        self.dose = dose
        
class Compra:
    def __init__(self, id_cliente, id_medicamento, valor_unitario=None, quantidade=None, valor_total=None):
        self.id_cliente = id_cliente
        self.id_medicamento = id_medicamento
        self.valor_unitario = valor_unitario
        self.quantidade = quantidade
        self.valor_total = valor_total
        
class Farmacia:
    def __init__(self, nome, cnpj, responsavel):
        self.nome = nome
        self.cnpf = cnpj
        self.responsavel = responsavel
        
    def cadastrar_cliente(self, nome_completo, cpf, data_nascimento):
        try:
            with sqlite3.connect("farma.db") as conexao:
                cursor = conexao.cursor()
                
                cursor.execute(""" SELECT * FROM clientes WHERE cpf = ?  """, (cpf,))
                usuario = cursor.fetchone()
                
                if usuario:
                    print("Usuário já cadastrado.")
                    return
                
                cursor.execute(" INSERT INTO clientes (nome_completo, cpf, data_nascimento) VALUES (?, ?, ?) ", (nome_completo, cpf, data_nascimento))
                
                conexao.commit()
                
                print("Usuário cadastrado com sucesso.")
            
        except sqlite3.Error as erro:
            print(f"Erro ao cadastrar cliente: {erro}")
            
            
    def cadastrar_medicamento(self, nome, codigo, classificacao, data_fab, data_val, lote, quantidade=None, dose=None):
            try:
                with sqlite3.connect("farma.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute (" SELECT * FROM medicamentos WHERE codigo = ? ", (codigo,))
                    medicamento = cursor.fetchone()
                    
                    if medicamento:
                        print("Medicamento já cadastrado.")
                        return
                    
                    cursor.execute(" INSERT INTO medicamentos (nome, codigo, classificacao, data_fab, data_val, lote, dose, quantidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ", (nome, codigo, classificacao, data_fab, data_val, lote, dose, quantidade))
                    
                    conexao.commit()
                    
                    print("Medicamento cadastrado com sucesso.")
                    
            except sqlite3.Error as erro:
                print(f"Erro ao cadastrar medicamento: {erro}")
                
                
    def comprar_medicamento(self, cpf_cliente, medicamento, valor_unitario, quantidade):
            try:
                with sqlite3.connect("farma.db") as conexao:
                    cursor = conexao.cursor()
                    
                    cursor.execute(" SELECT * from clientes WHERE cpf = ? ", (cpf_cliente,))
                    cliente = cursor.fetchone()
                    
                    if not cliente:
                        print("Cliente não cadastrado.")
                        return
                    
                    id_cliente = cliente[0]
                    
                    cursor.execute(" SELECT * from medicamentos WHERE nome = ? ", (medicamento,))
                    medicamento = cursor.fetchone()
                    
                    quantidade_medicamento = medicamento[7]
                    id_medicamento = medicamento[0]
                    nome_medicamento = medicamento[1]
                    
                    if not medicamento:
                        print("Medicamento não encontrado.")
                        return
                        
                    if quantidade_medicamento < 1:
                        print("Medicamento não disponível no estoque no momento.")
                        return
                    
                    valor_total = quantidade * valor_unitario
                    data_atual = datetime.now().strftime("%Y-%m-%d")
                    
                    cursor.execute(" INSERT INTO compras (id_cliente, id_medicamento, cpf_cliente, medicamento, valor_unitario, quantidade, valor_total, data) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (id_cliente, id_medicamento, nome_medicamento, cpf_cliente, valor_unitario, quantidade, valor_total, data_atual))
                    
                    print(f"Compra realizada com sucesso. Total: {valor_total:.2f}")
                    
                    conexao.commit()
                        
            except sqlite3.Error as erro:
                print(f"Erro ao comprar medicamento: {erro}")
        
if __name__ == "__main__":
    criar_banco_de_dados()
    farmacia = Farmacia("drog+", "12345678-9", "ane silva")
    
    while True:
        print(""" SISTEMA DE GESTÃO DE FARMÁCIA 
              1 - Cadastrar cliente
              2 - Cadastrar medicamento
              3 - Realizar compra
              4 - Encerrar programa """)
        
        opcao = input("Digite a opção desejada: ")
        
        if opcao == '1':
            nome_completo = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input ("Data de nascimento (AAAA-MM-DD): ")
            farmacia.cadastrar_cliente(nome_completo, cpf, data_nascimento)
        
        elif opcao == '2':
            try:
                nome = input("Medicamento: ")
                codigo = input("Código: ")
                classificacao = input("Classificação: ")
                data_fab = input("Data de fabricação: ")
                dat_val = input("Data de validade: ")
                lote = input("Lote: ")
                dose = int(input("Dose: "))
                quantidade = int(input("Quantidade: "))
                farmacia.cadastrar_medicamento(nome, codigo, classificacao, data_fab, dat_val, lote, quantidade, dose)
            except ValueError: 
                print("Digite um valor válido.")
        
        elif opcao == '3':
            try:
                cpf_cliente = input("CPF do cliente: ")
                medicamento = input("Medicamento: ")
                quantidade = int(input("Quantidade: "))
                valor_unitario = float(input("Valor unitário: "))
                farmacia.comprar_medicamento(cpf_cliente, medicamento, quantidade, valor_unitario)
                
            except ValueError:
                print("Digite um valor válido.")
        
        elif opcao == '4':
            print("encerrando programa...")
            break
        
        else:
            print("opção inválida")