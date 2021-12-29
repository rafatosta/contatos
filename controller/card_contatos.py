from controller.delete_dialog import DeleteDialog
from qt_core import *
from assets.color import getColor
import model.contato_dao as contato_dao


class CardContatos(QWidget):
    def __init__(self, contato, mainWindow=None):
        super().__init__()
        uic.loadUi('view/card_contatos.ui', self)

        self.contato = contato
        self.mainWindow = mainWindow

        # pega a primeira letra da string
        if contato.nome != "":
            self.icon.setText(contato.nome[0])
        self.nome.setText(contato.nome[:20] + ' '+str(contato.sobrenome))

        # determina o estilo do label
        style_sheet = f'border: filed; border-radius: 25px; background-color: {self.contato.cor};'
        self.icon.setStyleSheet(style_sheet)

        # se não tiver a referência do mainWindow, ocultar os botões de ação
        if mainWindow == None:  # lixeira
            self.fav.hide()
            self.editar_btn.hide()
            self.excluir_btn.hide()

            self.frame.setStyleSheet("")
            self.frame.setCursor(Qt.ArrowCursor)

            # evento do botão recuperar
            self.recuperar.clicked.connect(self.recuperar_contato)
        else:  # janela de contatod

            # preenche as informações sobre o contato
            self.email.setText(contato.email)
            self.telefone.setText(contato.telefone)

            # oculta o botão de restaurar
            self.rec_widget.hide()

            # valor do checkbox
            self.fav.setChecked(contato.favorito)

            # estilo do favorito
            self.fav.setStyleSheet("QCheckBox::indicator {width: 30px;height: 30px;}"
                                   "QCheckBox::indicator:checked {image: url(assets/icons/star-checked.png);}"
                                   "QCheckBox::indicator:unchecked {image: url(assets/icons/star-unchecked.png);}")

            # eventos dos botões
            self.excluir_btn.clicked.connect(self.remover)
            self.fav.toggled.connect(self.update_fav)
            self.editar_btn.clicked.connect(self.mousePressEvent)

    def remover(self):
        dlg = DeleteDialog()
        if dlg.exec():
            contato_dao.update_lixeira(self.contato.id, deletado=1)
            self.hide() 
        else:
            pass

    def update_fav(self):
        self.contato.favorito = int(self.fav.isChecked())
        contato_dao.update_favorito(self.contato.id, self.contato.favorito)
        self.mainWindow.show_contatos_page()

    def mousePressEvent(self, event):
        if self.mainWindow != None:
            self.mainWindow.show_criar_contatos(self.contato)

    def recuperar_contato(self):
        contato_dao.update_lixeira(self.contato.id, deletado=0)
        self.hide() 
