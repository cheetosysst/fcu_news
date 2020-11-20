from gui.views import Ui
from PyQt5 import QtWidgets, uic
import sys


app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
exit()
# pprint(soup.getArticle(url))

