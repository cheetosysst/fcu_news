from gui.views import Ui
from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication(sys.argv)
sWidth  = app.primaryScreen().availableGeometry().width()
sHeight = app.primaryScreen().availableGeometry().height()
window = Ui(sWidth*2/3,sHeight*2/3)
app.exec_()
exit()
