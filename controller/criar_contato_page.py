from model.contato import Contatos
import model.contato_dao as contato_dao
from assets.color import getColor
from qt_core import *


class CriarContatoPage(QWidget):
    def __init__(self, mainWindow, contato=None):
        super().__init__()
        uic.loadUi('view/criar_contato_page.ui', self)
        # referencia da janela princial
        self.mainWindow = mainWindow
        self.contato = contato
        if contato != False:
            self.carrega_contato()

        self.fechar.clicked.connect(self.fechar_page)
        self.salvar.clicked.connect(self.salvar_contato)

        # estilo do favorito
        self.fav.setStyleSheet("QCheckBox::indicator {width: 30px;height: 30px;}"
                               "QCheckBox::indicator:checked {image: url(assets/icons/star-checked.png);}"
                               "QCheckBox::indicator:unchecked {image: url(assets/icons/star-unchecked.png);}")

    def fechar_page(self):
        self.mainWindow.painel.setCurrentIndex(0)

    def carrega_contato(self):
        self.nome_label.setText(
            self.contato.nome + " " + self.contato.sobrenome)
        self.nome.setText(self.contato.nome)
        self.sobrenome.setText(self.contato.sobrenome)
        self.email.setText(self.contato.email)
        self.empresa.setText(self.contato.emp)
        self.cargo.setText(self.contato.cargo)
        self.telefone.setText(self.contato.telefone)
        self.obs.setText(self.contato.obs)
        self.fav.setChecked(self.contato.favorito)

        # determina o estilo do label
        cor = getColor()  # gera uma cor aleatória
        style_sheet = f'border: filed; border-radius: 50px; background-color: {cor};'
        self.img.setStyleSheet(style_sheet)
        if self.contato.nome != "":
            self.img.setText(self.contato.nome[0])

    def salvar_contato(self):
        nome = self.nome.text()
        sobrenome = self.sobrenome.text()
        emp = self.empresa.text()
        cargo = self.cargo.text()
        email = self.email.text()
        telefone = self.telefone.text()
        obs = self.obs.text()
        fav = int(self.fav.isChecked())

        if self.contato != False:  # edição
            contato_editado = Contatos(self.contato.id, nome, sobrenome, emp,
                                       cargo, email, telefone, obs, fav)
            contato_dao.update(contato_editado)
        else:  # criação
            # cria novo objeto contatos
            contato_novo = Contatos(None, nome, sobrenome, emp,
                                    cargo, email, telefone, obs, fav)
            # insere no banco de dados
            contato_dao.insert(contato_novo)

        # carrega os dados no mainwindow
        self.mainWindow.show_contatos_page()
