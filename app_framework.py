from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import QIcon
import design
import numpy as np
import rc_icons



class MyApp(QMainWindow, design.Ui_MainWindow):
    flag1 = False # flag for equation validation
    flag2 = False # flag for min and max values of X validation

# ------------ Constructor for building the ui and connecting all buttons and textLines ------------
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.plotButton.clicked.connect(self.plot) # connect the plot button with the plot function
        self.inputFunction.textEdited.connect(self.is_eq_valid) # connect the inputFunction textLine with the is_eq_valid function
        self.maxX.textEdited.connect(self.is_max_min_valid) # connect the maxX textLine with the is_max_min_valid function
        self.minX.textEdited.connect(self.is_max_min_valid) # connect the minX textLine with the is_max_min_valid function
        self.plotButton.setEnabled(False) # disable the plot button
        self.MplWidget.canvas.axes.set_xlabel('X') 
        self.MplWidget.canvas.axes.set_ylabel('Y')   
        self.correctIcon = QIcon(":/Icons/Icons/checked.png") # correct icon variable
        self.wrongIcon = QIcon(":/Icons/Icons/warning.png") # wrong icon variable
        

# ------------ Function that plot the function on the canvas ------------
    def plot(self):
        self.MplWidget.canvas.axes.clear()

        x, y = self.readData()
        self.MplWidget.canvas.axes.plot(x, y)
        
        self.MplWidget.canvas.axes.legend(('f(x)',), loc='upper right')
        self.MplWidget.canvas.draw()

# ------------ Function that reads inputs of the user which are (Equation formula, min X, min Y) ------------
# ------------ and return x list and y list after evaluation ------------
    def readData(self):

        min = float(self.minX.text())
        max = float(self.maxX.text())
        equation = self.inputFunction.text()

        x_val, y_val =  self.evaluation(equation, min, max)
        return x_val, y_val
    
    def evaluation(self, equation, min, max):

        e = equation.replace('^', '**')
        x_val = np.linspace(min, max, 1000)
        y_val = []
        for x in x_val:
            y_val.append(eval(e))
        
        return x_val, y_val



# ------------ Function that checks if the equation is valid or not and is connected with the change in the inputFunction textLine ------------
# ------------ It also checks if the min and max values of X are valid or not and is connected with the change in the minX and maxX textLines ------------   
    def is_eq_valid(self):
        eq = self.inputFunction.text()
        eq = eq.replace('^', '**')

        try:
            x = 5.12
            eval(eq)
            
            self.validation_msg.setText('Correct equation but you need to enter the min and max values of X')
            self.validation_msg.setStyleSheet("QLabel { color : green; font: 15pt Segoe UI Black; }")
            self.validation_icon.setIcon(self.correctIcon)
            self.flag1 = True
            
        except:
            self.validation_msg.setText('The equation you entered in the form of f(x) is not valid')
            self.validation_msg.setStyleSheet("QLabel { color : red; font: 15pt Segoe UI Black; }")
            self.validation_icon.setIcon(self.wrongIcon)
            self.plotButton.setEnabled(False)
            self.flag1 = False

        self.validation_message()

# ------------ Function that validates the input of min and max values of X ------------
# ------------ It is connected with the change in the minX and maxX textLines ------------
    def is_max_min_valid(self):
        try:
            minX = float(self.minX.text())
            maxX = float(self.maxX.text())

            self.validation_msg.setText('Correct values but you need to enter a correct equation')
            self.validation_msg.setStyleSheet("QLabel { color : green; font: 15pt Segoe UI Black; }")
            self.validation_icon.setIcon(self.correctIcon)
            
            if minX >= maxX:
                self.plotButton.setEnabled(False)
                self.validation_msg.setText('Max X value must be greater than Min X value')
                self.validation_msg.setStyleSheet("QLabel { color : red; font: 15pt Segoe UI Black; }")
                self.validation_icon.setIcon(self.wrongIcon)
                self.flag2 = False
            else:
                self.flag2 = True
        except:
            self.validation_msg.setText('Please enter suitable number in each field')
            self.validation_msg.setStyleSheet("QLabel { color : red; font: 15pt Segoe UI Black; }")
            self.validation_icon.setIcon(self.wrongIcon)
            self.plotButton.setEnabled(False)
            self.flag2 = False
        
        self.validation_message()


# ------------ Function that checks if the equation and the min and max values of X are valid or not ------------
    def validation_message(self):
        if self.flag1 and self.flag2:
            self.plotButton.setEnabled(True)
            self.validation_msg.setText('Correct equation & values')
            self.validation_msg.setStyleSheet("QLabel { color : green; font: 15pt Segoe UI Black; }")
            self.validation_icon.setIcon(self.correctIcon)
        else:
            self.plotButton.setEnabled(False)
            self.validation_icon.setIcon(self.wrongIcon)

