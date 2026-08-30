# 🏦 Sistema Bancário Interativo em Python

Um sistema de gerenciamento de contas bancárias e simulação de investimentos executado via linha de comando (CLI), focado em validação de dados em tempo real, orientação a objetos, interface limpa no terminal e persistência de dados local com SQLite.

---

## ✨ Funcionalidades

* **Comprovação de Crédito:**
  * Validação automática de saldo mínimo (R$ 1.000,00) para liberação do acesso e cadastro da conta.
* **Módulo de Investimentos (Bolsa de Valores):**
  * Painel para compra de ações em tempo real (*PETR4, ITUB4, VALE3, ABEV3, BBDC3*) com débito direto no saldo da conta.
* **Validação Rígida de Entradas:**
  * **Nome:** Mínimo de 3 caracteres, apenas letras e formatação automática em *Capital Case*.
  * **E-mail:** Validação de formato correto com domínio e `@`.
  * **Senha:** Análise de força (mínimo de 8 caracteres, letras maiúsculas, números e caracteres especiais).
  * **Valores:** Tratamento rigoroso de exceções (`try/except`) para evitar travamentos por digitação incorreta e bloqueio de valores negativos.
* **Interface Dinâmica:** Limpeza automática do terminal a cada instrução para simular a navegação de um software profissional.
* **Persistência de Dados:** Integração com SQLite para armazenamento permanente dos clientes e atualização instantânea do saldo após depósitos, saques e investimentos.
* **Zero Dependências Externas:** Desenvolvido exclusivamente com bibliotecas padrão do Python (`sqlite3`, `os`).

---

## 📁 Estrutura do Projeto

```text
Sistema_Bancario/
├── __main__.py            # Ponto de entrada: orquestra a execução, análise de crédito e o loop principal
├── classes.py             # Classe ContaBancaria e renderização dos painéis (Conta e Bolsa)
├── funcoes.py             # Captura de dados, validações (nome, e-mail, senha) e controle de tela
├── sistema_financeiro.py  # Regras de negócio (saques, depósitos, compra de ações e comprovação de crédito)
└── banco_de_dados.py      # Camada de persistência SQLite (criação de tabela, inserção e atualização de saldo)

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **SQLite3** (Banco de dados relacional embutido)
* **OS** (Comandos do sistema operacional para limpeza do terminal)
```

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado em sua máquina.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone https://github.com/seu-usuario/sistema-bancario-python.git
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd sistema-bancario-python
   ```

3. **Execute o arquivo principal:**
   ```bash
   python __main__.py
   ```

## 🎮 Exemplo de Uso
```text
Ao iniciar a aplicação, você será guiado pelo cadastro e pela verificação de crédito:

Plaintext
--- SISTEMA DE COMPROVAÇÃO DE CRÉDITO ---
✅ Crédito aprovado! R$ 1500.00 atinge o requisito de R$ 1000.00.

=============================================
|              PAINEL DA CONTA              |
=============================================
| Cliente      | Anderson Silva             |
| E-mail       | anderson@gmail.com         |
| Saldo        | R$ 1500.00                 |
=============================================
[1] Depositar [2] Sacar [3] Ações [0] Sair
=============================================

Digite a opção desejada: 3
Ao acessar a opção [3] Ações, o painel da bolsa é exibido:


=============================================
|              PAINEL DA BOLSA              |
=============================================
   TICKER    |   LUCRO(R$)  | VALOR UNI(R$)
=============================================
[1] ⛽ PETR4 |   77.82B     |   R$ 38,50   |
[2] 🏦 ITUB4 |   43.82B     |   R$ 36,20   |
[3] ⛏️ VALE3  |   27.82B     |   R$ 61,10   |
[4] 🍻 ABEV3 |   15.19B     |   R$ 12,40   |
[5] 🏦 BBDC3 |   20.97B     |   R$ 13,80   |
=============================================