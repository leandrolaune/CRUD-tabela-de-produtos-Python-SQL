# Descrição
Construído a partir da integração do Python com o MySQL, esse projeto engloba um menu de opções em python onde o usuário poderá registrar produtos, lista-los, edita-los e deleta-los, as modificações são automaticamente registradas em uma tabela no banco de dados MySQL e ficam simultaneamente disponíveis para a visualização no terminal. O DDL para construção do banco de dados MySQL está no arquivo dentro desse repositório, chamado: "DDL SQL"
# Description
Built from the integration of Python with MySQL, this project includes a menu of options in Python where the user can register products, list them, edit and delete them, modifications are automatically recorded in a table in the database. MySQL data and are simultaneously available for viewing in the terminal. The DDL for building the MySQL database is in the file within this repository, called: "DDL SQL"
### Importando Bibliotecas
### Importing Libraries

```
import os
import mysql.connector
```

### Criando o Menu
### Creating the Menu

```
print(' ____________________________________')
print("│Digite (1) para registrar um produto│")
print("│Digite (2) para listar os produto   │")
print("│Digite (3) para editar valores      │")
print("│Digite (4) para editar estoque      │")
print("│Digite (5) para deletar um produto  │")
print('|____________________________________│')
opcao = int(input())
os.system('cls' if os.name == 'nt' else 'clear')
```

### Estabelecendo Conexão com o MySQL
### Establishing Connection to MySQL

```
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='CRUD_PythonSQL_',
)
```

### Definindo Resposta para Número Inválido no Menu
### Setting Response to Invalid Number in Menu

```
cursor = conexao.cursor()
while opcao != 7:
    if opcao < 1 or opcao > 6:
        print("Opção inválida! Digite novamente:")
        opcao = int(input())
    else:
```

### Criar Produto
### Create Product

```
        if opcao == 1:
            nome_produto = input("Digite o nome do produto: ")
            valor = float(input("Digite o valor do produto: "))
            estoque = int(input
                          ("Digite a quantidade desse produto no estoque: "))

            comando = f'INSERT INTO vendas (nome_produto, valor, estoque) VALUES ("{nome_produto}","{valor}","{estoque}")'
            cursor.execute(comando)
            conexao.commit()
            print("Produto registrado com sucesso!")
```

### Ler Produtos Ordenados por Ordem Alfabética
### Read Products Sorted in Alphabetical Order

```
        elif opcao == 2:
            comando = f'SELECT*FROM vendas ORDER BY nome_produto'
            cursor.execute(comando)
            resultado = cursor.fetchall()
            print(resultado)
```


### Editar Valor do produto
### Edit Product value

```
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
```

### Editar Quantidade de Estoque do Produto
### Edit Product Stock Quantity

```
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
```

### Deletar Produto
### Delete Product

```
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
```

### Finalizando Código
### Finalizing Code

```
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
```
