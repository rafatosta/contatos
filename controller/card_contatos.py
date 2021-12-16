from qt_core import *
from assets.color import getColor


class CardContatos(QWidget):
    def __init__(self, contato):
        super().__init__()
        uic.loadUi('view/card_contatos.ui', self)

        # pega a primeira letra da string
        self.icon.setText(contato.nome[0])
        self.nome.setText(contato.nome + ' '+contato.sobrenome)
        self.email.setText(contato.email)
        self.telefone.setText(contato.telefone)

        # determina o estilo do label
        cor = getColor()  # gera uma cor aleatória
        style_sheet = f'border: 1px solid {cor}; border-radius: 25px; background-color: {cor};'
        self.icon.setStyleSheet(style_sheet)

        # estilo do favorito
        self.fav.setStyleSheet("QCheckBox::indicator {width: 30px;height: 30px;}"
                               "QCheckBox::indicator:checked {image: url(assets/icons/star-checked.png);}"
                               "QCheckBox::indicator:unchecked {image: url(assets/icons/star-unchecked.png);}")
        
        
