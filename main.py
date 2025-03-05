import sys
import PyQt5
from PyQt5.QtCore import QMetaObject
from PyQt6.QtCore import QCoreApplication
import PyQt6
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget

class AnotherWindow(QWidget):
   """
   This "window" is a QWidget. If it has no parent, it
   will appear as a free-floating window as we want.
   """
   def __init__(self):
      super().__init__()
      # setting title
      self.Currentuser = str()
      self.setWindowTitle("Python ")

      # setting geometry
      self.setGeometry(100, 100, 100, 100)

      # calling methods
      self.UiComponents()
      self.mainWindowSetup()

      # showing all the widgets
      self.show()






   def UiComponents(self):
      pass
   def mainWindowSetup(self):
      pass


if __name__ == '__main__':
   app = QApplication(sys.argv)

   window = QMainWindow()
   window.show()

   # Start the event loop.
   app.exec()
