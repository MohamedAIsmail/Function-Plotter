from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 829)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.MplWidget = MplWidget(self.frame_2)
        self.MplWidget.setObjectName("MplWidget")
        self.gridLayout_9.addWidget(self.MplWidget, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("background-color: rgb(49, 58, 70);\n"
"border-radius: 10px;")
        self.widget.setObjectName("widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.validation_icon = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validation_icon.sizePolicy().hasHeightForWidth())
        self.validation_icon.setSizePolicy(sizePolicy)
        self.validation_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/Icons/warning.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.validation_icon.setIcon(icon)
        self.validation_icon.setIconSize(QtCore.QSize(50, 100))
        self.validation_icon.setObjectName("validation_icon")
        self.gridLayout_8.addWidget(self.validation_icon, 0, 0, 1, 1)
        self.validation_msg = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.validation_msg.sizePolicy().hasHeightForWidth())
        self.validation_msg.setSizePolicy(sizePolicy)
        self.validation_msg.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.validation_msg.setStyleSheet("font: 15pt \"Segoe UI Black\";\n"
"color: rgb(155, 164, 181);")
        self.validation_msg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.validation_msg.setObjectName("validation_msg")
        self.gridLayout_8.addWidget(self.validation_msg, 0, 1, 1, 1)
        self.gridLayout_9.addWidget(self.widget, 1, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("QFrame QLabel {\n"
"color: rgb(155, 164, 181);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(49, 58, 70);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QFrame QLineEdit{\n"
"border-radius: 3px;\n"
"font: 10pt \"Segoe UI Black\"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.minX = QtWidgets.QLineEdit(self.frame_4)
        self.minX.setMaximumSize(QtCore.QSize(50, 16777215))
        self.minX.setAlignment(QtCore.Qt.AlignCenter)
        self.minX.setObjectName("minX")
        self.gridLayout.addWidget(self.minX, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMaximumSize(QtCore.QSize(50, 20))
        self.label.setStyleSheet("\n"
"font: 10pt \"Segoe UI Black\"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.maxX = QtWidgets.QLineEdit(self.frame_4)
        self.maxX.setMaximumSize(QtCore.QSize(50, 16777215))
        self.maxX.setAlignment(QtCore.Qt.AlignCenter)
        self.maxX.setObjectName("maxX")
        self.gridLayout.addWidget(self.maxX, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setMaximumSize(QtCore.QSize(50, 20))
        self.label_3.setStyleSheet("font: 10pt \"Segoe UI Black\"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_4, 2, 1, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.inputFunction = QtWidgets.QLineEdit(self.frame_7)
        self.inputFunction.setMaximumSize(QtCore.QSize(300, 16777215))
        self.inputFunction.setStyleSheet("")
        self.inputFunction.setAlignment(QtCore.Qt.AlignCenter)
        self.inputFunction.setObjectName("inputFunction")
        self.gridLayout_7.addWidget(self.inputFunction, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMaximumSize(QtCore.QSize(300, 20))
        self.label_2.setStyleSheet("font: 12pt \"Segoe UI Black\"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_7, 1, 0, 1, 3)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 67))
        self.frame_6.setStyleSheet("QFrame QPushButton {\n"
"color: rgb(155, 164, 181);\n"
"background-color: rgb(33, 42, 62);\n"
"}\n"
"\n"
"QFrame QPushButton:hover{\n"
"background-color: rgb(241, 246, 249);\n"
"}\n"
"\n"
"QFrame QPushButton:checked{\n"
"color: #fff;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.plotButton = QtWidgets.QPushButton(self.frame_6)
        self.plotButton.setMinimumSize(QtCore.QSize(0, 50))
        self.plotButton.setMaximumSize(QtCore.QSize(130, 16777215))
        self.plotButton.setStyleSheet("font: 12pt \"Segoe UI Black\";\n"
"border-radius: 20px;\n"
"\n"
"")
        self.plotButton.setObjectName("plotButton")
        self.gridLayout_5.addWidget(self.plotButton, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_6, 3, 0, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 4, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 0, 0, 1, 3)
        self.gridLayout_10.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.validation_msg.setText(_translate("MainWindow", "Please fill up all the fields"))
        self.label.setText(_translate("MainWindow", "Min X"))
        self.label_3.setText(_translate("MainWindow", "Max X"))
        self.label_2.setText(_translate("MainWindow", "Please enter your function here"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
from MplWidget import MplWidget
import rc_icons


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
