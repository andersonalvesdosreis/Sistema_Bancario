import funcoes
from rich.panel import Panel
from rich import print


class ContaBancaria:
    def __init__(self,email , senha ,saldo=0 , nome=''):
        self.email = funcoes.email(email)
        self.senha = funcoes.senha_forte(senha)
        self.saldo = saldo
        self.nome = nome

    def pergunta_d(self):
        

    def tabela(self):
        conteudo = (
            f'Cliente: {self.nome}\nEmail: {self.email}\nSaldo: {self.saldo}'
        )
        client = Panel(
            conteudo,
            title= '[bold blue]Sistema Bancario[/bold blue]:'
        )
        