from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QStandardItem, QStandardItemModel
import sys
import os.path as path

class Ui(QtWidgets.QMainWindow):
	def __init__(self, debug=False):
		# print(path.join(path.dirname(path.abspath(__file__)),'ui','main.ui'))
		super(Ui, self).__init__() # Call the inherited classes __init__ method
		uic.loadUi(path.join(path.dirname(path.abspath(__file__)),'ui','main.ui'), self) # Load the .ui file
		self.show() # Show the GUI
		self.tab = self.findChild(QtWidgets.QTabWidget, 'tabWidget')
		self.tabs = self.tab.findChildren(QtWidgets.QListView)
		for i in self.tabs:
			model = QStandardItemModel()
			item = QStandardItem('item')
			model.appendRow(item)
			i.setModel(model)
		# print(self.title)

	def updateContent(self, page):
		print()

