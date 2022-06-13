import mysql.connector

# Estabelece conexão entre Python e MySQL.
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='2011',
    database='bdcrud',
)

cursor = conexao.cursor()

"""
comando = ''
cursor.execute(comando) # executa o comando.
conexao.commit() # Edita o banco de dados.
resultado = cursor.fetchall() # ler o banco de dados.
"""
# CRUD

# Creat


def creat():
    nome_filme = input('Digite o nome do filme: ')
    nota_filme = float(input('Digite a nota do filme: '))
    genero_filme = input('Digite o genero do filme: ')
    comando = f'INSERT INTO filmes (nome_filme, nota_filme) VALUES ("{nome_filme}", {nota_filme}, "{genero_filme}")'
    cursor.execute(comando)
    conexao.commit()


# Read
def read():
    comando = f'SELECT * FROM filmes'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)


# Update
def update():
    nome_filme = input('Digite o nome do filme: ')
    nota_filme = float(input('Digite a nota do filme: '))
    genero_filme = input('Digite o genero do filme: ')
    comando = f'UPDATE filmes SET nota_filme = {nota_filme} WHERE nome_filme = "{nome_filme}" WHERE genero_filme = "{genero_filme}"'
    cursor.execute(comando)
    conexao.commit()


# Delete
def delete():
    nome_filme = input('Digite o nome do filme que você quer deleta: ')
    comando = f'DELETE FROM filmes WHERE nome_filme = "{nome_filme}"'
    cursor.execute(comando)
    conexao.commit()


# Fecha a conexão
cursor.close()
conexao.close()
