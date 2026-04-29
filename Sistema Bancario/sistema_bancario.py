import requests
import sqlite3
import os
import time

print('='*30,'Bem vindo Ao Banco Central','='*30)
print('\n')
print('\n')
pergunta = int(input('Digite oque deseja fazer:' \
'\n[1] Criar uma conta' \
'\n[2] Acessar a Minha conta' \
'\n[3] Consultar investimentos' \
'\n[4] Outro...'))

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
dados = requisicao.json()
cotacao = dados['USDBRL']['bid'] # O 'bid' é o valor de compra

conexao = sqlite3.connect('meu_projeto.db')
cursor = conexao.cursor()

conexao.commit()
conexao.close()

print("Dados salvos com sucesso!")