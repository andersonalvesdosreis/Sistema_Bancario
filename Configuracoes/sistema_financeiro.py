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


def pedir_sim_ou_nao(mensagem: str) -> bool:
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ['s', 'sim']:
            return True
        elif resposta in ['n', 'nao', 'não']:
            return False
        print("\033[31mOpção inválida! Digite 's' para sim ou 'n' para não.\033[m")

def depositar(saldo: float, dep: float) -> float:
    if dep <= 0:
        print("\033[31mValor de depósito deve ser maior que zero!\033[m")
        return saldo
    return saldo + dep

def saque(saldo: float, saq: float) -> float:
    if saq <= 0:
        print("\033[31mValor de saque inválido!\033[m")
        return saldo
    if saq > saldo:
        print(f"\033[31mSaldo insuficiente para sacar R$ {saq:.2f}\033[m")
        return saldo  
    return saldo - saq

def pergunta_dep(saldo: float) -> float:
    if pedir_sim_ou_nao('Deseja depositar?'):
        while True:
            try:
                valor = float(input('Digite o valor: R$ '))
                return depositar(saldo, valor)
            except ValueError:
                print("\033[31mValor inválido! Digite apenas números.\033[m")
    print('Depósito cancelado.')
    return saldo 

def pergunta_saque(saldo: float) -> float:
    if pedir_sim_ou_nao('Deseja sacar?'):
        while True:
            try:
                valor = float(input('Digite o valor: R$ '))
                return saque(saldo, valor)
            except ValueError:
                print("\033[31mValor inválido! Digite apenas números.\033[m")
    print('Saque cancelado.')
    return saldo  

def comprar_acao(saldo: float, num_da_acao: int) -> float:
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

    while True:
        try:
            quantidade = int(input('Deseja comprar quantas ações? '))
            break
        except ValueError:
            print("\033[31mDigite um número inteiro válido!\033[m")

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero!")
        return saldo

    preco_unitario = precos[num_da_acao]
    custo_total = preco_unitario * quantidade

    if saldo >= custo_total:
        saldo -= custo_total
        print(f"\033[32mCompra realizada com sucesso! Custo total: R$ {custo_total:.2f}\033[m")
        print(f"Novo saldo: R$ {saldo:.2f}")
    else:
        print(f"\033[31mSaldo insuficiente! Você precisa de R$ {custo_total:.2f}, mas tem R$ {saldo:.2f}\033[m")

    return saldo