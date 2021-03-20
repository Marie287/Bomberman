#! /usr/bin/python3

import sys
from math import *
from time import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
from RenderArea import RenderArea

class Window(QMainWindow):
    def __init__(self,argument):
      super().__init__()
      self.initUI(argument)

    def closeEvent(self,event):
      QCoreApplication.instance().quit()

    def setRenderArea(self):
      self.renderArea = RenderArea()
      self.setCentralWidget(self.renderArea)

    def initUI(self,argument):
      self.setWindow()
      self.setWindowTitle("GOTBERMAN")
      self.setFixedSize(1300,950) #Fixer la taille de la fenêtre
      self.setCenter() #Centrer la fenêtre sur l'écran
      self.pageaccueil() #Faire apparaitre le  Menu Principal
      self.show()
      self.position = 1 #initalisation de deux variables qui serviront par la suite à
      self.position2 = 1
      self.position3 = 1

    def setCenter(self): #Méthode qui s'occupe de centrer la fenêtre sur l'écran
      qr = self.frameGeometry()
      cp = QDesktopWidget().availableGeometry().center()
      qr.moveCenter(cp)
      self.move(qr.topLeft())

    def setWindow(self):
      width = QDesktopWidget().availableGeometry().width()/2
      height = QDesktopWidget().availableGeometry().height()/2
      self.setGeometry(10, 10, width, height)
      self.setWindowTitle("Coloriage Interactif sous Qt")

#---------------------------------------------------------------------

    def bouttonsMenu(self): #Bouttons du menu principal
      #Boutton Jouer
      self.buttonp = QPushButton('Jouer', self)
      self.buttonp.setStyleSheet('QPushButton { border: none; color: #e2fcfb; font: bold 29px;}')
      self.buttonp.setGeometry(1070,100,80,50)
      self.buttonp.setToolTip("Appuyez pour commencer")
      self.buttonp.clicked.connect(self.initGame)

      #Boutton Règles
      self.buttonr = QPushButton('Règles', self)
      self.buttonr.setStyleSheet('QPushButton { border: none; color: #e2fcfb; font: bold 29px;}')
      self.buttonr.setGeometry(1015,220,200,50)

      self.buttonr.clicked.connect(self.initRegles)

      #Boutton Quitter
      self.buttonq = QPushButton('Quitter', self)
      self.buttonq.setStyleSheet('QPushButton { border: none; color: #e2fcfb; font: bold 29px;}')
      self.buttonq.setGeometry(1015,340,200,50)
      self.buttonq.clicked.connect(self.initQuitter)

      self.setCenter()
      self.show()

    #Boutons du Menu de l'affichage des règles du jeu
    def bouttonsRegles(self):
      self.buttonre = QPushButton('Retour', self)
      self.buttonre.setStyleSheet('QPushButton { border: none; color: #e2fcfb; font: bold 29px;}')
      self.buttonre.setGeometry(1015,340,200,50)
      self.buttonre.clicked.connect(self.pageaccueil)
      self.show()

    #Affichage du Menu principal
    def pageaccueil(self):
      self.bouttonsMenu() #Faire apparaitre les bouttons
      self.fond(1)

    #Affichage du plateau de jeu (map) = début de la partie
    def initGame(self):
      self.fond(2) #Afficher un autre fond par dessus celui du menu principal
      self.setRenderArea() #Appel de la classe contenant l'affichage de la map (contenue dans un PainEvent)
      self.buttonp.setEnabled(False)
      self.buttonr.setEnabled(False) #Le bouton sera caché derrière la map, mais sera désactivé, alors il ne gênera pas
      self.buttonq.setEnabled(False)
      self.buttonp.setText(" ") #Faire disparaitre les boutons du menu
      self.buttonr.setText(" ")
      self.buttonq.setText(" ")
      self.renderArea.timerIA.timeout.connect(self.IA)
      self.renderArea.timerIA.start(1000)

    #Méthode faisant correspondant à l'affichage des règles (associée à un bouton)
    def initRegles(self):
      self.fond(3)
      self.bouttonsRegles()
      self.buttonp.setEnabled(False)
      self.buttonr.setEnabled(False)
      self.buttonq.setEnabled(False)
      self.buttonp.setText(" ")
      self.buttonr.setText(" ")
      self.buttonq.setText(" ")

    #Méthode pour quitter le jeu (associée à un boutton)
    def initQuitter(self):
      quit()

    def fond(self, f):
      if(f == 1):     #Fond d Menu principal
        oImage = QImage("images/fond1.jpg")
      elif(f == 2):   #Fond lors du lancement de la map du jeu
        oImage = QImage("images/fond2.png")
      elif(f == 3):   #Fond pour la visualisation des règles du jeu
        oImage = QImage("images/fond3.png")
      elif(f == 4):   #Fond pour la fin du jeu (mort du personnage 1)
        oImage = QImage("images/fond4.png")
      sImage = oImage.scaled(QSize(1300,950))
      palette = QPalette()
      palette.setBrush(10, QBrush(sImage))
      self.setPalette(palette)

    def aff_bomb_dessous_P1(self, x):
      self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] = x
      self.renderArea.update()

    def aff_bombe_dessous_main_P1(self):
      #Si la position actuelle est de face, arrière, ou de profil
      if self.position == 1:    #Faire afficher l'image du personnage avec celle de la bombe par dessous avec la même posiiton du personnage
        self.aff_bomb_dessous_P1(8)
      elif self.position == 11:
        self.aff_bomb_dessous_P1(88)
      elif self.position == 111:
        self.aff_bomb_dessous_P1(888)
      elif self.position == 1111:
        self.aff_bomb_dessous_P1(8888)


    def aff_bomb_dessous_P2(self, x):
      self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] = x
      self.renderArea.update()

    def aff_bombe_dessous_main_P2(self):
      if self.position2 == 1:
        self.aff_bomb_dessous_P2(10)
      if self.position2 == 11:
        self.aff_bomb_dessous_P2(1010)
      if self.position2 == 111:
        self.aff_bomb_dessous_P2(101010)
      if self.position2 == 1111:
        self.aff_bomb_dessous_P2(10101010)
            

    #Mettre une image de bombe à la place du joueur actuelle, et faire avancer le joueur
    def move_P1(self, a, b, dir, c):
      if (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] == 8) or (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] == 88) or (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] == 888) or (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] == 8888):
        # Si il n'y a pas d'image de personnage associée à une bombe à la place actuelle, remplacer la place actuelle par un bloc vide (chiffre 0 dans la matrice), et faire avancer le personnage
        self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] = a
        if(dir == "x"):
          self.renderArea.positionXP1 += c
        else:
          self.renderArea.positionYP1 += c
        self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] = b
        self.renderArea.update()
      else :
        self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] = 0
        if(dir == "x"):
          self.renderArea.positionXP1 += c
        else:
          self.renderArea.positionYP1 += c
        self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1] = b
        self.renderArea.update()
        self.renderArea.timerBomb.timeout.connect(self.replace1)
        self.renderArea.timerBomb.start(1000)
        
      
      

    def move_P2(self, a, b, dir, c):
      if (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] == 10) or (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] == 1010) or (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] == 101010) or (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] == 10101010):
        self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] = a
        if(dir == "x"):
          self.renderArea.positionXP2 += c
        else:
          self.renderArea.positionYP2 += c
        self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] = b
        self.renderArea.update()
      else: 
        self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] = 0
        if(dir == "x"):
          self.renderArea.positionXP2 += c
        else:
          self.renderArea.positionYP2 += c
        self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2] = b
        self.renderArea.update()
        self.renderArea.timerBomb2.timeout.connect(self.replace2)
        self.renderArea.timerBomb2.start(1000)


    #DEPLACEMENT DU PERSONNAGE
    def keyPressEvent(self,event):
        key = event.key()
        #Déplacement PERSONNAGE 1 1 (Z,Q,S,D)

        #ALLER A DROITE
        if (key == Qt.Key_D) and (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1+1] == 0):
          self.position = 1111
          #Si la case actuelle correspond à l'affichae simultanné du joueur et de la bombe
          self.move_P1(7, 5555, "x", 1)

        #ALLER A GAUCHE
        elif (key == Qt.Key_Q) and (self.renderArea.matrice[self.renderArea.positionYP1][self.renderArea.positionXP1-1] == 0):
          self.position =111
          self.move_P1(7, 555, "x", -1)

        #ALLER EN HAUT
        elif (key == Qt.Key_Z) and (self.renderArea.matrice[self.renderArea.positionYP1-1][self.renderArea.positionXP1] == 0):
          self.position = 11
          self.move_P1(7, 55, "y", -1)

        #ALLER EN BAS
        elif (key == Qt.Key_S) and (self.renderArea.matrice[self.renderArea.positionYP1+1][self.renderArea.positionXP1] == 0):
          self.position = 1
          self.move_P1(7, 5, "y", 1)

        #Conditions sur BOMBE PERSONNAGE 1 :
        elif (key == Qt.Key_Space):
          self.aff_bombe_dessous_main_P1()



        #Déplacement PERSONNAGE 2 (Haut,Gauche,Bas,Droite)
        #ALLER A DROITE
        if (key == Qt.Key_Right) and (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2+1] == 0):
          self.position2 = 1111
          self.move_P2(11, 9999, "x", 1)

        #ALLER A GAUCHE
        elif (key == Qt.Key_Left) and (self.renderArea.matrice[self.renderArea.positionYP2][self.renderArea.positionXP2-1] == 0):
          self.position2 = 111
          self.move_P2(11, 999, "x", -1)


        #ALLER EN HAUT
        elif (key == Qt.Key_Up) and (self.renderArea.matrice[self.renderArea.positionYP2-1][self.renderArea.positionXP2] == 0):
          self.position2 = 11
          self.move_P2(11, 99, "y", -1)

        #ALLER EN BAS
        elif (key == Qt.Key_Down) and (self.renderArea.matrice[self.renderArea.positionYP2+1][self.renderArea.positionXP2] == 0):
          self.position2 = 1
          self.move_P2(11, 9, "y", 1)

        #Conditions sur la BOMBE PERSONNAGE 2 :
        elif (key == Qt.Key_Return):
            self.aff_bombe_dessous_main_P2()

    #Méthode pour faire disparaitre l'image de la bombe DU PERSONNAGE 1 après 1 seconde (cette méthode est reliée à un Timer())
    def replace1(self):
      self.renderArea.bomb_position(1) #Faire appel à la méthode qui recherche la position de la bombe du PERSONNAGE 1 dans la matrice
      self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX] = 0 #REmplacer la position de la bombe par une case vide
      self.explosion1()
      self.renderArea.update()

    #Méthode pour faire disparaitre l'image de la bombe DU PERSONNAGE 2 après 1 seconde (cette méthode est reliée à un Timer())
    def replace2(self):
      self.renderArea.bomb_position(2) #Faire appel à la méthode qui recherche la position de la bombe du PERSONNAGE 2 dans la matrice
      self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX] = 0
      self.explosion2()
      self.renderArea.update()

    #Méthode pour faire disparaitre l'image de la bombe DU PERSONNAGE IA après 1 seconde (cette méthode est reliée à un Timer())
    def replace3(self):
      self.renderArea.bomb_position(3) #Faire appel à la méthode qui recherche la position de la bombe du PERSONNAGE IA dans la matrice
      self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX] = 0
      self.explosion3()
      self.renderArea.update()

    #Si un bloc autour de la bombe correspond à un bloc cassable, casser le bloc = rendre la case vide (chiffre 0 dans la matrice) POUR LE PERSONNAGE 1
    def explosion1(self):
      if (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] == 15) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] == 14) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] == 13) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] == 12):
        self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] = 0

      #Si le bloc à côté de la bombe correspond au joueur adverse
      elif (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX+1] == 9):
        self.fond(4) #Lancer le fond de la fin du jeu
        self.quitLabel(1) #Lancer une fenêtre qui affiche le nom du gagnant

      if (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] == 15) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] == 14) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] == 13) or (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] == 12):
        self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] = 0

      elif (self.renderArea.matrice[self.renderArea.bomb1PositionY][self.renderArea.bomb1PositionX-1] == 9):
        self.fond(4)
        self.quitLabel(1)

      if (self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] == 12):
        self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] = 0

      elif (self.renderArea.matrice[self.renderArea.bomb1PositionY+1][self.renderArea.bomb1PositionX] == 9):
        self.fond(4)
        self.quitLabel(1)

      if (self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] == 12):
        self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] = 0

      elif (self.renderArea.matrice[self.renderArea.bomb1PositionY-1][self.renderArea.bomb1PositionX] == 9):
        self.fond(4)
        self.quitLabel(1)


    #Si un bloc autour de la bombe correspond à un bloc cassable, casser le bloc = rendre la case vide (chiffre 0 dans la matrice) POUR LE PERSONNAGE 2
    def explosion2(self):
      if (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] == 15) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] == 14) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] == 13) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] == 12):
        self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX+1] == 5):
        self.fond(4)
        self.quitLabel(2)

      if (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] == 15) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] == 14) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] == 13) or (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] == 12):
        self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb2PositionY][self.renderArea.bomb2PositionX-1] == 5):
        self.fond(4)
        self.quitLabel(2)

      if (self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] == 12):
          self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb2PositionY+1][self.renderArea.bomb2PositionX] == 5):
          self.fond(4)
          self.quitLabel(2)

      if (self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] == 12):
          self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb2PositionY-1][self.renderArea.bomb2PositionX] == 5):
          self.fond(4)
          self.quitLabel(2)


    #Pareil pour l'IA:
    def explosion3(self):
      if (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 15) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 14) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 13) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 12):
          self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 5) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 9):
          self.fond(4)
          self.quitLabel(3)

      if (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] == 15) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] == 14) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] == 13) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] == 12):
          self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX-1] == 5) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 9):
          self.fond(4)
          self.quitLabel(3)

      if (self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] == 12):
          self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb3PositionY+1][self.renderArea.bomb3PositionX] == 5) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 9):
          self.fond(4)
          self.quitLabel(3)

      if (self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] == 15) or (self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] == 14) or (self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] == 13) or (self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] == 12):
          self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] = 0
      elif (self.renderArea.matrice[self.renderArea.bomb3PositionY-1][self.renderArea.bomb3PositionX] == 5) or (self.renderArea.matrice[self.renderArea.bomb3PositionY][self.renderArea.bomb3PositionX+1] == 9):
          self.fond(4)
          self.quitLabel(3)


    #Fenêtre qui affiche le nom du PERSONNAGE 1 en tant que gagnant lorsque sa bombe a touché le PERSONNAGE 2
    def quitLabel(self, n):
      dialog = QMessageBox(self)
      dialog.setWindowTitle("Gagné !")
      if(n==1):
        dialog.setInformativeText("Daenerys Targaryen a gagné ! Voulez-vous rejouer ?")
      if(n==2):
        dialog.setInformativeText("John Snow a gagné ! Voulez-vous rejouer ?")
      if(n==3):
        dialog.setInformativeText("Le Marcheur Blanc a gagné ! Voulez-vous rejouer ?")
      dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
      dialog.setBaseSize(QSize(600, 120))
      dialog.setDefaultButton(QMessageBox.Yes)
      dialog.show()
      result = dialog.exec()
      if result == QMessageBox.No:
        QApplication.instance().quit()
      elif result == QMessageBox.Yes:
        self.initGame() #Redémarrer le jeu = nouvelle partie



    def move_IA(self, a, b, dir, c, bomb):
      self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = a
      if(dir == "x"):
        self.renderArea.positionXIA += c
      else:
        self.renderArea.positionYIA += c
      self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = b
      self.renderArea.update()
      if(bomb):
        self.renderArea.timerBomb3.timeout.connect(self.replace3)
        self.renderArea.timerBomb3.start(1000)


    def position_bomb_IA(self):
      if self.position3 == 1:
        self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = 17
        self.renderArea.update()
      if self.position3 == 11:
        self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = 1717
        self.renderArea.update()
      if self.position3 == 111:
        self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = 171717
        self.renderArea.update()
      if self.position3 == 1111:
        self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] = 17171717
        self.renderArea.update()


    #ITELLIGENCE ARTIFICIELLE (déplacement et pose de bombes)
    def IA(self):
      PositionAleatoire = random.randint(1,4)
      PositionBombeAleatoire = random.randint(1,4)
      if PositionAleatoire == 1:
        if (self.renderArea.matrice[self.renderArea.positionYIA+1][self.renderArea.positionXIA] == 0):
          self.position3 = 1
          if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 1717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 171717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17171717):
            self.move_IA(18, 16, "y", 1, 1)
          else:
            self.move_IA(0, 16, "y", 1, 0)

      elif PositionAleatoire == 2:
        if (self.renderArea.matrice[self.renderArea.positionYIA-1][self.renderArea.positionXIA] == 0):
          self.position3 = 11
          if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 1717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 171717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17171717):
            self.move_IA(18, 1616, "y", -1, 1)
          else:
            self.move_IA(0, 1616, "y", -1, 0)

      elif PositionAleatoire == 3:
        if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA+1] == 0):
          self.position3 = 1111
          if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 1717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 171717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17171717):
            self.move_IA(18, 161616, "x", 1, 1)
          else:
            self.move_IA(0, 161616, "x", 1, 0)

      elif PositionAleatoire == 4:
        if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA-1] == 0):
          self.position3 = 111
          if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 1717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 171717) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA] == 17171717):
              self.move_IA(18, 161616, "x", -1, 1)
          else:
              self.move_IA(0, 161616, "x", -1, 0)

      if PositionBombeAleatoire == 1:
        if (self.renderArea.matrice[self.renderArea.positionYIA+1][self.renderArea.positionXIA] == 15) or (self.renderArea.matrice[self.renderArea.positionYIA+1][self.renderArea.positionXIA] == 14) or (self.renderArea.matrice[self.renderArea.positionYIA+1][self.renderArea.positionXIA] == 13) or (self.renderArea.matrice[self.renderArea.positionYIA+1][self.renderArea.positionXIA] == 12):
          self.position_bomb_IA()
      elif PositionBombeAleatoire== 2:
        if (self.renderArea.matrice[self.renderArea.positionYIA-1][self.renderArea.positionXIA] == 15) or (self.renderArea.matrice[self.renderArea.positionYIA-1][self.renderArea.positionXIA] == 14) or (self.renderArea.matrice[self.renderArea.positionYIA-1][self.renderArea.positionXIA] == 13) or (self.renderArea.matrice[self.renderArea.positionYIA-1][self.renderArea.positionXIA] == 12):
          self.position_bomb_IA()
      elif PositionBombeAleatoire == 3:
        if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA+1] == 15) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA+1] == 14) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA+1] == 13) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA+1] == 12):
          self.position_bomb_IA()
      elif PositionBombeAleatoire == 4:
        if (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA-1] == 15) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA-1] == 14) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA-1] == 13) or (self.renderArea.matrice[self.renderArea.positionYIA][self.renderArea.positionXIA-1] == 12):
          self.position_bomb_IA()
