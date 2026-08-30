import sistema_financeiro

class ContaBancaria:
    def __init__(self, email: str, senha: str, nome: str, saldo: float):
        self.email = email
        self.senha = senha
        self.saldo = float(saldo)
        self.nome = nome

    def solicitar_deposito(self):
        self.saldo = sistema_financeiro.pergunta_dep(self.saldo)

    def solicitar_saque(self):
        self.saldo = sistema_financeiro.pergunta_saque(self.saldo)

    def solicitar_acao(self):
        opcao = input("\nDigite a opção da ação desejada (1-5) ou outra tecla para sair: ").strip()
        if opcao in ['1', '2', '3', '4', '5']:
            self.saldo = sistema_financeiro.comprar_acao(saldo=self.saldo, num_da_acao=int(opcao))

    def tabela_acao(self) -> str:
        largura = 45
        linha = "=" * largura
        return (
            f"{linha}\n"
            f"| {'PAINEL DA BOLSA':^41} |\n"
            f"{linha}\n"
            f"   TICKER    |   LUCRO(R$)  | VALOR UNI(R$)\n"
            f"{linha}\n"
            f"[1] ⛽ PETR4 |   77.82B     |   R$ 38,50   |\n"
            f"[2] 🏦 ITUB4 |   43.82B     |   R$ 36,20   |\n"
            f"[3] ⛏️ VALE3  |   27.82B     |   R$ 61,10   |\n"
            f"[4] 🍻 ABEV3 |   15.19B     |   R$ 12,40   |\n"
            f"[5] 🏦 BBDC3 |   20.97B     |   R$ 13,80   |\n"
            f"{linha}"
        )

    def tabela_com_menu(self) -> str:
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
            f"[1] Depositar [2] Sacar [3] Ações [0] Sair\n"
            f"{linha}"
        )