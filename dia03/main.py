# Sistema bancário básico

# O programa realiza as operações:
# Crias novos usuários
# Criar novas contas (poupança e corrente)
# Fazer depósito e saques
# Consultar o extrato
# Listar contas cadastradas

from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco

class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.limite_saques = 3
        self.numero_saques = 0
        self.extrato = []
        
    def depositar(self, valor):
        """ Deposita dinheiro na conta """
        if valor > 0:
            self.saldo += valor
            self.extrato.append({
                "tipo":"depósito",
                "valor": valor,
                "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            })
            print(f"O depósito de R${valor} foi realizado com sucesso. Saldo atual: R${self.saldo}.")
        else:
            print("O valor do depósito deve ser superior a R$0.")
            
    def sacar(self, valor):
        """ Saca dinheiro da conta """
        if valor <= self.saldo:
            if self.numero_saques < self.limite_saques:
                if valor > 0:
                    self.saldo -= valor
                    self.extrato.append({
                        "tipo": "saque",
                        "valor": valor,
                        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                    })
                    self.numero_saques += 1
                    print(f"Saque de R${valor} realizado com sucesso. Saldo atual: R${self.saldo}.")
                else:
                    print("Operação falhou. O valor do saque deve ser superior a R$0.")
            else:
                print(" Operação falhou. Você excedeu o limite de saques diários.")
        else:
            print("Operação falhou. Você não possui saldo o suficiente.")
            
    def visualizar_extrato(self):
        """ Exibe extrato da conta """
        for movimento in self.extrato:
            print(movimento)
            
    def __str__(self):
        """ Formata objeto conta para ser exibido na tela """
        return f"Agência: {self.agencia}, Conta: {self.numero_conta}, Titular: {self.usuario.nome}"
    
class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_conta, usuario, taxa_juros):
        super().__init__(agencia, numero_conta, usuario)
        self.taxa_juros = taxa_juros
        
    def aplicar_juros(self):
        rendimento = self.saldo * self.taxa_juros
        self.sacar += rendimento
        return rendimento
    
    def consultar_saldo(self):
        print(f"Saldo atual: {self.saldo}.")
        
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, usuario, limite, taxa_manutenção):
        super().__init__(agencia, numero_conta, usuario)
        self.limite = limite
        self.taxa_manutenção = taxa_manutenção
        
    def cobrar_taxa_mensal(self):
        self.saldo -= self.taxa_manutenção
        
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
        """ Filtra usuário por CPF e retorna se existir """
        for usuario in self.usuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
    
    def criar_conta(self, cpf):
        """ Cria conta de usuário """
        usuario = self.filtrar_usuario(cpf)
        
        if not usuario:
            print("Usuário não cadastrado.")
            return None
        
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                print("Usuário com esse CPF já cadastrado.")
                return None
            
        numero_conta = len(self.contas) + 1
        conta = Conta(self.agencia, numero_conta, usuario)
        self.contas.append(conta)
        print(f"Conta de {usuario.nome} criada com sucesso.")
        return conta
    
    def visualizar_contas(self):
        """ Visualiza as contas cadastradas """
        for conta in self.contas:
            print(conta)