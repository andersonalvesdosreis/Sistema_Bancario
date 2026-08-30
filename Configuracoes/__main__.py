import funcoes
import classe
import banco_de_dados
import sistema_financeiro

def main():
    banco_de_dados.conectar()

    cliente_num1 = classe.ContaBancaria(
        nome=funcoes.nome(),
        email=funcoes.email(),
        senha=funcoes.senha_forte(),
        saldo=funcoes.saldo()
    )

    # Verificação de crédito antes de liberar a conta e salvar no banco
    if not sistema_financeiro.comprovacao_de_credito(cliente_num1.saldo, limite_minimo=1000.0):
        input("\nAcesso negado. Pressione ENTER para encerrar...")
        return

    banco_de_dados.salvar_cliente(cliente_num1)
    input("\nPressione ENTER para acessar o painel...")

    while True:
        funcoes.limpar_terminal()
        print(cliente_num1.tabela_com_menu())
        
        opcao = input("\nDigite a opção desejada: ").strip()
        
        if opcao == '1':
            cliente_num1.solicitar_deposito()
            banco_de_dados.atualizar_saldo(cliente_num1.email, cliente_num1.saldo)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '2':
            cliente_num1.solicitar_saque()
            banco_de_dados.atualizar_saldo(cliente_num1.email, cliente_num1.saldo)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '3':
            funcoes.limpar_terminal()
            print(cliente_num1.tabela_acao())
            cliente_num1.solicitar_acao()
            banco_de_dados.atualizar_saldo(cliente_num1.email, cliente_num1.saldo)
            input("\nPressione ENTER para voltar ao menu...")
        elif opcao == '0':
            funcoes.limpar_terminal()
            print("Sessão finalizada. Até logo!")
            break
        else:
            input("\n\033[31mOpção inválida!\033[m Pressione ENTER para tentar novamente...")

if __name__ == "__main__":
    main()