class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome.title()
        self.idade = idade
        self.profissao = profissao.title()

    def __str__(self):
        return f'{self.nome} - {self.idade} anos - {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}. Trabalho como {self.profissao}.'
        return f'Olá, sou {self.nome}.'

    def aniversario(self):
        self.idade += 1

Pessoa1 = Pessoa('joão', 30, 'engenheiro')
Pessoa2 = Pessoa('maria', 25, 'médica')

print(Pessoa1)
print(Pessoa2)
print(Pessoa1.saudacao)
print(Pessoa2.saudacao)
print(f'Idade antes do aniversário: {Pessoa1.idade}')
Pessoa1.aniversario()
print(f'Idade após o aniversário: {Pessoa1.idade}')
print(f'Idade antes do aniversário: {Pessoa2.idade}')
Pessoa2.aniversario()
print(f'Idade após o aniversário: {Pessoa2.idade}')