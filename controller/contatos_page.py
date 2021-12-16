from controller.card_contatos import CardContatos
from qt_core import *
import model.contato_dao as contato_dao


class ContatosPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/contatos_page.ui', self)

        self.load()

    def load(self):
        lista = contato_dao.selectAll()
        for c in lista:
            self.painel_contatos.addWidget(CardContatos(c))

        # atualizar a contagem
        self.label_contatos.setText(f'Contatos ({len(lista)})')
