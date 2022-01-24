from qt_core import *
from controlle.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()
window.show() 

app.exec()