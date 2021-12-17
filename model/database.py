import sqlite3


def connect(): # conexão do banco de dados
    # cria a conexão
    conn = sqlite3.connect('database/contatos.sqlite')
    return conn
