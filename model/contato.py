from assets.color import getColor


class Contatos():
    # obs-> atribuir um valor a uma variável no init é o mesmo que informar o seu valor padrão em caso de não existência
    def __init__(self, id, nome, sobrenome, emp, cargo, email, telefone, obs, favorito, deletado=0):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.emp = emp
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.obs = obs
        self.favorito = favorito
        self.deletado = deletado

        self.cor = getColor()

    def get_dados_lista(self):
        lista_dados = [self.nome, self.sobrenome, self.emp, self.cargo, self.email,
                       self.telefone, self.obs, self.favorito]
        return lista_dados
