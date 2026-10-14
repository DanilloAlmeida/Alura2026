class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
            # return f'Titular: {self.titular.ljust(25)} | Saldo: R${self.saldo} | Ativo: {self.ativo}'
            return f'Titular: {self._titular.ljust(25)} | Saldo: R${self._saldo} | Ativo: {self._ativo}'

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True


conta1 = ContaBancariaPythonica('João', 1000)
conta2 = ContaBancariaPythonica('Maria', 1500)
conta3 = ContaBancariaPythonica('Maria de João', 1000)

print(conta1)
print(conta2)
print(conta3)

print('\n ativando contas\n')
# conta1._ativo = True
# conta2._ativo = True
# conta3._ativo = True
ContaBancariaPythonica.ativar_conta(conta1)
ContaBancariaPythonica.ativar_conta(conta2)
ContaBancariaPythonica.ativar_conta(conta3)
print(conta1)
print(conta2)
print(conta3)
print('\n desativando contas\n')
conta1._ativo = False
conta2.ativo = False
conta3._ativo = False
print(conta1)
print(conta2)
print(conta3)