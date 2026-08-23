import funcoes
import classe
import banco_de_dados


cliente_num1 = classe.ContaBancaria(
    nome=funcoes.nome(),
    email=funcoes.email(),
    senha=funcoes.senha_forte(),
    saldo=funcoes.saldo()
)

banco_de_dados.salvar_cliente(cliente_num1)

def main():
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
     elif opcao == '0':
        funcoes.limpar_terminal()
        print("Sessão finalizada. Até logo!")
        break
     else:
        input("\n\033[31mOpção inválida!\033[m Pressione ENTER para tentar novamente...")

if __name__ == "__main__":
    main()