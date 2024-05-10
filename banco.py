class Banco:
    def __init__(self):
        self.saldo = 1000  
        self.saques_feitos = 0

    def saque(self, valor):
        if self.saldo >= valor and self.saques_feitos < 3 and valor <= 500:
            self.saldo -= valor
            self.saques_feitos += 1
            print(f"Saque de ${valor} realizado. Seu saldo é de ${self.saldo}.")
        elif self.saldo < valor:
            print("Saldo insuficiente para o saque.")
        elif self.saques_feitos >= 3:
            print("Limite de saques diários atingido.")
        elif valor > 500:
            print("Limite de saque por operação é de $500.")

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de ${valor} realizado. Seu saldo é de ${self.saldo}.")

    def extrato(self):
        print(f"Seu saldo é de ${self.saldo}. Saques feitos hoje: {self.saques_feitos}.")

banco = Banco()

while True:
    print("\nEscolha uma opção:")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = int(input("Digite o valor do saque: "))
        banco.saque(valor)
    elif opcao == "2":
        valor = int(input("Digite o valor do depósito: "))
        banco.deposito(valor)
    elif opcao == "3":
        banco.extrato()
    elif opcao == "4":
        print("Sessão encerrada.")
        break
    else:
        print("Opção inválida. Tente novamente.")
