from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import os.path as path
from tools.soup import soup
from pprint import pprint

soup = soup()
url = "http://news.fcu.edu.tw/wSite/lp?ctNode=14980&mp=9000&nowPage=1&pagesize=45"

class Ui(QtWidgets.QMainWindow):
	def __init__(self, debug=False):
		super(Ui, self).__init__() 
		uic.loadUi(path.join(path.dirname(path.abspath(__file__)),'ui','main.ui'), self)
		self.show()
		self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
		self.tabs = self.tab.findChildren(QtWidgets.QListView)

		print("[views] updating tab#3")
		model = QStandardItemModel()
		for i in self.updateContent(0):
			model.appendRow(QStandardItem(i["title"]))
			print(i["title"])
		self.tabs[3].setModel(model)

		model = QStandardItemModel()
		for i in self.updateContent(1):
			model.appendRow(QStandardItem(i["title"]))
			print(i["title"])
		self.tabs[2].setModel(model)

		model = QStandardItemModel()
		for i in self.updateContent(2):
			model.appendRow(QStandardItem(i["title"]))
			print(i["title"])
		self.tabs[1].setModel(model)

		model = QStandardItemModel()
		for i in self.updateContent(3):
			model.appendRow(QStandardItem(i["title"]))
			print(i["title"])
		self.tabs[0].setModel(model)
		

		# for i in self.tabs:
		# 	# for page in range(4):
		# 	# 	data = self.updateContent(page)
		# 	model = QStandardItemModel()
		# 	model.appendRow(QStandardItem('item'))
		# 	i.setModel(model)

	def updateContent(self, page, pageNum=1):
		self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
		self.tabs = self.tab.findChildren(QtWidgets.QListView)

		urlList = [
			15360,
			14980,
			15361,
			15362
		]
		url = "http://news.fcu.edu.tw/wSite/lp?ctNode="+str(urlList[page])+"&mp=9000&nowPage="+str(pageNum)+"&pagesize=45"
		
		data = soup.getArticle(url)
		return data

