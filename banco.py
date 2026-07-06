import datetime

class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.agencia = "0000-0"
        self.conta = "000000-0"
        self.saldo = 0.0
        self.extrato = []

    def depositar(self, valor):
        self.saldo += valor
        self.adicionarExtrato(f"\nDepositado R${valor}")

    def sacar(self, valor)
        if (self.saldo <= 0 and self.saldo > valor):
            print("\nSALDO INSUFICIENTE")
        else: 
            self.saldo -= valor
            self.adicionarExtrato(f"\nSacado R${valor}")
            print(f"Saldo atual: {self.saldo}")

    def adicionarExtrato(self, descricao):
        self.extrato.append(
            [descricao, self.saldo, datetime.now().strftime("%D %H:%M:%S")]
        )
        
