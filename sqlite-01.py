import sqlite3
from contato import Contato

#------------------------------------------------------------------------------
# Inicializa a conexão com o banco de dados
# con = sqlite3.connect("banco-de-dados.sqlite")
con = sqlite3.connect(":memory:")


#------------------------------------------------------------------------------
# Cursor para executar os comandos SQL
cursor = con.cursor()


#------------------------------------------------------------------------------
# Se existir, apaga permanentemente a tabela "tb_contatos" (não precisa de commit)
# cursor.execute("DROP TABLE IF EXISTS tb_contatos;")


#------------------------------------------------------------------------------
# Cria a tabela "tb_contatos"
cursor.execute("""
        CREATE TABLE tb_contatos (
                                id INTEGER PRIMARY KEY,
                                nome TEXT,
                                telefone TEXT,
                                cidade TEXT
                                );
                            """)
con.commit()


#------------------------------------------------------------------------------
# Insere os valores da lista "contatos" na tabela "tb_contatos" usando qmarks
contatos = [
    ("Everton", "99999-9999", "Blumenau"),
    ("Priscila", "88888-8888", "São João"),
    ("Maria", "98888-7777", "Brusque")
]
cursor.executemany("INSERT INTO tb_contatos (nome, telefone, cidade) VALUES (?, ?, ?);", contatos)
con.commit()


# cursor.execute("SELECT * FROM tb_contatos;")
cursor.execute("SELECT * FROM tb_contatos WHERE cidade='Blumenau';")
pessoas = cursor.fetchall()

contatos = [Contato(pessoa[1], pessoa[2], pessoa[3]) for pessoa in pessoas]
for contato in contatos:
    print(contato)


#------------------------------------------------------------------------------
# Antes de encerrar, termina a conexão com o bando de dados
con.close()
