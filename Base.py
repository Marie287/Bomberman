#! /usr/bin/python3

import sys
from math import *
from time import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
from RenderArea import RenderArea
from Window import Window


class Application(QApplication):
  def __init__(self, argv):
    super().__init__(argv)
    self.initUI()

  def initUI(self):
    self.setFont(QFont("Arial",14))
    self.setStyle(QStyleFactory.create('fusion'))
    p = self.palette();
    p.setColor(QPalette.Window, QColor(53,53,53))
    p.setColor(QPalette.Button, QColor(53,53,53))
    p.setColor(QPalette.Highlight, QColor(142,45,197))
    p.setColor(QPalette.ButtonText, QColor(255,255,255))
    p.setColor(QPalette.WindowText, QColor(255,255,255))
    self.setPalette(p)

#-----------------------------------------------------------------------

def main(argv):
  app = Application(argv)
  if len(argv) > 1:
    win = Window(argv[1])
  else:
    win = Window("red")
  app.exec_()

if __name__ == "__main__":
  main(sys.argv)