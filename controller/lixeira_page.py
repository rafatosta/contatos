from qt_core import *
import model.contato_dao as contato_dao
from controller.card_contatos import CardContatos


class LixeiraPage(QWidget):
    def __init__(self,mainWindow):
        super().__init__()
        uic.loadUi('view/lixeira_page.ui', self)

        self.mainWindow = mainWindow

        self.esvaziar.clicked.connect(self.esvaziar_lixeira)

        self.load()

    def load(self):
        lista = contato_dao.selectDeletedAll()
        for contato in lista:
            self.painel.addWidget(
                CardContatos(contato))

        self.lixeira_label.setText(f'Lixeira ({len(lista)})')

    def esvaziar_lixeira(self):
        contato_dao.deleteLixeiraAll()
        self.mainWindow.show_lixeira_page()
