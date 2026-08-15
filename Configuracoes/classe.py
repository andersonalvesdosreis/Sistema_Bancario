from rich.panel import Panel


class ContaBancaria:
    def __init__(self,email , senha ,nome , saldo):
        self.email = email
        self.senha = senha
        self.saldo = float(saldo)
        self.nome = nome

    def painel(self):
        conteudo = (
            f'Cliente: {self.nome}\nEmail: {self.email}\nSaldo: {self.saldo}'
        )
        client = Panel(
            conteudo,
            title= '[bold blue]Sistema Bancario[/bold blue]:'
        )
        return client

   