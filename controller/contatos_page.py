from controller.card_contatos import CardContatos
from qt_core import *
import model.contato_dao as contato_dao


class ContatosPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/contatos_page.ui', self)

        self.mainWindow = mainWindow

        self.load()

    def load(self):
        lista = contato_dao.selectAll()
        for contato in lista:
            self.painel_contatos.addWidget(
                CardContatos(contato, self.mainWindow))

        # atualizar a contagem
        self.label_contatos.setText(f'Contatos ({len(lista)})')
