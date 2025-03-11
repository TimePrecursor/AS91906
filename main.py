import sys
from idlelib.zoomheight import set_window_geometry

import PyQt5
from PyQt5.QtCore import QMetaObject
from PyQt6.QtCore import QCoreApplication
import PyQt6

from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt6.QtWidgets import *


class Window(QMainWindow):
   """
   This "window" is a QWidget. If it has no parent, it
   will appear as a free-floating window as we want.
   """
   def __init__(self):
      super().__init__()
      # setting title
      self.Currentuser = str()
      # self.setWindowTitle("Pythhon ")
      self.setFixedSize(500, 300)
      # setting geometry
      self.setGeometry(100, 100, 100, 100)

      # calling methods
      self.UiComponents()
      self.mainWindowSetup()

      # showing all the widgets
      self.show()






   def UiComponents(self):
      self.TempUserInputBox = QLineEdit(self)
      self.TempUserInputBox.setGeometry(100,100,100,100)
      self.TempUserInputBox.show()


   def mainWindowSetup(self):
      pass


def main():
   # create pyqt5 app
   App = QApplication(sys.argv)

   # create the instance of our Window
   window = Window()

   # start the app
   sys.exit(App.exec())


if __name__ == '__main__':
   main()
