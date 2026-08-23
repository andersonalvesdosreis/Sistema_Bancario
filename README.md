# 🏦 Sistema Bancário Interativo em Python

Um sistema de gerenciamento de contas bancárias executado via linha de comando (CLI), focado em validação de dados em tempo real, orientação a objetos, interface limpa no terminal e persistência de dados local com SQLite.

---

## ✨ Funcionalidades

* **Validação Rígida de Entradas:**
  * **Nome:** Mínimo de 3 caracteres, apenas letras e formatação automática em *Capital Case*.
  * **E-mail:** Verificação do formato correto.
  * **Senha:** Validação de força (Caracteres Especiais, Letras Maiusculas, etc..).
  * **Valores:** Tratamento de exceções contra digitação de letras e impedimento de saldos/operações negativas.
* **Interface Dinâmica:** Limpeza automática do terminal a cada instrução para simular a navegação de um software profissional.
* **Persistência de Dados:** Integração com SQLite para armazenamento permanente dos clientes e atualização instantânea de saldos.
* **Zero Dependências Externas:** Desenvolvido exclusivamente com bibliotecas padrão do Python (`sqlite3`, `os`).

---

## 📁 Estrutura do Projeto

```text
Sistema_Bancario/
├── __main__.py                # Ponto de entrada: orquestra a execução e o loop principal
├── classe.py              # Classe ContaBancaria e renderização do painel/menu
├── funcoes.py             # Captura de dados, validações e controle de tela
├── sistema_financeiro.py  # Regras de negócio para saques e depósitos
└── banco_de_dados.py      # Camada de persistência e comandos SQL
```

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **SQLite3** (Banco de dados relacional embutido)
* **OS** (Comandos do sistema operacional para limpeza do terminal)

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* Python 3.8 ou superior instalado em sua máquina.

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/sistema-bancario-python.git](https://github.com/seu-usuario/sistema-bancario-python.git)
   ```

2. **Acesse o diretório do projeto:**
   ```bash
   cd sistema-bancario-python
   ```

3. **Execute o arquivo principal:**
   ```bash
   python main.py
   ```

---

## 🎮 Exemplo de Uso

Ao iniciar a aplicação, você será guiado pelo processo de cadastro:

```text
=============================================
|              PAINEL DA CONTA              |
=============================================
| Cliente      | Anderson Silva             |
| E-mail       | anderson@gmail.com         |
| Saldo        | R$ 1000.00                 |
=============================================
  [1] Depositar   |   [2] Sacar   |   [0] Sair
=============================================

Digite a opção desejada:
```

Ao efetuar um depósito ou saque, o valor do saldo é recalculado e imediatamente atualizado no arquivo `banco.db`.