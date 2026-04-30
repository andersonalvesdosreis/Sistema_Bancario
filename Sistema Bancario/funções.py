import os
def senha_forte(senha_digitada):
    while True:
        # Se a senha for maior que 8, ele retorna ela e sai da função
        if len(senha_digitada.strip()) > 8:
            print('\033[32mSenha Forte!\033[m')
            return senha_digitada
        else:
            # Se for menor, ele avisa e pede outra vez dentro do loop
            print('\033[31mSenha Fraca!\033[m Digite mais de 8 caracteres!')
            senha_digitada = str(input('Tente novamente: '))
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
