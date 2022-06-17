from controller import filmeController

if __name__ == "__main__":
    while True:
        print("Seja bem vindo ao banco de dados de filmes do Felipe Moreira!!! \n")
        print('1 - Adicionar filme ao banco de dados.\n')
        print('2 - Ve os filmes do banco de dados.\n')
        print('3 - Atualizar dados do filme.\n')
        print('4 - Deletar filme do banco de dados.\n')
        user_choice = input("Opção: ")

        service = filmeController()

        if user_choice == "1":
            nome_filme = input('Digite o nome do filme você quer adicionar: ')
            nota_filme = float(input('Digite a nota que você da ao filme: '))
            genero_filme = input('Digite o genero do filme: ')

            service.create(nome_filme, nota_filme, genero_filme)

        elif user_choice == "2":
            service.read()

        elif user_choice == "3":
            id_filme = input('Digite o id do filmes a ser editado: ')
            nome_filme = input('Digite o novo nome do filme: ')
            nota_filme = float(input('Digite a nova nota do filme editado: '))
            genero_filme = input('Digite o genero do filme editado: ')

            service.update(id_filme, nome_filme, nota_filme, genero_filme)

        elif user_choice == "4":
            id_filme = input('Digite o id do filme que você quer deletar: ')

            service.delete(id_filme)

        else:
            continue


# Fecha a conexão
