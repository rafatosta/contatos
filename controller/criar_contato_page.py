from model.contato import Contatos
import model.contato_dao as contato_dao
from qt_core import *


class CriarContatoPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/criar_contato_page.ui', self)
        # referencia da janela princial
        self.mainWindow = mainWindow

        self.fechar.clicked.connect(self.fechar_page)
        self.salvar.clicked.connect(self.salvar_contato)

    def fechar_page(self):
        self.mainWindow.painel.setCurrentIndex(0)

    def salvar_contato(self):
        nome = self.nome.text()
        sobrenome = self.sobrenome.text()
        emp = self.empresa.text()
        cargo = self.cargo.text()
        email = self.email.text()
        telefone = self.telefone.text()
        obs = self.obs.text()
        fav = 0
        # cria novo objeto contatos
        novo = Contatos(None, nome, sobrenome, emp,
                        cargo, email, telefone, obs, fav)

        # insere no banco de dados
        contato_dao.insert(novo)

        # carrega os dados no mainwindow
        self.mainWindow.show_contatos_page()
