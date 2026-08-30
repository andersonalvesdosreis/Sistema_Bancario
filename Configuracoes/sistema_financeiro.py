def comprovacao_de_credito(saldo_ou_renda: float, limite_minimo: float = 1000.0) -> bool:
    """
    Verifica se o usuário possui saldo ou renda suficiente para entrar no banco/investir.
    Retorna True se aprovado, ou False caso contrário.
    """
    print("\n--- SISTEMA DE COMPROVAÇÃO DE CRÉDITO ---")
    
    if saldo_ou_renda >= limite_minimo:
        print(f"✅ Crédito aprovado! R$ {saldo_ou_renda:.2f} atinge o requisito de R$ {limite_minimo:.2f}.")
        return True
    else:
        faltante = limite_minimo - saldo_ou_renda
        print(f"❌ Crédito recusado! Faltam R$ {faltante:.2f} para o requisito de R$ {limite_minimo:.2f}.")
        return False


saldo_usuario = 1500.0

if comprovacao_de_credito(saldo_usuario, limite_minimo=1000.0):
    print("Acesso ao banco liberado com sucesso!")
else:
    print("Acesso negado. Procure seu gerente.")

def comprar_acao(saldo: float | int, num_da_acao: int) -> float:
    precos = {
        1: 38.50, # PETR4
        2: 36.20, # ITUB4
        3: 61.10, # VALE3
        4: 12.40, # ABEV3
        5: 13.80  # BBDC3
    }
    
    if num_da_acao not in precos:
        print("Opção de ação inválida!")
        return saldo

    quantidade = int(input('Deseja comprar quantas? '))
    
    if quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
        return saldo

    preco_unitario = precos[num_da_acao]
    custo_total = preco_unitario * quantidade

    if saldo >= custo_total:
        saldo -= custo_total
        print(f"Compra realizada com sucesso! Custo total: R$ {custo_total:.2f}")
        print(f"Saldo restante: R$ {saldo:.2f}")
    else:
        print(f"Saldo insuficiente! Você precisa de R$ {custo_total:.2f}, mas tem R$ {saldo:.2f}")

    return saldo

def pedir_sim_ou_nao(mensagem):
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        print("\033[31mOpção inválida! Digite apenas 's' (sim) ou 'n' (não).\033[m")

def depositar(saldo, dep):
    if dep <= 0:
        print("\033[31mValor de depósito deve ser maior que zero!\033[m")
        return saldo
    return saldo + dep

def saque(saldo, saq):
    if saq <= 0:
        print("\033[31mValor de saque inválido!\033[m")
        return saldo
    if saq > saldo:
        print(f"\033[31mSaldo insuficiente para sacar R${saq:.2f}\033[m")
        return saldo  
    
    return saldo - saq


#Função principal:


def pergunta_dep(saldo):
    if pedir_sim_ou_nao('Deseja depositar? '):
        valor = float(input('Digite o valor: R$ '))
        return depositar(saldo=saldo, dep=valor)
    
    print('OK! Depósito cancelado.')
    return saldo 

def pergunta_saque(saldo):
    if pedir_sim_ou_nao('Deseja sacar? '):
        valor = float(input('Digite o valor: R$ '))
        return saque(saldo=saldo, saq=valor)
    
    print('Ok! Saque cancelado.')
    return saldo  