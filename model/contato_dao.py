from model import database

lista = []


def insert(contato):  # insere
    try:
        conn = database.connect()  # conecta
        cursor = conn.cursor()  # se move no banco
        sql = """INSERT INTO Contatos (nome,sobrenome,empresa,cargo,email,telefone,obs,favorito) 
            VALUES (?,?,?,?,?,?,?,?);"""
        cursor.execute(sql, contato.getContato())
        conn.commit()
    except Exception as e:
        print('Deu erro!!!')
        print(e)
    finally:
        conn.close()


def update(contato):  # atualiza
    pass


def delete(id):  # deleta
    pass


def selectAll():  # pega todos
    #lista = []
    # acesso ao banco de dados
    ##
    ###
    return lista
