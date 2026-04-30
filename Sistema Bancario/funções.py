import os
def senha_forte(senha_aleatoria):
        procurando_caracter = len(senha_aleatoria.strip())
        tentar_novamente = str(input('Senha errada tente novamente: '))
        if len(tentar_novamente.strip()) > 8:
             return tentar_novamente
        else:
            print('\033[32mSenha Forte!\033[m')
            return senha_aleatoria
def email(email_nao_encontrado):
    if not '@gmail.com' in email_nao_encontrado:
        print('\033[31memail nao encontrado\033[m')
        while True:
                tentar_novamente =  str(input('Login errado tente novamente: \033[35m'))
                print(end='\033[m') 
                if not '@gmail.com' in tentar_novamente:
                     continue
                else:
                     email_nao_encontrado = tentar_novamente
                     break
    else:
        print('\033[32mEmail encontrado\033[m')
        return email_nao_encontrado
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
