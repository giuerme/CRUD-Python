# Importação e conexão com o banco de dados

import mysql.connector

conexao = mysql.connector.connect(
    host="...",
    user="...",
    password="...",
    database="..."
)
cursor = conexao.cursor()

# CRUD - Create, Read, Update, Delete

# Create - Inserir dados na tabela

nome_produto = "Tody"
valor = 10
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()  # Salvar as alterações no banco de dados

# Read - Consultar dados na tabela

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #consultando o banco de dados
print(resultado) #imprimindo o resultado da consulta

# Update - Atualizar dados na tabela

nome_produto = "Tody"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# Delete - Deletar dados na tabela

id_produto = 1
comando = f'DELETE FROM vendas WHERE idVendas = {id_produto}'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()