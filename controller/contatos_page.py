from qt_core import *

class ContatosPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/contatos_page.ui', self)