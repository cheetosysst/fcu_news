from tools.soup import soup
import requests as req
from pprint import pprint
from gui.views import Ui
from PyQt5 import QtWidgets, uic
import sys

soup = soup()
url = "http://news.fcu.edu.tw/wSite/lp?ctNode=14980&mp=9000&nowPage=1&pagesize=45"

app = QtWidgets.QApplication(sys.argv) # Create an instance of QtWidgets.QApplication
window = Ui() # Create an instance of our class
app.exec_() # Start the application
exit()
# pprint(soup.getArticle(url))

