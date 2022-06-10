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


# Fecha a conexão
cursor.close()
conexao.close()
