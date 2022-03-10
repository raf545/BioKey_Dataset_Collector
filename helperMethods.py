from mimetypes import init
import re   
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Helper():

    def checkEmail(email):   
        regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
        if(re.search(regex,email)):   
            return True 
        else:   
            return False
    
    def popupWinError(msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.StandardButton.Close)
        
        returnValue = msgBox.exec()


    def checkTextField(typing):
        if len(typing) < 150:
            return False
        else:
            return True