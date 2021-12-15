from qt_core import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('view/main_window.ui', self)