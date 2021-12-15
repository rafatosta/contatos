from qt_core import *
from controller.main_window import MainWindow

os.environ['XDG_SESSION_TYPE'] = 'Wayland'

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec())