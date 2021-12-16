from qt_core import *
from controller.contatos_page import ContatosPage
from controller.criar_contato_page import CriarContatoPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)
        
        #insere a pág. de contatos na posição zero
        self.painel.insertWidget(0, ContatosPage())
    
        #evento do botão
        self.criar_contato.clicked.connect(self.show_criar_contatos)
    
    def show_criar_contatos(self):
        self.painel.insertWidget(1, CriarContatoPage(self)) # self -> a própria classe
        self.painel.setCurrentIndex(1)
    
    def show_contatos_page(self):
        self.painel.insertWidget(0, ContatosPage())
        self.painel.setCurrentIndex(0)
