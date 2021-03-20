#! /usr/bin/python3
# -*- coding: utf-8 -*-
#

import sys
from math import *
from random import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Application(QApplication):
	def __init__(self, argv):
		super().__init__(argv)
		self.initUI()

	def initUI(self):
		self.setFont(QFont("Arial",14))
		self.setStyle(QStyleFactory.create('fusion'))
		p = self.palette()
		p.setColor(QPalette.Window, QColor(53,53,53))
		p.setColor(QPalette.Button, QColor(53,53,53))
		p.setColor(QPalette.Highlight, QColor(142,45,197))
		p.setColor(QPalette.ButtonText, QColor(255,255,255))
		p.setColor(QPalette.WindowText, QColor(255,255,255))
		self.setPalette(p)

class RenderArea(QWidget):
	def __init__(self):
		super().__init__()
		# self.initUI()
		self.paintEvent()
		self.texturesPerso()



	def paintEvent(self,event):
		#création d'un rectange pour les textures
		self.perso=QRect(0,0,50,50)
		painter = QPainter(self)
		painter.setPen(Qt.white)
		self.creationMap(painter)
"""revoir le prog car 4 types de personnages dispo"""
	def texturesPerso(self):
		#texture du perso
		self.perso1=QImage("perso1.png")
		self.perso2=QImage("perso2.png")
		self.perso3=QImage("perso3.png")
		self.perso4=QImage("perso4.png")

		def creationPerso(self,painter):
                    """RECUPERE LES DONNER DU CLAVIER ET DISONS QUE:
                            'z'= haut
                            's'= bas
                            'q'= gauche
                            'd'=droite
                            le truc qui appuit = action
                            pas oublier un if le deplacement possible, faire le deplacement"""
                    key = event.key()
                    if (key == Qt.Key_Z):
                        self.perso=self.perso1
                        c=QPoint(0,-50)
                        self.perso.moveTo(c)
                    if (key == Qt.Key_S):
                        self.perso=self.perso2
                        c=QPoint(0,50)
                        self.perso.moveTo(c)
                    if (key == Qt.Key_Q):
                        self.perso=self.perso3
                        c=QPoint(-50,0)
                        self.perso.moveTo(c)
                    if (key == Qt.Key_D):
                        self.perso=self.perso4
                        c=QPoint(50,0)
                        self.perso.moveTo(c)
                        
                        
                        


class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def closeEvent(self,event):
		QCoreApplication.instance().quit()

	def initUI(self):
		self.setWindow()
		self.setCenter()
		self.setRenderArea()
		self.show()

	def setCenter(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def setRenderArea(self):
		self.renderArea = RenderArea()
		self.setCentralWidget(self.renderArea)

	def setWindow(self):
		width = QDesktopWidget().availableGeometry().width()/2
		height = QDesktopWidget().availableGeometry().height()/2
		self.setGeometry(10, 10, width, height)
		self.setWindowTitle("Dessin sous Qt")
		self.statusBar().showMessage("Aucun événement")


app = Application([])
win = Window()
app.exec_()

