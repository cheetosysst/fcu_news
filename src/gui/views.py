from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import os.path as path
from tools.soup import soup
from pprint import pprint

soup = soup()

class Ui(QtWidgets.QMainWindow):
	def __init__(self, debug=False):
		super(Ui, self).__init__() 
		uic.loadUi(path.join(path.dirname(path.abspath(__file__)),'ui','main.ui'), self)
		self.show()
		self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
		self.tabs = self.tab.findChildren(QtWidgets.QListView)
		self.pageData = []

		for t in range(4):
			print("[views] updating tab#",t)
			model = QStandardItemModel()
			self.pageData = self.updateContent(t)
			for i in self.pageData:
				model.appendRow(QStandardItem(i["title"]))
			self.tabs[t].setModel(model)
			self.tabs[t].setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
			self.tabs[t].clicked.connect(self.clicked)

	def clicked(self,qModelIndex):
		QtWidgets.QMessageBox.information(self,'ListWidget'," ".join(soup.getContent(self.pageData[qModelIndex.row()]["url"]).split("\t")))

	def updateContent(self, page, pageNum=1):
		self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
		self.tabs = self.tab.findChildren(QtWidgets.QListView)

		urlList = [
			15362,
			15361,
			14980,
			15360
		]

		url = "http://news.fcu.edu.tw/wSite/lp?ctNode="+str(urlList[page])+"&mp=9000&nowPage="+str(pageNum)+"&pagesize=45"
		
		data = soup.getArticle(url)
		return data

