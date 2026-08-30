import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def email() -> str:
    limpar_terminal()
    while True:
        email_digitado = input('Digite seu e-mail: ').strip().lower()
        
        partes = email_digitado.split('@')
        
        # Exige exatamente 1 caractere '@' e nome de usuário não vazio
        if len(partes) == 2 and len(partes[0]) > 0:
            usuario, dominio = partes
            partes_dominio = dominio.split('.')
            
            # Exige que o domínio tenha ponto, nome do servidor e extensão válida (ex: 'com', 'br')
            if len(partes_dominio) >= 2 and all(len(p) > 0 for p in partes_dominio):
                limpar_terminal()
                print('\033[32mE-mail válido!\033[m')
                return email_digitado
        
        limpar_terminal()
        print('\033[31mE-mail inválido! Digite um formato válido (ex: usuario@dominio.com)\033[m')

def senha_forte() -> str:
    limpar_terminal()
    while True:
        senha_digitada = input('Digite sua senha: ')
        pontos = 0
        
        if len(senha_digitada) >= 8:
            pontos += 1
        if any(c.isupper() for c in senha_digitada):
            pontos += 1
        if any(c.isdigit() for c in senha_digitada):
            pontos += 1
        if any(c in "!@#$%&*" for c in senha_digitada):
            pontos += 1

        if pontos >= 3:
            limpar_terminal()
            print('\033[32mSenha aceita!\033[m')
            return senha_digitada
        else:
            limpar_terminal()
            print('\033[31mSenha fraca!\033[m Use ao menos 8 caracteres, letras maiúsculas, números e símbolos (!@#$%&*).')

def nome() -> str:
    limpar_terminal()
    while True:
        nome_digitado = input('Digite seu nome: ').strip().title()
        if len(nome_digitado) >= 3 and nome_digitado.replace(' ', '').isalpha():
            limpar_terminal()
            print('\033[32mNome validado!\033[m')
            return nome_digitado
        
        limpar_terminal()
        print('\033[31mNome inválido!\033[m Mínimo 3 letras, sem números.')

def saldo() -> float:
    limpar_terminal()
    while True:
        try:
            saldo_digitado = float(input('Digite o saldo inicial: R$ '))
            if saldo_digitado < 0:
                limpar_terminal()
                print('\033[31mSaldo inválido!\033[m O saldo não pode ser negativo.')
                continue
            
            limpar_terminal()
            print('\033[32mSaldo cadastrado com sucesso!\033[m')
            return saldo_digitado
        except ValueError:
            limpar_terminal()
            print('\033[31mEntrada inválida!\033[m Digite apenas números.')