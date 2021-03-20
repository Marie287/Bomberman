#! /usr/bin/python3

import sys
from math import *
from time import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random

class RenderArea(QWidget):
    def __init__(self, parent=None):
      super(RenderArea,self).__init__(parent)
      self.initUI()

    def initUI(self):
      self.block = QImage("images/image.png")
      self.rien = QImage("images/fondtransparent.png")
      self.incassable=QImage("images/wall.png")
      self.player1=QImage("images/Dperso1.png")
      self.player2=QImage("images/Jperso1.png")
      self.player3=QImage("images/Mperso1.png")
      self.player4=QImage("images/Cperso1.png")
      self.bomb1=QImage("images/Dbomb.png")
      self.bomb2=QImage("images/Jbomb.png")
      self.bomb3=QImage("images/Mbomb.png")
      self.bomb4=QImage("images/Cbomb.png")
      self.explosion=QImage("images/explosion0.png")

      self.block=QImage("images/block.png")
      self.block2=QImage("images/block2.png")
      self.block3=QImage("images/block3.png")
      self.block4=QImage("images/block4.png")
      self.block101=QImage("images/block101.png")
      self.block102=QImage("images/block102.png")
      self.block301=QImage("images/block301.png")
      self.block302=QImage("images/block302.png")

      self.cage=QImage("images/cage2.png")
      self.sqlt=QImage("images/sqlt2.png")
      self.cassable=QImage("images/cassable.png")
      self.coffre=QImage("images/coffre.png")

      self.timerBomb = QTimer()
      self.timerBomb2 = QTimer()
      self.timerBomb3 = QTimer()
      self.timerIA=QTimer()
      self.timerExplosion = QTimer()

      #Images PERSONNAGE 1
      self.DFace=QImage("images/DPerso1Face.png")
      self.DArriere=QImage("images/DPerso1Arriere.png")
      self.DGauche=QImage("images/DPerso1Gauche.png")
      self.DDroite=QImage("images/DPerso1Droite.png")

      #Images PERSONNAGE 2
      self.JFace=QImage("images/JPerso2Face.png")
      self.JArriere=QImage("images/JPerso2Arriere.png")
      self.JDroite=QImage("images/JPerso2Droite.png")
      self.JGauche=QImage("images/JPerso2Gauche.png")      

      #Images IA
      self.MFace=QImage("images/mbS.png")
      self.MArriere=QImage("images/mbZ.png")
      self.MGauche=QImage("images/mbQ.png")
      self.MDroite=QImage("images/mbD.png")
      self.MBombe=QImage("images/Mbomb.png")


      self.matrice =[[321,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123],
          [123,101,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,102,123],
					[123,4,5,0,0,12,12,12,12,12,12,12,12,12,12,12,12,12,0,0,16,2,123],
					[123,4,0,6,12,6,12,6,12,6,13,6,12,6,12,6,12,6,12,6,0,2,123],
					[123,4,0,12,12,12,12,12,12,12,12,12,12,12,12,15,12,15,12,12,0,2,123],
					[123,4,12,6,13,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,2,123],
					[123,4,12,12,14,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,2,123],
					[123,4,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,2,123],
					[123,4,12,12,12,12,12,12,14,12,13,12,14,12,12,12,12,12,12,12,12,2,123],
					[123,4,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,2,123],
					[123,4,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,12,2,123],
					[123,4,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,6,12,2,123],
					[123,4,12,12,12,12,13,12,14,12,12,12,12,12,12,12,14,12,12,12,0,2,123],
					[123,4,0,6,12,6,12,6,12,6,12,6,12,6,15,6,12,6,12,6,0,2,123],
					[123,4,0,0,0,12,12,12,12,12,12,12,12,12,12,12,12,12,0,0,9,2,123],
					[123,302,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,301,123],
          [123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,123]]

        
      self.positionXP1, self.positionYP1 = 0, 0   #Perso 1
      self.positionXP2, self.positionYP2 = 0, 0   #Perso 2
      self.positionXIA, self.positionYIA = 0, 0   # IA

      # Récupérer la position du personnage
      for i in range(0,len(self.matrice)):
        for n in range(0,len(self.matrice[i])):
          j=self.matrice[i][n]
          if j==5:          # Méthode recherche des coordonnées de la position du PERSONNAGE 1
            self.positionXP1 = n
            self.positionYP1= i
          elif j==9:        # Méthode recherche des coordonnées de la position du PERSONNAGE 2
            self.positionXP2 = n
            self.positionYP2= i
          elif j==16:       # Méthode recherche des coordonnées de la position du PERSONNAGE IA
            self.positionXIA = n
            self.positionYIA= i

      self.bomb1PositionX, self.bomb1PositionY = 0, 0
      self.bomb2PositionX, self.bomb2PositionY = 0, 0
      self.bomb3PositionX, self.bomb3PositionY = 0, 0


    # Recherche des coordonnées de la position de la bombe
    def bomb_position(self,x):
      if(x == 1):   # bombe du personnage 1
        num = 7
      elif(x == 2): # bombe du personnage 2
        num = 11
      elif(x == 3): # bombe du personnage IA
        num = 18
      for i in range(0,len(self.matrice)):
        for n in range(0,len(self.matrice[i])):
          j=self.matrice[i][n]
          if j == num:
            self.bomb1PositionX = n
            self.bomb1PositionY= i


    #Création d'un rectangle qui est indispensable pour l'utilisation de la méthode drawImage
    def setOriginalFigure(self):
      r1 = QRect(0,0,50,50)
      return r1


    #DESSIN DE LA MAP
    def paintEvent(self, event):
      #Création de la map
      painter = QPainter(self)
      original = self.setOriginalFigure()

      x=100
      y=33
      for i in range(0,len(self.matrice)):
        for n in range(0,len(self.matrice[i])):
          j=self.matrice[i][n]
          original.setRect(x,y,50,50)
          if j == 0:    #Bloc vide
            painter.drawImage(original,self.rien)
            
          elif j == 1: #Bloc contour
            painter.drawImage(original,self.block)

          elif j == 2: #Bloc contour à droite
            painter.drawImage(original,self.block2)

          elif j == 3: #Bloc contour en bas
            painter.drawImage(original,self.block3)

          elif j == 4: #Bloc contour à gauche
            painter.drawImage(original,self.block4)

          elif j == 101: #Bloc contour coin en haut a gauche
            painter.drawImage(original,self.block101)

          elif j == 102: #Bloc contour coin en haut droite
            painter.drawImage(original,self.block102)

          elif j == 301: #Bloc contour coin en bas a droite
            painter.drawImage(original,self.block301)

          elif j == 302: #Bloc contour coin en bas a gauche
            painter.drawImage(original,self.block302)

          elif j == 6: #Bloc incassable
            painter.drawImage(original,self.incassable)

          elif j == 5:    #Joueur 1 Face
            painter.drawImage(original,self.player1)
            
          elif j == 55:    #Joueur 1 Arriere
            painter.drawImage(original,self.DArriere)

          elif j == 555:    #Joueur 1 Gauche
            painter.drawImage(original,self.DGauche)

          elif j == 5555:    #Joueur 1 Droite
            painter.drawImage(original,self.DDroite)

          elif j == 7:    #Bombe Joueur 1
            painter.drawImage(original,self.bomb1)

          elif j == 8:    #Joueur1 FACE avec bombe derrière
            painter.drawImage(original,self.bomb1)
            painter.drawImage(original,self.player1)

          elif j == 88:    #Joueur1 ARRIERE avec bombe derrière
            painter.drawImage(original,self.bomb1)
            painter.drawImage(original,self.DArriere)

          elif j == 888:    #Joueur1 GAUCHE avec bombe derrière
            painter.drawImage(original,self.bomb1)
            painter.drawImage(original,self.DGauche)

          elif j == 8888:    #Joueur1 DROITE avec bombe derrière
            painter.drawImage(original,self.bomb1)
            painter.drawImage(original,self.DDroite)

          elif j == 9:    #Joueur 2 FACE
            painter.drawImage(original,self.player2)
            
          elif j == 99:    #Joueur 2 ARRIERE
            painter.drawImage(original,self.JArriere)

          elif j == 999:    #Joueur 2 GAUCHE
            painter.drawImage(original,self.JGauche)

          elif j == 9999:    #Joueur 2 DROITE
            painter.drawImage(original,self.JDroite)

          elif j == 10:    #Joueur 2 FACE avec bombe derrière
            painter.drawImage(original,self.bomb2)
            painter.drawImage(original,self.player2)

          elif j == 1010:    #Joueur2 ARRIERE avec bombe derrière
            painter.drawImage(original,self.bomb2)
            painter.drawImage(original,self.JArriere)

          elif j == 101010:    #Joueur 2 GAUCHE avec bombe derrière
            painter.drawImage(original,self.bomb2)
            painter.drawImage(original,self.JGauche)

          elif j == 10101010:    #Joueur2 DROITE avec bombe derrière
            painter.drawImage(original,self.bomb2)
            painter.drawImage(original,self.JDroite)

          elif j == 11:    #Bombe Joueur 2
            painter.drawImage(original,self.bomb2)

          elif j == 12:    #Bloc cassable
            painter.drawImage(original,self.cassable)

          elif j == 13:    #Bloc coffre
            painter.drawImage(original,self.coffre)

          elif j == 14:    #Bloc squelette
            painter.drawImage(original,self.sqlt)

          elif j == 15:    #Bloc cage
            painter.drawImage(original,self.cage)

          elif j == 16:    #IA FACE
            painter.drawImage(original,self.MFace)

          elif j == 1616:    #IA ARRIERE
            painter.drawImage(original,self.MArriere)

          elif j == 161616:    #IA GAUCHE
            painter.drawImage(original,self.MGauche)

          elif j == 16161616:    #IA DROITE
            painter.drawImage(original,self.MDroite)

          elif j == 18:    #IA BOMBE
            painter.drawImage(original,self.MBombe)

          elif j == 17:    #IA BOMBE + PERSO FACE
            painter.drawImage(original,self.MBombe)
            painter.drawImage(original,self.MFace)

          elif j == 1717:    #IA BOMBE + PERSO ARRIERE
            painter.drawImage(original,self.MBombe)
            painter.drawImage(original,self.MArriere)

          elif j == 171717:    #IA BOMBE + PERSO GAUCHE
            painter.drawImage(original,self.MBombe)
            painter.drawImage(original,self.MGauche)

          elif j == 17171717:    #IA BOMBE + PERSO DROITE
            painter.drawImage(original,self.MBombe)
            painter.drawImage(original,self.MDroite)

          x+=50
        x=100
        y+=50