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
# conta1._ativo = False
# conta2.ativo = False
# conta3._ativo = False
print(conta1)
print(conta2)
print(f'{conta3}\n\n')

class ClienteBanco:
    def __init__(self, nome, idade, endereco, cpf, profissao):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.profissao = profissao
        self.conta = None

    def __str__(self):
        return f'Cliente: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}, Profissão: {self.profissao}, Endereço: {self.endereco}'

    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        titular.conta = ContaBancariaPythonica(titular.nome, saldo_inicial)
        return titular.conta

cliente1 = ClienteBanco('João', 30, 'Rua A', '123.456.789-00', 'Engenheiro')
cliente2 = ClienteBanco('Maria', 25, 'Rua B', '987.654.321-00', 'Médica')
cliente3 = ClienteBanco('José', 40, 'Rua C', '456.789.123-00', 'Professor')

print(cliente1)
print(cliente2)
print(cliente3)

conta_cliente1 = ClienteBanco.criar_conta(cliente1, 1000)
print('\n\n dados da conta do cliente 1:')
print(f'{conta_cliente1}')
print('\n\ndados do cliente 1:')
print(cliente1)