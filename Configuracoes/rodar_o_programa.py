import funcoes
from funcoes import limpar_terminal
import sistema_financeiro
import classe


cliente_num1 = classe.ContaBancaria(email=funcoes.email(), 
                                    senha=funcoes.senha_forte(), 
                                    nome=funcoes.nome(), 
                                    saldo=funcoes.saldo())

print(cliente_num1.tabela_com_menu())

while True:
    funcoes.limpar_terminal()
    print(cliente_num1.tabela_com_menu())
    
    opcao = input("\nDigite a opção desejada: ").strip()
    
    if opcao == '1':
        cliente_num1.solicitar_deposito()
        input("\nPressione ENTER para voltar ao menu...")
    elif opcao == '2':
        cliente_num1.solicitar_saque()
        input("\nPressione ENTER para voltar ao menu...")
    elif opcao == '0':
        funcoes.limpar_terminal()
        print("Sessão finalizada. Até logo!")
        break
    else:
        input("\n\033[31mOpção inválida!\033[m Pressione ENTER para tentar novamente...")