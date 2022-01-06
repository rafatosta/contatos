from controller.lixeira_page import LixeiraPage
from qt_core import *
from controller.contatos_page import ContatosPage
from controller.criar_contato_page import CriarContatoPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)

        # carrega a página inicial ao criar a janela
        self.show_contatos_page()

        # inicia a janela princial fullscreen
        #screen = QDesktopWidget().screenGeometry()
        #self.setGeometry(0, 0, screen.width(), screen.height())

        # evento do botão
        self.criar_contato.clicked.connect(self.show_criar_contatos)
        self.contatos_btn.clicked.connect(self.show_contatos_page)
        self.lixeira.clicked.connect(self.show_lixeira_page)

        #evendo da barra de pesquisa
        self.pesquisar.textEdited.connect(self.goPesquisa)


    def goPesquisa(self,texto):
        print(texto)
        print(self.painel.currentIndex())


    def show_contatos_page(self):
        self.painel.insertWidget(0, ContatosPage(self))
        self.painel.setCurrentIndex(0)

    def show_criar_contatos(self, contato=None):
        # self -> a própria classe (MainWindow)
        self.painel.insertWidget(1, CriarContatoPage(self, contato))
        self.painel.setCurrentIndex(1)
    
    def show_lixeira_page(self):
        self.painel.insertWidget(0, LixeiraPage(self))
        self.painel.setCurrentIndex(0)

    
