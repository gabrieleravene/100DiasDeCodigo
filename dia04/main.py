# Sistema bancário básico

# O programa realiza as operações:
# Crias novos usuários
# Criar novas contas (poupança e corrente)
# Fazer depósito e saques
# Consultar o extrato
# Listar contas cadastradas
# Menu de interação com o usuário

from datetime import datetime

class Usuario:
    def __init__(self, nome, cpf, data_nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        
class ContaBancaria:
    def __init__(self, agencia,  numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.numero_saques = 0
        self.limite_saques = 3
        self.extrato = []
        
    def depositar(self, valor):
        """ Deposita dinheiro na conta """
        if valor > 0:
            self.saldo += valor
            self.extrato.append({
                "tipo": "depósito",
                "valor": valor,
                "data_hora": datetime.now().strftime("%d%m%Y %H:%M:%S")
            })
            print(f"Depósito de R${valor} realizado com sucesso. Saldo atual:R${self.saldo}.")
            return True
        print("Operação falhou! O valor do depósito deve ser superior a R$0.")
        return False
    
    def sacar(self, valor):
        """ Saca dinheiro da conta """
        if valor <= self.saldo:
            if self.numero_saques < self.limite_saques:
                if valor > 0:
                    self.saldo -= valor
                    self.extrato.append({
                        "tipo": "saque",
                        "valor": valor,
                        "data_hora": datetime.now().strftime("%d%m%Y %H:%M:%S")
                    })
                    self.numero_saques += 1
                    print(f"Saque de R${valor} realizado com sucesso! Saldo atual: {self.saldo}.")
                    return True
                print("Operação falhou! O valor do saque deve ser superior a R$0.")
                return False
            print("Operação falhou! Você excedeu o limite de saques diários.")
            return False
        print(f"Operação falhou! Você não posui saldo o suficiente. Saldo atual: R${self.saldo}.")
        return False
    
    def visualizar_extrato(self):
        """ Visualiza extrato da conta """
        for movimento in self.extrato:
            print(movimento)
            
    def __str__(self):
        """ Formata objeto conta para ser exibido na tela """
        return f"Agência: {self.agencia}, Conta: {self.numero_conta}, Titular: {self.usuario.nome}"
    
class ContaPoupanca(ContaBancaria):
    def __init__(self, agencia, numero_conta, usuario, taxa_juros):
        super().__init__(agencia, numero_conta, usuario)
        self.taxa_juros = taxa_juros
        
    def aplicar_juros(self):
        """ Aplica juros na conta """
        rendimento = self.saldo * self.taxa_juros
        self.sacar += rendimento
        return rendimento
    
    def consultar_saldo(self):
        """ Consulta o saldo da conta poupança """
        print(f"Saldo atual: {self.saldo}.")
        
class ContaCorrente(ContaBancaria):
    def __init__(self, agencia, numero_conta, usuario, limite, taxa_manutenção):
        super().__init__(agencia, numero_conta, usuario)
        self.limite = limite
        self.taxa_manutenção = taxa_manutenção
        
    def cobrar_manutenção(self):
        """ Cobra taxa de manutenção da conta """
        self.saldo -= self.taxa_manutenção
        
class Banco:
    def __init__(self):
        self.usuarios = [] 
        self.contas =[]
        self.agencia = "0001"
        
    def cadastrar_usuario(self, nome, cpf, data_nascimento, endereco):
        """ Cadastra novo usuário """
        if self.filtrar_usuario(cpf): 
            print("Usuário já cadastrado.")
            return None
        
        novo_usuario = Usuario(nome, cpf, data_nascimento, endereco) 
        self.usuarios.append(novo_usuario) 
        print(f"Usuário {novo_usuario.nome} cadastrado com sucesso.")
        return novo_usuario
            
    def filtrar_usuario(self, cpf):
        """ Filtra usuários por CPF e retorna o usuário caso ele seja encontrado """
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
                print("Usuário com esse CPF já possui uma conta.")
                print(conta.usuario.cpf)
                return None
            
        numero_conta = len(self.contas) + 1
        nova_conta = ContaBancaria(self.agencia, numero_conta, usuario)
        self.contas.append(nova_conta)
        print(f"Conta de {usuario.nome} criada com sucesso!")
        print(nova_conta)
        return nova_conta
        
    def visualizar_contas(self):
        """ Visualiza contas cadastradas """
        for conta in self.contas:
            print(conta)
            
if __name__ == "__main__":
    banco = Banco()
    
    while True:
        print("\nSistema Bancário")
        print("1- Cadastrar usuário")
        print("2 - Criar conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Visualizar extrato")
        print("6 - Listar contas")
        print("7 - Encerrar programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            cpf = input("CPF: ")
            data_nascimento = input("Data de nascimento: ")
            endereco = input("Endereço: ")
            banco.cadastrar_usuario(nome, cpf, data_nascimento, endereco)
            
        elif opcao == "2":
            cpf = input("CPF do usuário: ")
            banco.criar_conta(cpf)
            
        elif opcao == "3":
            cpf = input("CPF do titular: ")
            conta = banco.filtrar_usuario(cpf)
            if conta:
                valor = float(input("Valor do depósito: "))
                for c in banco.contas:
                    if c.usuario.cpf == cpf:
                        c.depositar(valor)
                        
        elif opcao == "4":
            cpf = input("CPF do titular: ")
            conta = banco.filtrar_usuario(cpf)
            if conta:
                valor = float(input("Valor do saque: "))
                for c in banco.contas:
                    if c.usuario.cpf == cpf:
                        c.sacar(valor)
                        
        elif opcao == "5":
            cpf = input("CPF do titular: ")
            for c in banco.contas:
                if c.usuario.cpf == cpf:
                    c.visualizar_extrato()
                    break
                else:
                    print("Conta não encontrada.")
                    
        elif opcao == "6":
            banco.visualizar_contas()
            
        elif opcao == "7":
            print("Fim do programa.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")      