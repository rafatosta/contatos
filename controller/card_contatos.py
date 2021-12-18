from controller.delete_dialog import DeleteDialog
from qt_core import *
from assets.color import getColor
import model.contato_dao as contato_dao


class CardContatos(QWidget):
    def __init__(self, contato, mainWindow):
        super().__init__()
        uic.loadUi('view/card_contatos.ui', self)

        self.contato = contato
        self.mainWindow = mainWindow
        # pega a primeira letra da string
        if contato.nome != "":
            self.icon.setText(contato.nome[0])
        self.nome.setText(contato.nome + ' '+contato.sobrenome)
        self.email.setText(contato.email)
        self.telefone.setText(contato.telefone)

        # determina o estilo do label
        style_sheet = f'border: filed; border-radius: 25px; background-color: {self.contato.cor};'
        self.icon.setStyleSheet(style_sheet)

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
            # carrega os dados no mainwindow
            self.mainWindow.show_contatos_page()
        else:
            pass

    def update_fav(self):
        self.contato.favorito = int(self.fav.isChecked())
        contato_dao.update_favorito(self.contato.id, self.contato.favorito)
        self.mainWindow.show_contatos_page()

    def mousePressEvent(self, event):
        self.mainWindow.show_criar_contatos(self.contato)

    def __copy__(self):
        return self
