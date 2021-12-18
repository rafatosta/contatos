from qt_core import *
from controller.main_window import MainWindow

os.environ['XDG_SESSION_TYPE'] = 'Wayland'

app = QApplication(sys.argv)
app.setWindowIcon(QIcon('assets/icons/contatos.png'))
win = MainWindow()
win.show()
sys.exit(app.exec())