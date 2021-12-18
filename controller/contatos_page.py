from controller.card_contatos import CardContatos
from qt_core import *
import model.contato_dao as contato_dao


class ContatosPage(QWidget):
    def __init__(self, mainWindow):
        super().__init__()
        uic.loadUi('view/contatos_page.ui', self)

        self.mainWindow = mainWindow

        # inicia os favoritos oculto
        self.fav_widget.hide()

        self.load()

    def load(self):
        lista = contato_dao.selectAll()
        cont_fav = 0
        for contato in lista:
            if contato.favorito == 1:
                self.painel_fav.addWidget(
                    CardContatos(contato, self.mainWindow))
                cont_fav += 1

            self.painel_contatos.addWidget(
                CardContatos(contato, self.mainWindow))

        # mostra o widget dos favoritos
        if cont_fav > 0:
            self.fav_widget.show()

        # atualizar a contagem
        self.label_contatos.setText(f'Contatos ({len(lista)})')
        self.label_fav.setText(f'Contatos com estrela ({cont_fav})')
