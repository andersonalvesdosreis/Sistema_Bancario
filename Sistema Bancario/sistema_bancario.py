import requests
import sqlite3
import os
from time import sleep

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dados = requisicao.json()
cotacao = dados['USDBRL']['bid'] # O 'bid' é o valor de compra

deposito = 0
investimento = 0

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

while True:
     print('='*30,'Bem vindo Ao Banco Central','='*30)
     pergunta = int(input('Digite oque deseja fazer:' \
     '\n[1] Criar uma conta' \
     '\n[2] Acessar a Minha conta' \
     '\n>>>>'))
     if pergunta == 1:
          limpar_terminal()
          print('='*20,'Crie um usuario e uma senha','='*20)
          login = email(str(input('login: \033[32m')))
          print(end='\033[m')
          senha = senha_forte(str(input('Digite a Senha:  \033[32m')))
          print(end='\033[m')
          print('\033[32mEmail e Senha Fortes!\033[m')
          conexao = sqlite3.connect('login.db')
          cursor = conexao.cursor()
          cursor.execute('''
              CREATE TABLE IF NOT EXISTS usuarios (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  login TEXT NOT NULL,
                  senha TEXT NOT NULL
              )
          ''')
          cursor.execute('INSERT INTO usuarios (login, senha) VALUES (?, ?)', (login, senha))
          print("\033[32mConta criada e salva no banco de dados com sucesso!\033[m")
          conexao.commit()
          conexao.close()
          print("Dados salvos com sucesso!")
     elif pergunta == 2:
        limpar_terminal()
        print('='*20, 'Acesse sua Conta', '='*20)
        
        # Pedindo os dados para conferir
        usuario_login = str(input('Digite seu login: ')).strip()
        usuario_senha = str(input('Digite sua senha: ')).strip()
        
        # Conectando ao banco
        conexao = sqlite3.connect('login.db')
        cursor = conexao.cursor()
        
        # O comando SELECT: Procure onde o login E a senha sejam iguais aos informados
        cursor.execute('SELECT * FROM usuarios WHERE login = ? AND senha = ?', (usuario_login, usuario_senha))
        
        # Tenta pegar o resultado
        usuario_encontrado = cursor.fetchone()
        
        conexao.close()
        
        if usuario_encontrado:
            limpar_terminal()
            print(f'\033[32mBem-vindo de volta, {usuario_login}!\033[m')
            print('\n')
            while True:
                 pergunta2 = int(input('Digite oque deseja fazer:' \
                 '\n[1] Depositar' \
                 '\n[2] Acessar os Investimentos'
                 '\n[3] Sair'
                 '\n>>>'))
                 if pergunta2 == 1:
                      deposito = float(input('Quanto deseja transferir para sua conta?'))
                      print('Transferindo...')
                      sleep(3)
                      print('\n')
                      print('Tranferencia Realizada com Sucesso!')
                      limpar_terminal()
                      continue
                 elif pergunta2 == 2:
                      print('='*20,'Sistema Bancario','='*20)
                      print(f'{login}:')
                      print(f'Valor na conta: R${deposito}')
                      print(f'Valor do Dolar hoje: R${cotacao}')
                      print(f'Valor investido no Dolar: R${investimento}')
                      pergunta3 = int(input('Deseja investir no Dolar hoje?' \
                      '\n[1] Sim' \
                      '\n[2] Não'
                      '\n>>>'))
                      if pergunta3 == 1:
                        print('Perfeito!')
                        sleep(1)
                        limpar_terminal()
                        print(f'Usuário: {usuario_login}')
                        print(f'Saldo disponível: R${deposito:.2f}')
                        valor_investir = float(input('Quanto deseja investir (em Reais)? R$'))
                        if valor_investir > deposito:
                              print('\033[31mSaldo insuficiente para este investimento!\033[m')
                              sleep(2)
                        elif valor_investir <= 0:
                              print('\033[31mValor inválido!\033[m')
                              sleep(2)
                        else:
                              compra_dolar = valor_investir / float(cotacao)
                              investimento += compra_dolar
                              print(f'\n\033[32mInvestimento realizado!\033[m')
                              print(f'Você comprou: US${compra_dolar:.2f}')
                              sleep(3)
                              pergunta6 = int(input('Deseja sair?' \
                                                 '\n[1] Sim' \
                                                 '\n[2] Não' \
                                                 '\n>>>'))
                              if pergunta6 == 1:
                                     limpar_terminal()
                                     break
                              else:
                                     continue
                      else:
                           pergunta4 = int(input('Deseja sair?' \
                                                 '\n[1] Sim' \
                                                 '\n[2] Não' \
                                                 '\n>>>'))
                           if pergunta4 == 1:
                                limpar_terminal()
                                break
                           else:
                                continue
        else:
            print('\033[31mErro: Login ou Senha incorretos!\033[m')
     else:
      print('Não conseguir entender!')
      sleep(1)
      limpar_terminal()
      continue