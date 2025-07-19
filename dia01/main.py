# Sistema bancário básico

# O programa realiza as operações:
# Crias novos usuários
# Criar novas contas
# Fazer depósito e saques
# Consultar o extrato

from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
  
class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3
        self.extrato = ""
        
    def depositar(self, valor):
        """ Faz depósito na conta """
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
        else:
            print("Operação falhou. O valor do depósito deve ser superior a R$0.")
            
    def sacar(self, valor):
        """ Saca dinheiro da conta """
        if self.numero_saques < self.limite_saques:
            if valor <= self.saldo:
                self.saldo -= valor
                self.registrar_transacao("Saque", -valor)
                self.numero_saques += 1
            elif valor < 0:
                print("Operação falhou. O valor do saque deve ser superior a R$0.")
            else:
                print("Operação falhou. Saldo insuficiente.")
        else:
            print("Operação falhou. Você atingiu o limite de saques diários.")
            
    def mostrar_historico(self):
        """ Mostra extrato bancário """
        print("\n=== EXTRATO ===")
        if self.extrato:
            print(self.extrato)
        else:
            print("Não foram realizadas movimentações.")
        print(f"Saldo: {self.saldo}")
            
    def registrar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato += f"{tipo}:\t\tR$ {valor:>10.2f} ({data_hora})\n"

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
        
    def criar_conta(self, usuario):
        """ Cria conta do usuário """
        numero_conta = len(self.contas) + 1
        conta = Conta(self.agencia, numero_conta, usuario)
        self.contas.append(conta)
        return conta