# Sistema bancário básico

# O programa realiza as operações:
# Crias novos usuários
# Criar novas contas
# Fazer depósito e saques
# Consultar o extrato
# Listar contas cadastradas

from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereço):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereço

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.limite = 500
        self.numero_saques = 0
        self.limite_saques = 3
        self.extrato = []
        self.saldo = 0
        
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append({
                "tipo": "deposito",
                "valor": valor,
                "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
            print(f"O depósito de R${valor} foi realizado com sucesso. Saldo atual: {self.saldo}.")
            return True
        else:
            print("Operação falhou! O valor do depósito deve ser superior a R$0.")
            return False
            
    def sacar(self, valor):
        if valor <= self.saldo:
            if self.numero_saques < self.limite_saques:
                if valor > 0:
                    self.saldo -= valor
                    self.extrato.append({
                    "tipo": "saque",
                    "valor": valor,
                    "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    })
                    print(f"O saque de R${valor} foi realizado com sucesso. Saldo atual: {self.saldo}.")
                    self.numero_saques += 1
                    return True
                else:
                    print("Operaçãoo falhou! O valor do saque deve ser superior a R$0.")
                    return False
            else:
                print("Operação falhou! Você ultrapassou o limite de saques diários.")
                return False
        else:
            print("Operação falhou! Você não possui saldo o suficiente.")
            return False
        
    def visualizar_extrato(self):
        """ Visualiza extrato bancário """
        for movimento in self.extrato:
            print(movimento)
            
    def __str__(self):
        return f"Agência: {self.agencia}, Conta: {self.numero_conta}, Titular: {self.usuario.nome}"
        
class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.agencia = "0001"
        
    def cadastrar_usuario(self, nome, cpf, data_nascimento, endereco):
        """ Cadastra novo usuário """
        if self.filtrar_usuario(cpf):
            print("Erro: CPF já cadastrado.")
            return None
        
        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {nome} cadastrado com sucesso.")
        return novo_usuario
        
    def filtrar_usuario(self, cpf):
        """ Filta usuário por CPF e retorna se existir """
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
        
    def criar_conta(self, cpf):
        """ Cria conta de usuário """
        usuario = self.filtrar_usuario(cpf)
        
        if not usuario:
            print("Usuário não existe.")
            return None
        
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                print("Usuário com esse CPF já cadastrado.")
                return None
            
        numero_conta = len(self.contas) + 1
        conta = Conta(self.agencia, numero_conta, usuario)
        self.contas.append(conta)
        print("Conta criada com sucesso.")
        return conta
    
    def visualizar_contas(self):
        """ Visualiza as contas cadastradas """
        for conta in self.contas:
            print(conta)