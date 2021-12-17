class Contatos():
    def __init__(self, id, nome, sobrenome, emp, cargo, email, telefone, obs, favorito):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.emp = emp
        self.cargo = cargo
        self.email = email
        self.telefone = telefone
        self.obs = obs
        self.favorito = favorito

    def getContato(self):
        return [self.nome, self.sobrenome, self.emp, self.cargo, self.email,
                self.telefone, self.obs, self.favorito]
