from qt_core import *

class CriarContatoPage(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/criar_contato_page.ui', self)