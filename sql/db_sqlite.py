import sqlite3


conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()


cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'nome TEXT,'
                'peso REAL'
                ')')


cursor.execute('SELECT nome, peso FROM clientes WHERE peso>90')

conexao.commit()

cursor.execute('SELECT * FROM clientes')

cursor.fetchall()

for linha in cursor.fetchall():
    nome, peso = linha

    print( nome, peso)

cursor.close()
conexao.close()