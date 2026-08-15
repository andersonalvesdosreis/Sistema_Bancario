import os

def senha_forte(senha_digitada):
    while True:
        # Se a senha for maior que 8 caracteres, retorna a senha
        if len(senha_digitada.strip()) > 8:
            print('\033[32mSenha Forte!\033[m')
            return senha_digitada
        
        # Se for menor, avisa e pede novamente
        print('\033[31mSenha Fraca!\033[m Digite mais de 8 caracteres!')
        senha_digitada = str(input('Tente novamente: '))


def email(email_digitado):
    # Enquanto não tiver @gmail.com, continua pedindo no mesmo loop
    while '@gmail.com' not in email_digitado:
        print('\033[31mEmail inválido / não encontrado\033[m')
        email_digitado = str(input('Login errado, tente novamente: \033[35m'))
        print(end='\033[m')
    
    print('\033[32mEmail encontrado!\033[m')
    return email_digitado  # Sempre retorna o email válido no final


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')