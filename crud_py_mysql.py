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
    comando = f'INSERT INTO filmes (nome_filme, nota_filme, genero_filme) VALUES ("{nome_filme}", {nota_filme}, "{genero_filme}")'
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
    id_filme = input('Digite o id do filmes para ser editado: ')
    nome_filme = input('Digite o nome do filme: ')
    nota_filme = float(input('Digite a nota do filme: '))
    genero_filme = input('Digite o genero do filme: ')
    comando = f'UPDATE filmes SET nome_filme = "{nome_filme}", nota_filme = "{nota_filme}", genero_filme = "{genero_filme}" WHERE idFilmes = "{id_filme}"'
    cursor.execute(comando)
    conexao.commit()


# Delete
def delete():
    id_filme = input('Digite o id do filme que você quer deleta: ')
    comando = f'DELETE FROM filmes WHERE idFilmes = "{id_filme}"'
    cursor.execute(comando)
    conexao.commit()


while True:
    print("Seja bem vindo ao banco de dados de filmes do Felipe Moreira!!! \n")
    print('1 - Adicionar filme ao banco de dados.\n')
    print('2 - Ve os filmes do banco de dados.\n')
    print('3 - Atualizar dados do filme.\n')
    print('4 - Deletar filme do banco de dados.\n')
    user_choice = input("Opção: ")

    if user_choice == "1":
        creat()
    elif user_choice == "2":
        read()
    elif user_choice == "3":
        update()
    elif user_choice == "4":
        delete()
    else:
        continue


# Fecha a conexão
cursor.close()
conexao.close()
