from qt_core import *


class CardContatos(QWidget):
    def __init__(self, contato):
        super().__init__()
        uic.loadUi('view/card_contatos.ui', self)

        self.icon.setText(contato.nome[0])
        self.nome.setText(contato.nome)
