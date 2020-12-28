from PIL import Image
import easygui
from PyQt5 import QtCore, QtGui, QtWidgets
from mainwindow import Ui_MainWindow
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
global file_name
file_name = None

def open_file():
	global file_name
	file_name = easygui.fileopenbox(msg = 'Select image file')

ui.pushButton_3.clicked.connect(open_file)

def to_png():
	global file_name
	if file_name:
		save_name = easygui.filesavebox(msg='Save png image')
		img = Image.open(file_name)
		img = img.convert('RGBA')
		img.save(save_name+".png", "png")

ui.pushButton.clicked.connect(to_png)

def to_jpg():
	global file_name
	if file_name:
		save_name = easygui.filesavebox(msg='Save jpg image')
		img = Image.open(file_name)
		img = img.convert('RGB')
		img.save(save_name+".jpg", "jpeg")

ui.pushButton_2.clicked.connect(to_jpg)

def to_bmp():
	global file_name
	if file_name:
		save_name = easygui.filesavebox(msg='Save bmp image')
		img = Image.open(file_name)
		img.save(save_name+".bmp", "bmp")

ui.pushButton_4.clicked.connect(to_bmp)

def to_tiff():
	global file_name
	if file_name:
		save_name = easygui.filesavebox(msg='Save tiff image')
		img = Image.open(file_name)
		img.save(save_name+".tiff", "tiff")

ui.pushButton_5.clicked.connect(to_tiff)

sys.exit(app.exec_())