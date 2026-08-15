import sistema_financeiro

class ContaBancaria:
    def __init__(self,email , senha ,nome , saldo):
        self.email = email
        self.senha = senha
        self.saldo = float(saldo)
        self.nome = nome

    def solicitar_deposito(self):
        self.saldo = sistema_financeiro.pergunta_dep(self.saldo)

    def solicitar_saque(self):
        self.saldo = sistema_financeiro.pergunta_saque(self.saldo)

    def tabela_com_menu(self):
     largura = 45
     linha = "=" * largura
    
     return (
        f"{linha}\n"
        f"| {'PAINEL DA CONTA':^41} |\n"
        f"{linha}\n"
        f"| {'Cliente':<12} | {self.nome:<26} |\n"
        f"| {'E-mail':<12} | {self.email:<26} |\n"
        f"| {'Saldo':<12} | R$ {self.saldo:<23.2f} |\n"
        f"{linha}\n"
        f"  [1] Depositar   |   [2] Sacar   |   [0] Sair\n"
        f"{linha}"
     )
