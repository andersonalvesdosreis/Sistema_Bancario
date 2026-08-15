import sqlite3

BANCO = 'banco.db'

def conectar():
    """Cria a conexão e a tabela de clientes se ela ainda não existir."""
    with sqlite3.connect(BANCO) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                saldo REAL NOT NULL
            )
        ''')
        conn.commit()

def salvar_cliente(cliente):
    """Salva um novo objeto ContaBancaria no banco."""
    conectar()
    try:
        with sqlite3.connect(BANCO) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clientes (nome, email, senha, saldo)
                VALUES (?, ?, ?, ?)
            ''', (cliente.nome, cliente.email, cliente.senha, cliente.saldo))
            conn.commit()
            print("\033[32mCliente cadastrado no banco de dados!\033[m")
    except sqlite3.IntegrityError:
        print("\033[31mErro: E-mail já cadastrado no banco!\033[m")

def atualizar_saldo(email, novo_saldo):
    """Atualiza o saldo do cliente após saques ou depósitos."""
    with sqlite3.connect(BANCO) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE clientes SET saldo = ? WHERE email = ?
        ''', (novo_saldo, email))
        conn.commit()