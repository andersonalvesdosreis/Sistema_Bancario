class ContaBancaria:
    def __init__(self,email , senha ,nome , saldo):
        self.email = email
        self.senha = senha
        self.saldo = float(saldo)
        self.nome = nome

    def tabela_moldura(self):
     return (
        "┌──────────────┬────────────────────────────┐\n"
        f"│ {'Cliente':<12} │ {self.nome:<26} │\n"
        f"│ {'E-mail':<12} │ {self.email:<26} │\n"
        f"│ {'Saldo':<12} │ R$ {self.saldo:<23.2f} │\n"
        "└──────────────┴────────────────────────────┘"
    )