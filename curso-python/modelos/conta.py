class ContaBancaria:
    def __init__(self, titular = '', saldo=0):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular.ljust(25)} | Saldo: R${self.saldo} | Ativo: {self._ativo}'

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True


conta1 = ContaBancaria('João', 1000)
conta2 = ContaBancaria('Maria', 1500)
conta3 = ContaBancaria('Maria de João', 1000)

print(conta1)
print(conta2)
print(conta3)
print('\n\n ativando contas\n\n')

# conta1._ativo = True
# conta2._ativo = True
# conta3._ativo = True

conta1._ativo = True
conta2._ativo = True
conta3._ativo = True
print(conta1)
print(conta2)
print(conta3)