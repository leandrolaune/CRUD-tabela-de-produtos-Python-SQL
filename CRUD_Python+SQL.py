import os
import mysql.connector

print(' ____________________________________')
print("│Digite (1) para registrar um produto│")
print("│Digite (2) para listar os produto   │")
print("│Digite (3) para editar valores      │")
print("│Digite (4) para editar estoque      │")
print("│Digite (5) para deletar um produto  │")
print('|____________________________________│')
opcao = int(input())
os.system('cls' if os.name == 'nt' else 'clear')

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='CRUD_PythonSQL_',
)

cursor = conexao.cursor()
while opcao != 7:
    if opcao < 1 or opcao > 6:
        print("Opção inválida! Digite novamente:")
        opcao = int(input())
    else:
        # CRUD
        # comando = ''
        # cursor.execute(comando)
        # conexao.commit  # edita o banco de dados
        # resultado = cursor.fetchall  # lê o banco de dados

        # create
        if opcao == 1:
            nome_produto = input("Digite o nome do produto: ")
            valor = float(input("Digite o valor do produto: "))
            estoque = int(input
                          ("Digite a quantidade desse produto no estoque: "))

            comando = f'INSERT INTO vendas (nome_produto, valor, estoque) VALUES ("{nome_produto}","{valor}","{estoque}")'
            cursor.execute(comando)
            conexao.commit()
            print("Produto registrado com sucesso!")


# read
        elif opcao == 2:
            comando = f'SELECT*FROM vendas ORDER BY nome_produto'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)


# update
        elif opcao == 3:
            comando = f'SELECT*FROM vendas ORDER BY nome_produto'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)

            idvendas = int(
                input("\nDigite o número do produto que você deseja editar o valor: \n"))
            valor = float(input("\nDigite o novo valor do produto: \n"))
            comando = f' UPDATE vendas SET valor = "{valor}" WHERE idvendas = "{idvendas}"'
            print(
                "\nValor do produto editado com sucesso! Digite 2 para visualizar a lista atualizada.\n")

            cursor.execute(comando)
            conexao.commit()

# delete
        elif opcao == 4:
            comando = f'SELECT*FROM vendas ORDER BY nome_produto'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
            idvendas = int(
                input("\nDigite o número do produto que você deseja editar o estoque: \n"))
            estoque = int(input("\nDigite o novo estoque do produto: \n"))
            comando = f' UPDATE vendas SET estoque ="{estoque}" WHERE idvendas= "{idvendas}"'
            print(
                "\nEstoque do produto editado com sucesso! Digite 2 para visualizar a lista atualizada.\n")
            cursor.execute(comando)
            conexao.commit()

# bônus- editar estoque
        elif opcao == 5:
            comando = f'SELECT*FROM vendas ORDER BY nome_produto'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
            idvendas = int(
                input("\nDigite o número do produto que você deseja deletar: \n"))
            comando = f' DELETE FROM vendas WHERE idvendas = "{idvendas}"'

            print(
                "\nProduto deletado com sucesso! Digite 2 para visualizar a lista atualizada.\n")
            cursor.execute(comando)
            conexao.commit()

    print(' ____________________________________')
    print("│Digite (1) para registrar um produto│")
    print("│Digite (2) para listar os produtos  │")
    print("│Digite (3) para editar valores      │")
    print("│Digite (4) para editar estoque      │")
    print("│Digite (5) para deletar um produto  │")
    print('│____________________________________│')

    opcao = int(input())
    os.system('cls' if os.name == 'nt' else 'clear')
    cursor.close
    conexao.close
