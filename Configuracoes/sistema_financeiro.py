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
    return saldo  # Retorna o saldo original se cancelar

def pergunta_saque(saldo):
    if pedir_sim_ou_nao('Deseja sacar? '):
        valor = float(input('Digite o valor: R$ '))
        return saque(saldo=saldo, saq=valor)
    
    print('Ok! Saque cancelado.')
    return saldo  # Retorna o saldo original se cancelar