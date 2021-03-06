from model import database
from model.contato import Contatos


def insert(contato):
    # insere um novo contato
    try:  # tenta executar o código
        conn = database.connect()  # conecta
        cursor = conn.cursor()  # se move no banco
        sql = """INSERT INTO Contatos (nome,sobrenome,empresa,cargo,email,telefone,obs,favorito) 
            VALUES (?,?,?,?,?,?,?,?);"""
        cursor.execute(sql, contato.get_dados_lista())
        conn.commit()  # grava os dados no banco
    except Exception as e:  # em caso de erro
        print('Deu erro!!!')
        print(e)
    finally:  # obrigatoriamente irá executar esse bloco no final
        conn.close()  # fechar a conexão


def update(contato):
    # atualiza todos os campos de um contato
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contatos SET nome=?, sobrenome=?,empresa=?,cargo=?,email=?,telefone=?,obs=?,favorito=? WHERE id=?;"""
        l = contato.get_dados_lista()
        # insere o id no final da lista para ficar igual a sequência do SQL
        l.append(contato.id)
        cursor.execute(sql, l)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def update_favorito(id, favorito):
    # favorita o contato
    # favorito = 1 -> contato é favoritado
    # favorito = 0 -> deixa de ser favorito
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contatos SET favorito=? WHERE id=?;"""
        cursor.execute(sql, [favorito, id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def update_lixeira(id, deletado):
    # atualiza contato
    # deletado = 1 -> move para lixeira
    # deletado = 0 -> remove da lixeira
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """UPDATE Contatos SET deletado=? WHERE id=?;"""
        cursor.execute(sql, [deletado, id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def delete(id):
    # deleta um contato a partir do seu id
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Contatos WHERE id = ?;"""
        cursor.execute(sql, [id])
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def deleteLixeiraAll():
    # esvazia lixeira - exclui definitivamente todos os contatos existentes na lixeira
    try:
        conn = database.connect()
        cursor = conn.cursor()
        sql = """DELETE FROM Contatos WHERE deletado=1;"""
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def selectAll():
    # pega todos contatos salvos
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        # ORDER BY -> ordenar por
        sql = """SELECT * FROM Contatos WHERE deletado = 0 ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall()  # retorna uma lista com os dados de cada contato
        for r in result:
            # exemplo de como pegar os dados retornados
            #id = r[0]
            #nome = r[1]
            novo_contato = Contatos(
                r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9])
            lista.append(novo_contato)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista


def selectDeletedAll():
    # pega todos contatos movidos para a lixeira
    lista = []
    try:
        conn = database.connect()
        cursor = conn.cursor()
        # ORDER BY -> ordenar por
        sql = """SELECT * FROM Contatos WHERE deletado = 1 ORDER BY upper(nome);"""
        cursor.execute(sql)
        result = cursor.fetchall()  # retorna uma lista com os dados de cada contato
        for r in result:
            # exemplo de como pegar os dados retornados
            #id = r[0]
            #nome = r[1]
            novo_contato = Contatos(
                r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9])
            lista.append(novo_contato)
    except Exception as e:
        print(e)
    finally:
        conn.close()
    return lista
