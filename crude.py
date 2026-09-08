import time
import mysql.connector

# CONEXÃO COM O BANCO DE DADOS


def conectar():
    return mysql.connector.connect(
        host='...',
        user='...',
        password='...',
        database='...'
    )

# FUNÇÕES CRUD

def criar_produto():
    """Create - Insere um novo produto na tabela vendas."""
    print("\n" + "=" * 45)
    print("CADASTRAR PRODUTO")
    print("=" * 45)

    nome_produto = input("Nome do produto: ").strip()
    try:
        valor = float(input("Valor do produto: R$ "))
    except ValueError:
        print("Valor inválido. Operação cancelada.")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        comando = "INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)"
        cursor.execute(comando, (nome_produto, valor))
        conexao.commit()
        print(f"\nProduto '{nome_produto}' cadastrado com sucesso!")
    except mysql.connector.Error as erro:
        print(f"\nErro ao cadastrar produto: {erro}")
    finally:
        cursor.close()
        conexao.close()

    time.sleep(1.5)


def listar_produtos():
    """Read - Consulta e exibe todos os produtos da tabela vendas."""
    print("\n" + "=" * 45)
    print("LISTA DE PRODUTOS")
    print("=" * 45)

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        comando = "SELECT * FROM vendas"
        cursor.execute(comando)
        resultado = cursor.fetchall()

        if not resultado:
            print("Nenhum produto cadastrado.")
        else:
            print(f"{'ID':<6}{'Produto':<25}{'Valor':>10}")
            print("-" * 45)
            for linha in resultado:
                id_venda, nome_produto, valor = linha
                print(f"{id_venda:<6}{nome_produto:<25}R$ {valor:>7.2f}")
    except mysql.connector.Error as erro:
        print(f"\nErro ao consultar produtos: {erro}")
    finally:
        cursor.close()
        conexao.close()

    time.sleep(1.5)


def atualizar_produto():
    """Update - Atualiza o valor de um produto existente."""
    print("\n" + "=" * 45)
    print("ATUALIZAR PRODUTO")
    print("=" * 45)

    nome_produto = input("Nome do produto a atualizar: ").strip()
    try:
        novo_valor = float(input("Novo valor: R$ "))
    except ValueError:
        print("Valor inválido. Operação cancelada.")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        comando = "UPDATE vendas SET valor = %s WHERE nome_produto = %s"
        cursor.execute(comando, (novo_valor, nome_produto))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"\nProduto '{nome_produto}' atualizado com sucesso!")
        else:
            print(f"\nNenhum produto encontrado com o nome '{nome_produto}'.")
    except mysql.connector.Error as erro:
        print(f"\nErro ao atualizar produto: {erro}")
    finally:
        cursor.close()
        conexao.close()

    time.sleep(1.5)


def deletar_produto():
    """Delete - Remove um produto da tabela vendas pelo ID."""
    print("\n" + "=" * 45)
    print("DELETAR PRODUTO")
    print("=" * 45)

    try:
        id_produto = int(input("ID do produto a deletar: "))
    except ValueError:
        print("ID inválido. Operação cancelada.")
        return

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        comando = "DELETE FROM vendas WHERE idVendas = %s"
        cursor.execute(comando, (id_produto,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"\nProduto de ID {id_produto} deletado com sucesso!")
        else:
            print(f"\nNenhum produto encontrado com o ID {id_produto}.")
    except mysql.connector.Error as erro:
        print(f"\nErro ao deletar produto: {erro}")
    finally:
        cursor.close()
        conexao.close()

    time.sleep(1.5)

# MENU PRINCIPAL

def exibir_menu():
    """Exibe o menu estilizado de opções."""
    print("\n" + "=" * 45)
    print("SISTEMA DE GERENCIAMENTO DE VENDAS")
    print("=" * 45)
    print(" [1] Cadastrar produto (Create)")
    print(" [2] Listar produtos   (Read)")
    print(" [3] Atualizar produto (Update)")
    print(" [4] Deletar produto   (Delete)")
    print(" [0] Sair")
    print("=" * 45)


def main():
    """Loop principal do programa."""
    while True:
        exibir_menu()
        opcao = input("Escolha um número: ").strip()

        if opcao == "1":
            criar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "0":
            print("\nEncerrando o sistema... até logo!")
            time.sleep(1)
            break
        else:
            print("\nOpção inválida. Tente novamente.")
            time.sleep(1)


if __name__ == "__main__":
    main()