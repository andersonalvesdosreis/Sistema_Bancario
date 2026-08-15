import os

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def email():
    limpar_terminal()
    email_digitado = str(input('Digite seu e-mail: '))
    
    while '@gmail.com' not in email_digitado:
        limpar_terminal()
        print('\033[31mEmail inválido / não encontrado\033[m')
        email_digitado = str(input('Login errado, tente novamente: \033[35m'))
        print(end='\033[m')
    
    limpar_terminal()
    print('\033[32mEmail encontrado!\033[m')
    return email_digitado


def senha_forte():
    limpar_terminal()
    senha_digitada = str(input('Digite sua senha: '))
    
    while True:
        if len(senha_digitada.strip()) > 8:
            limpar_terminal()
            print('\033[32mSenha Forte!\033[m')
            return senha_digitada
        
        limpar_terminal()
        print('\033[31mSenha Fraca!\033[m Digite mais de 8 caracteres!')
        senha_digitada = str(input('Tente novamente: '))

def nome():
    limpar_terminal()
    nome_digitado = str(input('Digite seu nome: ')).strip().title()
    
    # Valida se tem pelo menos 3 caracteres e se contém apenas letras/espaços
    while len(nome_digitado) < 3 or not nome_digitado.replace(' ', '').isalpha():
        limpar_terminal()
        print('\033[31mNome inválido!\033[m Digite um nome válido (mínimo 3 letras, sem números).')
        nome_digitado = str(input('Tente novamente: ')).strip().title()
    
    limpar_terminal()
    print('\033[32mNome validado!\033[m')
    return nome_digitado

def saldo():
    limpar_terminal()
    while True:
        try:
            saldo_digitado = float(input('Digite o saldo inicial: R$ '))
            if saldo_digitado < 0:
                limpar_terminal()
                print('\033[31mSaldo inválido!\033[m O saldo inicial não pode ser negativo.')
                continue
            
            limpar_terminal()
            print('\033[32mSaldo cadastrado com sucesso!\033[m')
            return saldo_digitado
        except ValueError:
            limpar_terminal()
            print('\033[31mEntrada inválida!\033[m Digite apenas números (ex: 1000 ou 250.50).')