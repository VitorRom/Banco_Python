class Banco:
    def __init__(self):
        self.usuarios = {}
        self.contas = {}

    def criar_usuario(self, nome, cpf):
        if cpf in self.usuarios:
            print("Usuário já existe.")
        else:
            self.usuarios[cpf] = {"nome": nome}
            print(f"Usuário {nome} criado com sucesso.")

    def criar_conta_corrente(self, cpf):
        if cpf not in self.usuarios:
            print("Usuário não encontrado.")
        elif cpf in self.contas:
            print("Usuário já possui uma conta.")
        else:
            self.contas[cpf] = {"saldo": 1000, "saques_feitos": 0, "extrato": []}
            print("Conta corrente criada com sucesso.")

    def saque(self, *, saldo, valor, extrato, limite=500, saques_feitos, max_saques=3):
        if saldo >= valor and saques_feitos < max_saques and valor <= limite:
            saldo -= valor
            saques_feitos += 1
            extrato.append(f"Saque de ${valor}")
            print(f"Saque de ${valor} realizado. Seu saldo é de ${saldo}.")
        elif saldo < valor:
            print("Saldo insuficiente para o saque.")
        elif saques_feitos >= max_saques:
            print("Limite de saques diários atingido.")
        elif valor > limite:
            print("Limite de saque por operação é de $500.")
        return saldo, saques_feitos, extrato

    def deposito(self, saldo, valor, extrato, /):
        saldo += valor
        extrato.append(f"Depósito de ${valor}")
        print(f"Depósito de ${valor} realizado. Seu saldo é de ${saldo}.")
        return saldo, extrato

    def extrato(self, saldo, *, extrato):
        print(f"Seu saldo é de ${saldo}.")
        print("Extrato:")
        for item in extrato:
            print(item)

banco = Banco()

while True:
    print("\nEscolha uma opção:")
    print("1 - Criar Usuário")
    print("2 - Criar Conta Corrente")
    print("3 - Saque")
    print("4 - Depósito")
    print("5 - Extrato")
    print("6 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        banco.criar_usuario(nome, cpf)
    elif opcao == "2":
        cpf = input("Digite o CPF do usuário: ")
        banco.criar_conta_corrente(cpf)
    elif opcao == "3":
        cpf = input("Digite o CPF do usuário: ")
        if cpf in banco.contas:
            valor = int(input("Digite o valor do saque: "))
            conta = banco.contas[cpf]
            conta["saldo"], conta["saques_feitos"], conta["extrato"] = banco.saque(
                saldo=conta["saldo"], valor=valor, extrato=conta["extrato"],
                saques_feitos=conta["saques_feitos"]
            )
        else:
            print("Conta não encontrada.")
    elif opcao == "4":
        cpf = input("Digite o CPF do usuário: ")
        if cpf in banco.contas:
            valor = int(input("Digite o valor do depósito: "))
            conta = banco.contas[cpf]
            conta["saldo"], conta["extrato"] = banco.deposito(conta["saldo"], valor, conta["extrato"])
        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        cpf = input("Digite o CPF do usuário: ")
        if cpf in banco.contas:
            conta = banco.contas[cpf]
            banco.extrato(conta["saldo"], extrato=conta["extrato"])
        else:
            print("Conta não encontrada.")
    elif opcao == "6":
        print("Sessão encerrada.")
        break
    else:
        print("Opção inválida. Tente novamente.")
