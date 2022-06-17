
import mysql.connector

"""
comando = ''
cursor.execute(comando) # executa o comando.
conexao.commit() # Edita o banco de dados.
resultado = cursor.fetchall() # ler o banco de dados.
"""


class filmeController:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='2011',
            database='bdcrud',
        )

        self.cursor = self.conexao.cursor()

    def create(self, nome_filme: str, nota_filme: float, genero_filme: str):
        comando = f'INSERT INTO filmes (nome_filme, nota_filme, genero_filme) VALUES ("{nome_filme}", {nota_filme}, "{genero_filme}")'
        self.cursor.execute(comando)
        self.conexao.commit()

    def read(self):
        comando = f'SELECT * FROM filmes'
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        print(resultado)

    def update(self, id_filme, nome_filme: str, nota_filme: float, genero_filme: str):
        comando = f'UPDATE filmes SET nome_filme = "{nome_filme}", nota_filme = "{nota_filme}", genero_filme = "{genero_filme}" WHERE idFilmes = "{id_filme}"'
        self.cursor.execute(comando)
        self.conexao.commit()

    def delete(self, id_filme):
        comando = f'DELETE FROM filmes WHERE idFilmes = "{id_filme}"'
        self.cursor.execute(comando)
        self.conexao.commit()

        self.cursor.close()
        self.conexao.close()
